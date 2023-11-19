const fs = require('fs');

// Load json
let rawdata = fs.readFileSync("<filepath>\\<name of the json>");
let data = JSON.parse(rawdata);

// Get data list
let data_list = data["aaa"];

// Get scores
let scores = data_list.filter(item => 'score' in item && item['score'] !== null).map(item => parseFloat(item['score']));

// Calculate average
let average = scores.reduce((a, b) => a + b, 0) / scores.length;