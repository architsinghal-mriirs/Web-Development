/* const todos = [
  {
    id : 1,
    task : 'Learn nodejs',
    status : true
  },
  {
    id : 2,
    task : 'Learn Java',
    status : true
  },
  {
    id : 3,
    task : 'Eat Food',
    status : false
  }

]
console.clear();
//console.log(todos);
//console.log(todos[1].task);

//const todoJSON = JSON.stringify(todos);
//console.log(todoJSON);
//for (var i = 0; i < 10; i++) {
  //console.log(i);
//}

for(let i = 0; i < todos.length; i++) {
  console.log(todos[i].status);
}
for(let tasks of todos){
  console.log(tasks.task);
}

todos.forEach((todo)=>{
  console.log(todo.id);
})


const x = 25;
const check = x > 20 ? 'red' : 'blue';
console.log(check);
*/

function Person(firstName, lastName, dob){
  this.firstName = firstName;
  this.lastName = lastName;
  this.dob = new Date(dob);
  this.getFirstName = () => this.firstName
}

Person.prototype.getBirthYear = function() {
  return  this.dob.getFullYear();
}

const person1 = new Person('Archit','Singhal','4/3/1998\t');
console.log(person1);
console.log(person1.getBirthYear());
console.log(person1.getFirstName());
