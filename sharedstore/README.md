# The shared store: a thin HTTPS front end for the workers

*Drafted 2026-10-14 by Cloud at the owner's request ("PHP preferred"). One PHP file on the project's hosted website
gives every worker (Cloud, Local, Intel, GPT) read and write access to one shared folder over HTTPS. There is no SSH,
no shell and no database. Cloud cannot reach SSH or the home network, but it can make HTTPS requests on port 443, and
that is all this needs. In git, call it "the shared store", never by hostname or address (AGENTS item 7).*

## What each worker may do

| Area | Read | Create or replace | Append | Delete |
|---|---|---|---|---|
| `workers/<you>/...` | everyone | you | you | you |
| `flags/<you>/...` | everyone | you | you | you |
| `cited/...` | everyone | anyone, once (never overwritten) | no | no |
| `log/...` | everyone | no | anyone | no |
| anything else | everyone | no | no | no |

- **Live work** goes in your own `workers/<you>/` folder, so two runs never write to the same path.
- **Anything git cites by digest** goes in `cited/`, where it stays fixed. A new version gets a new name.
- **`log/manifest.jsonl`** is the shared, append-only manifest. Each line is one JSON object with `path`, `sha256`,
  `probe`, `commit`, `worker` and `time`.

## Installing it (cPanel, about fifteen minutes)

1. In your home folder (beside `public_html`, not inside it), make a folder `sharedstore-private`, and inside it a
   folder `data`. Nothing in here is reachable from the web.
2. Upload `config.example.php` into `sharedstore-private` as `config.php`. Replace `YOUR-ACCOUNT` in its two paths with
   your account name (cPanel's File Manager shows the home path at the top).
3. Upload `make_token.php` into `sharedstore-private` as well. It runs only from a terminal.
4. Make the folder `public_html/shared`. Upload `store.php` into it, and `htaccess.example` renamed to `.htaccess`.
5. Make one token per worker. In cPanel's Terminal (or over SSH), run:
   ```
   cd ~/sharedstore-private
   php make_token.php cloud
   php make_token.php local
   php make_token.php intel
   php make_token.php gpt
   ```
   - Each run prints a token once, and a line to paste into `config.php` under `'workers'`. That line holds only the
     token's SHA-256.
   - Give each token to its worker through that worker's own secret settings. Never through a chat or git.
   - For Cloud, the place is the cloud environment's settings (the environment menu in the session's title bar, then
     Edit). Put the token under Network secrets, or in an environment variable named `PLACEGO_SITE_TOKEN`.
   - Also add your site's domain under Network access, then Allowed domains.
   - Settings changes take effect in a new Cloud session.
6. Test it from any machine that holds a token:
   ```
   curl -sS -H "X-Store-Token: $PLACEGO_SITE_TOKEN" "https://YOUR-SITE/shared/store.php?whoami"
   ```
   The answer should be `{"worker":"cloud"}`, or whichever worker the token belongs to.

The script needs PHP 8.1 or newer. cPanel's "Select PHP Version" shows and sets it.

## Using it

With `T` holding your token and `S` set to `https://YOUR-SITE/shared/store.php`:

```
curl -sS -H "X-Store-Token: $T" "$S?whoami"
curl -sS -H "X-Store-Token: $T" "$S?list=workers/local"
curl -sS -H "X-Store-Token: $T" "$S?stat=cited/s8/k140_c52.drup"          # bytes, time, sha256
curl -sS -H "X-Store-Token: $T" "$S?path=flags/intel/state"               # read a file
curl -sS -H "X-Store-Token: $T" -X PUT --data-binary @proof.drup "$S?path=workers/cloud/proof.drup"
curl -sS -H "X-Store-Token: $T" -X POST --data-binary @line.json "$S?append=log/manifest.jsonl"
curl -sS -H "X-Store-Token: $T" -X DELETE "$S?path=workers/cloud/proof.drup"
```

Some hosts block PUT or DELETE. If so, `POST "$S?put=<path>"` and `POST "$S?delete=<path>"` do the same.
`Authorization: Bearer <token>` works in place of `X-Store-Token`, but some hosts strip that header, so
`X-Store-Token` is the default.

## Safety

- *Limits on what the script can touch.* The data folder sits outside the web root, so the files are reachable only
  through the script, which checks the token on every request. Paths are plain segments of letters, digits, `.`, `_`
  and `-`, so `..`, hidden files and absolute paths are refused.
- *HTTPS and size.* Plain HTTP is refused. Uploads are capped (`max_bytes`, 64 MB by default; the host's own limits may
  be lower).
- *Tokens.* They are random 256-bit values, and only their SHA-256 is stored on the server.
  - To revoke a worker, delete its line in `config.php`.
  - To rotate one, make a new token.
- *The log.* Every write is logged to `sharedstore-private/store.log` with the worker, the operation, the path, the
  size and the SHA-256.
- *Cloud's connection.* Cloud's traffic passes through its environment's policy proxy, which re-terminates TLS. That
  proxy sees the token and the content, which is another reason to keep every token's reach to this one folder.

## Testing it

`python3 sharedstore/test_store.py` runs the script under PHP's built-in server with a throwaway configuration and
checks 28 behaviours:
- tokens and both header forms;
- each area's permissions, the write-once rule for `cited/` and append-only `log/`;
- path attacks (`..`, absolute paths, hidden files, backslashes, empty segments);
- the size limit, with nothing left behind;
- listing, deleting and the POST fallbacks;
- refusal of plain HTTP;
- the write log.

It printed 28 of 28 on 2026-10-14, with PHP 8.3.
