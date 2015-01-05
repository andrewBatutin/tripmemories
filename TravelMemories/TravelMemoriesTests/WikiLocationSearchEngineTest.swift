//
//  WikiLocationSearchEngineTest.swift
//  TravelMemories
//
//  Created by Batutin, Andriy on 1/5/15.
//  Copyright (c) 2015 Batutin, Andriy. All rights reserved.
//

import UIKit
import XCTest

class WikiLocationSearchEngineTest: XCTestCase {
    
    override func setUp() {
        super.setUp()
        // Put setup code here. This method is called before the invocation of each test method in the class.
    }
    
    override func tearDown() {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
        super.tearDown()
    }
    
    func testExample() {
        // This is an example of a functional test case.
        XCTAssert(true, "Pass")
    }
    
    func testWikiLocationrequest(){
        let sut = WikiLocationSearchEngine()
        let res = sut.makeRequestToWikiByLocation("https://en.wikipedia.org/w/api.php?action=query&list=geosearch&gsradius=1000&gscoord=45.462321%7C9.234825&format=json")
        println(res)
    }
    
    func testPerformanceExample() {
        // This is an example of a performance test case.
        self.measureBlock() {
            // Put the code you want to measure the time of here.
        }
    }
    
}