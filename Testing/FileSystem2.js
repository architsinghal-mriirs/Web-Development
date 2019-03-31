const fs = require('fs');
/*
fs.mkdir('tut',(err)=>{
  if(err){
    console.log(err);
  }
  else {
    fs.writeFile('./tut/example1.txt','This is a file within the tut folder',(err)=>{
      if(err)
      {
        console.log(err);
      }
      else {
        console.log("Successfully created a file within a folder");
      }
    })
  }
})
*/

fs.unlink('./tut/example1.txt',(err)=>{
  if(err)
  {
    console.log(err);
  }
  else{ fs.rmdir('tut',(err)=>
  {
    if(err){
      console.log(err);
    }
    else {
      console.log("deleted folder");
    }
  })
    console.log("successfully deleted the file");
  }
})
