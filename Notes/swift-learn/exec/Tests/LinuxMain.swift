import XCTest

import execTests

var tests = [XCTestCaseEntry]()
tests += execTests.allTests()
XCTMain(tests)
