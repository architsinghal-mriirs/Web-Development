const EventEmitter = require('events');
const eventEmitter = new EventEmitter();

eventEmitter.on('call1',(num1,num2)=>{
  console.log(`The sum is ${num1 + num2}`);
})

eventEmitter.emit("call1", 30,40);

class Person extends EventEmitter
{
  constructor(name){
    super();
    this._name=name;
  }
  get name()
  {
    return this._name;
  }
}

let himanshu = new Person("Himanshu");

himanshu.on('name',()=>{
  console.log(`My name is\t` + himanshu._name);
})
himanshu.emit('name');

const readline = require('readline');
const rl = readline.createInterface({input : process.stdin,
                                    output : process.stdout});
let num1 = 100;
let num2 = 200;
let answer = num1 + num2;

rl.question(`What is the sum of ${num1} and ${num2} ?`, (userInput)=>{
  if(userInput.trim() == answer)
  {
    rl.close();
  }
  else
  {
    rl.setPrompt("Incorrect response. Please try again.");
    rl.prompt();
    rl.on('line',
    (userInput)=>
    {
      if(userInput.trim() == answer)
      {
        rl.close();
      }
      else
      {
        rl.setPrompt("Incorrect answer please try again");
        rl.prompt();
      }
    })
  }
});

rl.on('close',()=>{
  console.log('Correct Answer yolo');
});
