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

**Three checks after installing.**
- `https://YOUR-SITE/shared/` must not list the folder.
- `https://YOUR-SITE/shared/anything-else` must be refused.
- `http://YOUR-SITE/shared/store.php?whoami` (plain HTTP) must be refused or redirected to HTTPS.

The `.htaccess` uses Apache 2.4's `Require all denied`. If the first two checks fail, or the folder gives a 500
error, the host runs an older or different server (some cPanel hosts use LiteSpeed). Replace the `<FilesMatch>`
block's inner line with the older pair `Order allow,deny` and `Deny from all`.

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

## Flags (the `semaphores` rule, on this store)

Installed and tested by the owner and Cloud on 2026-10-15: all eleven authenticated checks passed from Cloud (whoami,
write with the digest echoed, byte-exact read, stat, list, 403 outside its own area, write-once `cited/`, append-only
`log/`, flags, delete). Cloud's heartbeat polls the flags every ten minutes.

- *A flag* is a file in your own folder, `flags/<you>/<to>.<KIND>.<commit>`, where `<to>` is a worker's name or `all`,
  `<KIND>` is `READ-LEDGER`, `REVIEW-REQUEST` or `PRIZE-CANDIDATE`, and `<commit>` is the short hash the reader must
  fetch. Its content is one line, a nonprivate pointer to a committed entry (`CL392`, `PROOFS.md G298`). Flags say
  "look at git, and how urgently"; nothing in a flag is evidence.
- *Acknowledge* by writing `flags/<you>/ack-<from>-<to>.<KIND>.<commit>` (any content). The sender deletes its own
  flag once it sees the ack; nobody can delete anyone else's.
- *State:* `flags/<you>/state` holds one line, written each tick: the time, the heartbeat cadence and what you are on.
- *Reading:* `?list=flags/<worker>` for each worker, or `?list=flags` for the folders. Read only flags addressed to
  you or to `all`.

## Safety

- *Limits on what the script can touch.* The data folder sits outside the web root, so the files are reachable only
  through the script, which checks the token on every request. Paths are plain segments of letters, digits, `.`, `_`
  and `-`, so `..`, hidden files and absolute paths are refused.
- *HTTPS and size.*
  - Plain HTTP is refused. A client's own `X-Forwarded-Proto` header is not believed unless `trust_forwarded_proto`
    is on, which is only for hosts behind a proxy that sets it.
  - Uploads are capped (`max_bytes`, 64 MB by default; the host's own limits may be lower).
  - The whole store is capped too (`max_total_bytes`, 2 GB by default, refused with 507 when full). The store shares
    the hosting account's disk with the website, and `cited/` files cannot be deleted through it, so a runaway
    upload loop or a leaked token must not be able to fill the account.
- *Tokens.* They are random 256-bit values, and only their SHA-256 is stored on the server.
  - To revoke a worker, delete its line in `config.php`.
  - To rotate one, make a new token.
- *The log.* Every write is logged to `sharedstore-private/store.log` with the worker, the operation, the path, the
  size and the SHA-256.
- *Cloud's connection.* Cloud's traffic passes through its environment's policy proxy, which re-terminates TLS. That
  proxy sees the token and the content, which is another reason to keep every token's reach to this one folder.
- *PHP engine bugs (PHP2Shell, 2026-10-21).* CVE-2026-109618 and CVE-2026-109619 are use-after-free bugs in PHP
  itself, reached while PHP parses a `multipart/form-data` body, before store.php runs, so the token check cannot
  stop them. One leaks worker memory, which can hold other requests' tokens. The store never takes multipart or form
  bodies, so `htaccess.example` now refuses multipart at the web server and turns off PHP's own POST parsing and
  upload progress (`enable_post_data_reading`, `session.upload_progress.enabled`). The raw body still reaches the
  script. **Upload with `--data-binary`, never `-F`**: a multipart upload is now answered 403. The lasting fix is a
  patched PHP from the host; keep these lines after it.

## Testing it

`python3 sharedstore/test_store.py` runs the script under PHP's built-in server with a throwaway configuration and
checks 30 behaviours:
- tokens and both header forms;
- each area's permissions, the write-once rule for `cited/` and append-only `log/`;
- path attacks (`..`, absolute paths, hidden files, backslashes, empty segments);
- the size limit, with nothing left behind;
- listing, deleting and the POST fallbacks;
- refusal of plain HTTP, including a spoofed `X-Forwarded-Proto`;
- the total cap;
- the write log.

It printed 30 of 30 on 2026-10-14, with PHP 8.3. The spoofed-header check was added after the first draft, which
would have failed it: the draft answered 200.
