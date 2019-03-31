const EventEmitter = require('events');
const eventEmitter = new EventEmitter();

eventEmitter.on('tutorial', (num1,num2) => {
  console.log(num1+num2);
});

eventEmitter.emit('tutorial',1,2);

class Person extends EventEmitter{
  constructor(name)
  {
    super();
    this._name = name;
  }
  get name(){
    return this._name;
  }
}

let archit = new Person('Archit');
let christina = new Person('Christina');

christina.on('name',()=> {
  console.log('My name is ' + christina.name);
})
archit.on('name',()=>{
  console.log('My name is ' + archit.name);
})
christina.emit('name');
archit.emit('name');
