var http = require('http');
var express = require('express');
var port = 8000;
var app = express();
var appRoutes = require('./routes/appRoutes');
var mongoose = require('mongoose');
var bodyParser = require('body-parser');

mongoose.connect('mongodb://localhost/meanDb',{useMongoClient:true});

app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());
app.use('/',appRoutes);

http.createServer(app).listen(port);

console.log('running on port 8000');
