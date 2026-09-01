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
echo "built $HERE/$APP -- double-click it, or: open $APP"
