// swift-tools-version:5.9
// The native Metal host for the quaddirectional shader (METALPORT.md).
// Build: ./gen.sh first (regenerates generated/ from the GLSL source of
// truth), then `swift build -c release`.
import PackageDescription

let package = Package(
    name: "QuadDemo",
    platforms: [.macOS(.v13)],
    targets: [
        .executableTarget(name: "QuadDemo", path: "Sources/QuadDemo")
    ]
)
