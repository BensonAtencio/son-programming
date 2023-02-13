// https://youtu.be/hdI2bqOjy3c

// console.log("Hello World");
// console.error('Error ito');
// console.warn('warning');

// let, const
    // let age = 30;
    // age = 18;
    // const x = 2022;
    // console.log(x);
    // console.log(age);

//Strings, Numberss, Boolean, null, undefined
    // const name = 'John';
    // const age = 36;
    // const deci = 4.5;
    // const male = true;
    // const x = null;
    // const y = undefined;
    // let z;
    // console.log(typeof x);

//Concatenation
    // const name = 'Cardo';
    // const age = 999;
    // //old way
    // console.log('My name is ' + name + ' and I am ' + age);
    // //new way
    // console.log(`My name is ${name} and I am ${age}`);

//string functions
    // const x = 'Hello World, a, b, c, d';
    // console.log(x.length);
    // console.log(x.toUpperCase());
    // console.log(x.toLowerCase());
    // console.log(x.substring(0, 5).toUpperCase());
    // console.log(x.split(', '));

//arrays
// const numbers = new Array(1, 2, 3, 4, 5);
// const numbers = [0, 1, 2, 3, 4];
// numbers[4] = 5;
// numbers.push(5);
// numbers.unshift(-1);
// numbers.pop();
// console.log(Array.isArray(numbers));
// console.log(numbers.indexOf(4));
// console.log(numbers);

//object literals
// const person = {
//     firstName: 'Jane',
//     lastName: 'Doe',
//     age: 30,
//     hobbies: ['music', 'singing'],
//     address: {
//         street: '123',
//         city: 'Batangas',
//         state: 'LA'
//     }
// }
// console.log(person.firstName, person.lastName);
// console.log(person.address.city);
// const { firstName, lastName, address:{city} } = person;
// console.log(firstName, lastName, city);
// console.log(person);
// person.email = 'janedoe@gmail.com';

// const todos = [
//     {
//         id: 1,
//         text: 'Take out trash',
//         isDone: true
//     },
//     {
//         id: 2,
//         text: 'Wash Plates',
//         isDone: true
//     },
//     {
//         id: 3,
//         text: 'Wash clothes',
//         isDone: false
//     }
// ];

// todos[2].isDone = true;
// console.log(todos[1].text);
// console.log(todos);
// const todoJSON = JSON.stringify(todos);
// console.log(todoJSON);

//for loops
// for(let i = 0; i < 10; i++){
//     console.log(`For loop number ${i}`);
// }
// //while loops
// let i = 0;
// while(i < 10){
//     console.log(`While loop number ${i}`);
//     i++
// }
// for(let i = 0; i < todos.length; i++){
//     console.log(todos[i]);
// }
// for(let i of todos){
//     console.log(i);
//     console.log(i.text);
// }

//foreach, map, filter

// todos.forEach(function(todo){
//     console.log(todo);
// });

// const todoT = todos.map(function(todo){
//     return todo.text;
// });
// console.log(todoT);

// const todoC = todos.filter(function(todo){
//     return todo.isDone === true;
// })
// console.log(todoC);

// const todoC = todos.filter(function(todo){
//     return todo.isDone === true;
// }).map(function(todo){
//     return todo.text
// })
// console.log(todoC);

// const x = 9;
// const y = 12;

// if(x >= 10 && y >= 10){
//     console.log('1');
// }else if (x > 10){
//     console.log('2');
// }else{
//     console.log('3');
// }

// const x = 10;
// const color = x > 10 ? 'red' : ' blue';

// const col = 'green';
// switch(col){
//     case 'red':
//         console.log('red ito');
//         break;
//     case 'blue':
//         console.log('blue ito');
//         break;
//     default:
//         console.log('unknown color');
//         break;
// }

// function addNums(x, y){
//     return x + y;
// }
// const addNums = (x, y) => {
//     return x + y;
// }
// const addNums = num1 => num1 + 5;
// console.log(addNums(6));


//object oriented es5
// function Person(fName, lName, dBirth){
//     this.fName = fName;
//     this.lName = lName;
//     this.dBirth = new Date(dBirth);
// }

// Person.prototype.getByear = function(){
//     return this.dBirth.getFullYear();
// }
// Person.prototype.getFullname = function(){
//     return `${this.fName} ${this.lName}`
// }

// const person1 = new Person('John', 'Doe', '11-11-2001');
// const person2 = new Person('Jane', 'Doe', '12-12-2002');
// console.log(person1.getByear());
// console.log(person2.getByear());
// console.log(person1.getFullname());
// console.log(person2.getFullname());
// console.log(person1);
// console.log(person2);

//object oriented es6 , classes
// class Person {
//     constructor(fName, lName, dBirth){
//         this.fName = fName;
//         this.lName = lName;
//         this.dBirth = new Date(dBirth);
//     }
//     getByear(){
//         return this.dBirth.getFullYear();
//     }
//     getFullname(){
//         return `${this.fName} ${this.lName}`;
//     }
// }
// const person1 = new Person('John', 'Doe', '11-11-2001');
// const person2 = new Person('Jane', 'Doe', '12-12-2002');
// console.log(person1.getByear());
// console.log(person2.getByear());
// console.log(person1.getFullname());
// console.log(person2.getFullname());
// console.log(person1);
// console.log(person2);

//DOM 
// document.getElementById('my-form');
// document.getElementsByClassName('item');
// document.getElementsByTagName('li');
// document.querySelector('h1');
// const items = document.querySelectorAll('.item');

// items.forEach(function(item){
//     console.log(item);
// })

// const ul = document.querySelector('.items');
// // ul.remove();
// // ul.lastElementChild.remove();
// ul.firstElementChild.textContent = 'hello';
// ul.children[1].innerText = 'Brad';
// ul.lastElementChild.innerHTML = '<h1>Hello</h1>'; 

// const btn = document.querySelector('.btn');
// // btn.style.background = 'red';

// const btn = document.querySelector('.btn');
// btn.addEventListener('click', (e) =>{
//     // e.preventDefault();
//     document.querySelector('#my-form').style.background = 'red';
//     document.querySelector('body').classList.add('bg-dark');
//     document.querySelector('.items').lastElementChild.innerHTML = '<h1>Hellooooooooo</h1>';
// });

// const myForm = document.querySelector('#my-form');
// const name = document.querySelector('#name');
// const ema = document.querySelector('#email');
// const msg = document.querySelector('.msg');
// const userL = document.querySelector('#users');

// myForm.addEventListener('submit', onSub);

// function onSub(e){
//     e.preventDefault();
//     if (name.value === '' || ema.value === ''){
//         msg.classList.add('error');
//         msg.innerHTML = 'Please enter all fields';
//         setTimeout(() => msg.remove(), 2000)
//     }else{
//         const li = document.createElement('li');
//         li.appendChild(document.createTextNode(`${name.value} : ${ema.value}`));

//         userL.appendChild(li);

//         name.value = '';
//         ema.value = '';
//     }
// }
