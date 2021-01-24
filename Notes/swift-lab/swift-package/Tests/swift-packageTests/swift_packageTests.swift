import XCTest
@testable import swift_package

final class swift_packageTests: XCTestCase {
    func testExample() {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct
        // results.
        XCTAssertEqual(swift_package().text, "Hello, World!")
    }

    static var allTests = [
        ("testExample", testExample),
    ]
}
