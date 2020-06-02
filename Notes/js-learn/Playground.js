var student = {
    name : "zhangsan",
    age : 18,
    gender : "male",
    sayHi: function () {
        document.write("[By Student Class] Hi, my name is " + this.name);
    },
};

function stud(name, age, gender) {
    this.name = name;
    this.age = age;
    this.gender = gender;
    this.sayHi = function () {
        document.write("[By stud Construct func] Hi, my name is " + this.name);
    };
}
var s1 = new stud("lisi", 18, "male");

student.sayHi();
document.write("<br>");
s1.sayHi();

document.write("<br> <h3> Recursion </h3>");

function fac(n) {
    if (n == 0) return 1;
    return fac(n-1)*n;
}

document.write(fac(10));

document.write("<br> <h3> Closure </h3>");

function f1() {
    var n1 = 6;
    function f2() {
        var n2 = 7;
        return n2;
    }
    return f2();
    document.write(n1 + n2)
}

f1();

document.write("<br> <h3> args </h3>");

function add() {
    var sum = 0;
    for (var i = 0; i < arguments.length; i++) {
        sum += arguments[i];
    }
    return sum;
}
document.write(add() + "<br>");
document.write(add(1) + "<br>");
document.write(add(1, 2) + "<br>");
document.write(add(1, 2, 3) + "<br>");

var add = new Function("a", "b", "document.write(a+b);");
add(2, 5);

document.write("<br> <h3> functions </h3>");
var add = new Function("a", "b", "console.log(a+b);");
document.write("valueOf() Method<br><pre>"+add.valueOf()+"</pre>");
document.write("<br>toString() Method<br><pre>"+add.toString()+"</pre>");

