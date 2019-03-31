 const fs = require('fs');
/*fs.writeFile('Example.txt', '\nThis is an example\n', (err)=>{
  if(err){
    console.log(err);
    }
  else {
      console.log('\nFile successfully created\n');
      fs.readFile('Example.txt','utf-8',(err,file)=>{
        if(err){
          console.log(err);
        }
        else {
          console.log(file);
        }
      })
    }
  });


fs.rename('example.txt', 'example2.txt',(err)=>{
  if(err){
    console.log(err);

  }
  else {
    console.log('successfully renamed the file');
  }
});

fs.appendFile('example2.txt','Some data is appended',(err)=>{
  if(err){
    console.log(err);
  }
    else {
      console.log("Successfully appended data to file");
    }

});
*/

fs.unlink('example2.txt',(err)=>
{
  if(err){
    console.log(err);
  }
  else{
    console.log("suucesffully deleted the file");
  }
})
