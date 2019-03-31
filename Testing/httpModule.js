//To create a web server use http
const http = require('http');
const server = http.createServer((req,res)=>{
if(req.url =='/'){
  res.write('Heloo world from node js');
  res.end();
}
else {
  res.write('Using some other domain');
}
});

server.listen('3000');
