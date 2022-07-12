class Person {
    constructor(name, age, sex){
        this.name = name;
        this.age = age;
        this.sex = sex;
    }

    fullDetails() {
        return `${this.name} is a ${this.age} year old ${this.sex}`;
    }
}

const person1 = new Person("John", 25, "Male");

console.log(person1);
console.log(person1.fullDetails());