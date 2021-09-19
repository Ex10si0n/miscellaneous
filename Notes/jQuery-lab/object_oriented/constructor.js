function Student(name, id, gpa) {
    this.name = name;
    this.id = id;
    this.gpa = gpa;
    this.sayHi = function () {
        console.log(name + ": Hi!");
    }
}

var eden = new Student("Eden", "P1908370", 4.13);
var kevyn = new Student("Kevyn", "P1908399", 3.14);

console.log(eden);
console.log(kevyn);
kevyn.sayHi();