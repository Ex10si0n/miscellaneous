import XCTest

import swift_packageTests

var tests = [XCTestCaseEntry]()
tests += swift_packageTests.allTests()
XCTMain(tests)
