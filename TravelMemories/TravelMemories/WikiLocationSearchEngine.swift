//
//  WikiLocationSearchEngine.swift
//  TravelMemories
//
//  Created by Batutin, Andriy on 1/5/15.
//  Copyright (c) 2015 Batutin, Andriy. All rights reserved.
//

import Foundation

public class WikiLocationSearchEngine : NSObject{
    
    public func makeRequestToWikiByLocation(location:String) -> NSDictionary{
        let urlPath: String = location
        var url: NSURL = NSURL(string: urlPath)!
        var request1: NSURLRequest = NSURLRequest(URL: url)
        var response: AutoreleasingUnsafeMutablePointer<NSURLResponse?> = nil
        var error: NSErrorPointer = nil
        var dataVal: NSData =  NSURLConnection.sendSynchronousRequest(request1, returningResponse: response, error:nil)!
        var err: NSError
        var jsonResult: NSDictionary = NSJSONSerialization.JSONObjectWithData(dataVal, options: NSJSONReadingOptions.MutableContainers, error: nil) as NSDictionary
        return jsonResult
    }
    
}