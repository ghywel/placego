#!/usr/bin/env bash
# Wrap QuadDemoUI into a double-clickable QuadDemo.app. No Xcode, no
# signing identity, no App Store: the bundle is ad-hoc signed, which runs
# cleanly on the machine that built it. (A DOWNLOADED copy of the .app
# will hit Gatekeeper's unidentified-developer prompt -- that is Apple's
# toll on distribution, not a defect here; recipients build from source
# or use right-click -> Open.)
#
#   ./make-app.sh        # builds release + bundles graphs into Resources
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$HERE"
[ -d generated ] || ./gen.sh
swift build -c release
APP=QuadDemo.app
rm -rf "$APP"
mkdir -p "$APP/Contents/MacOS" "$APP/Contents/Resources"
cp .build/release/QuadDemoUI "$APP/Contents/MacOS/"
cp -R generated generated-accel generated-jerk "$APP/Contents/Resources/"
cat > "$APP/Contents/Info.plist" <<'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
 "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key><string>QuadDemoUI</string>
    <key>CFBundleIdentifier</key><string>local.placego.quaddemo</string>
    <key>CFBundleName</key><string>Quaddirectional</string>
    <key>CFBundlePackageType</key><string>APPL</string>
    <key>CFBundleShortVersionString</key><string>1.0</string>
    <key>LSMinimumSystemVersion</key><string>13.0</string>
    <key>NSHighResolutionCapable</key><true/>
</dict>
</plist>
PLIST
# exFAT scatters AppleDouble (._*) files into the bundle and codesign
# refuses to sign over them -- the drive's usual junk, new costume.
find "$APP" -name '._*' -delete
codesign --force --deep -s - "$APP"
# The .app is a directory and stays out of git; the archive is the
# single-file artifact for sharing or attaching to a release. ditto is
# the canonical archiver here -- plain `zip -r` can mangle the signature
# metadata inside a bundle.
ditto -c -k --keepParent "$APP" QuadDemo-macos-$(uname -m).zip
# The mirror ships the archive alongside the docs: refresh the copy at
# scripts/ level so a rebuild never leaves a stale zip in the repo.
cp -f "QuadDemo-macos-$(uname -m).zip" "$HERE/../QuadDemo-macos-$(uname -m).zip"
echo "built $HERE/$APP -- double-click it, or: open $APP"
echo "archive: QuadDemo-macos-$(uname -m).zip (recipients: right-click -> Open past Gatekeeper)"
