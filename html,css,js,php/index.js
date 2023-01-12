/*class Person{
    constructor(name, age){
        this.name = name;
        this.age = age;
    }
}

class Degree extends Person {
    constructor(name, age, degree){
        super(name, age);
        this.degree = degree;
    }
}

class Cars extends Degree {
    constructor(name, age, degree, car){
        super(name, age, degree);
        this.car = car;
    }

    fullDetails(){
        return `${this.name} is ${this.age} years old and finishes ${this.degree} driving ${this.car}`;
    }
}
const person1 = new Cars("Leo", 200, "BSIT", "Honda");
const person2 = new Cars("Franco", 300, "BSCS", "Toyota");

console.log(person1);
console.log(person2);
*/


document.getElementById("btn").onmouseover = function() {mouseOver()};
document.getElementById("btn").onmouseout = function() {mouseOut()};
function mouseOver(){
    document.getElementById("btn").style.color = "Red";
}
function mouseOut(){
    document.getElementById("btn").style.color = "Black";
}
