#!/bin/bash
# Tighten this folder. Everything in it except Sources/, spike/, the scripts
# and Package.swift is either a compiler cache or a build product, and none of
# it is tracked (see .gitignore). The problem is the WORKING TREE: on the exFAT
# pool this repository lives on, clusters are 128 KB, so the ~2,000 small files
# of a SwiftPM build plus gen.sh's per-pass output cost about half a gigabyte
# and make every copy, sync and `git status` crawl.
#
#   ./clean.sh           delete .build/ and macOS ._ sidecars; MOVE QuadDemo.app/,
#                        generated*/ and the zip into
#                        $ARTIFACTS/<zip date>/  (default: ../../../metal-demo-artifacts,
#                        i.e. beside the repository, never inside it)
#   ./clean.sh --purge   delete them instead of moving. Safe: the zip contains
#                        the app, the app contains generated*/, and gen.sh
#                        remakes generated*/ from the committed shaders.
#
# Regenerate afterwards, on the Mac:  ./gen.sh  ->  swift build -c release
# ->  ./make-app.sh   (README.md has the prerequisites).
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$HERE" || exit 1
ART="${ARTIFACTS:-$HERE/../../../metal-demo-artifacts}"
PURGE=0; [ "${1:-}" = "--purge" ] && PURGE=1

before="$(du -sh . | cut -f1) / $(find . -type f | wc -l) files"

rm -rf .build
find . -name '._*' -type f -delete
find . -name '.DS_Store' -type f -delete

stamp="$(date +%F)"
[ -f QuadDemo-macos-arm64.zip ] && stamp="$(date -r QuadDemo-macos-arm64.zip +%F 2>/dev/null || echo "$stamp")"
moved=0
for item in QuadDemo.app generated generated-* QuadDemo-macos-*.zip; do
  [ -e "$item" ] || continue
  if [ $PURGE = 1 ]; then
    rm -rf "$item"
  else
    mkdir -p "$ART/$stamp-build" || exit 1
    rm -rf "$ART/$stamp-build/$item"
    mv "$item" "$ART/$stamp-build/" || exit 1
  fi
  moved=$((moved + 1))
done
[ $PURGE = 1 ] && verb=deleted || verb="moved to $ART/$stamp-build/"
echo "$moved build product(s) $verb; .build/ and sidecars deleted"
echo "before: $before"
echo "after:  $(du -sh . | cut -f1) / $(find . -type f | wc -l) files"
