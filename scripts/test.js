//
//  streetAreaExample.js
//  examples
//
//  Created by Ryan Huffman on 5/4/14
//  Copyright 2014 High Fidelity, Inc.
//
//  This is an example script showing how to load JSON data using XMLHttpRequest.
//
//  URL Macro created by Thijs Wenker.
//
//  Distributed under the Apache License, Version 2.0.
//  See the accompanying file LICENSE or http://www.apache.org/licenses/LICENSE-2.0.html
//

var url = "https://script.google.com/macros/s/AKfycbwIo4lmF-qUwX1Z-9eA_P-g2gse9oFhNcjVyyksGukyDDEFXgU/exec?action=listOwners&domain=alpha.highfidelity.io";
print("Loading street data from " + url);

var req = new XMLHttpRequest();

// Set response type to "json".  This will tell XMLHttpRequest to parse the response data as json, so req.response can be used
// as a regular javascript object
req.responseType = 'json';

req.open("GET", url, false);
req.send();

if (req.status == 200) {


} else {

}