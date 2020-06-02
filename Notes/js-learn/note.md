# Java Script 笔记
JavaScript 产生效果的位置:
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title> JavaScript Learn </title>
    </head>
    <body>

    <!--内置脚本-->
        <script>
            ...
        </script>

    <!--外置脚本-->
        <script src="name.js"></script>

    </body>
</html>
```

## Hello World 输入输出
```JavaScript
console.log("Hello World");
var msg = prompt("A Positive Integer"); 
document.write(msg); // document.write方法实际上写入的是html
```

## 变量
```JavaScript
var arr = [];
var str = "String";
var i = 0;
```
### 变量类型
值类型(基本类型)：字符串（String）、数字(Number)、布尔(Boolean)、对空（Null）、未定义（Undefined）、Symbol。
引用数据类型：对象(Object)、数组(Array)、函数(Function)。

## 方法
`toString()`
数值类型的 toString()，可以携带一个参数，输出对应进制的值.
```JavaScript
var num = 16;
console.log(num.toString()); // "16" 默认是10进制
console.log(num.toString(10)); // "16"
console.log(num.toString(2)); // "10000"
console.log(num.toString(8)); // "20"
console.log(num.toString(16)); // "10"
```
`Number()`
把任意值转换成数值，如果要转换的字符串中有一个不是数值的字符，返回 NaN（not a number）
`praseInt()`
把字符串转换成整数
parseInt() 可以传递两个参数，第一个参数是要转换的字符串，第二个参数是要转换的进制
`split()`
```JavaScript
"1:2:3:4".split(":"); // returns ["1", "2", "3", "4"]
"|a|b|c".split("|"); // returns ["", "a", "b", "c"]
```
`join()`
```JavaScript
["1", "2", "3", "4"].join(":"); // returns "1:2:3:4"
["", "a", "b", "c"].join("|"); // returns "|a|b|c"
```
`push(), pop()`
数组的追加和删除操作，类似栈操作

## 代码块
`if ()`

```JavaScript
if (true) {
    console.log("true");
} else {
    console.log("false");
}
```
`switch ()`

**三目运算符**

`for (;;)` & `continue; break;`

```JavaScript
for (var i = 0; i < 100; i += 1) {
    console.log(i);
}
```
`while ()`

`function funcName(parameters) { // PASS }`
函数声明 与 函数表达式
JavaScript 无 重载

```JavaScript
function f(a, b) {
    console.log(a + b);
    return a + b;
}
f(2, 3);

var f = function f(a, b) {
    return a + b;
}
console.log(f(2, 3));
```
匿名函数
```JavaScript
var myButton = document.querySelector("button");

myButton.onclick = function () {
    alert("hello");
};
```
匿名函数的自调用
```JavaScript
(function () {
    alert("hello");
})();
```
## JSON - JavaScript Object Notaion
- JSON 是一种纯数据格式,它只包含属性，没有方法。
- JSON 的属性必须通过双引号引起来。
- JSON 要求两头有 {} 来使其合法。
- 可以把 JavaScript 对象原原本本的写入 JSON 数据，比如：字符串，数字，数组，布尔还有其它的字面值对象。
```json
{
    "name": "张三",
    "age": 18,
    "gender": "male"
}
```

## 对象
### Array
`concat(arr)``join("")``pop()``push(4)``reverse()`
`shift()` 反向pop()
`unshift()` push_back()
`slice(2, 5)` 数组切片，返回新数组
`splice()`
arrayObject.splice(start, deleteCount, options);
// start 值是必需的，规定删除或替换项目的位置
// deleteCount 值是必需的，规定要删除的项目数量，如果设置为 0，则不会删除项目
// options 值是可选的，规定要替换的新项目
// 和 slice() 方法不同的是 splice() 方法会修改数组
`sort()`

### String
`charAt()`
`concat()` 方法，连接字符串，等效于 “+”，“+” 更常用。与数组中的 concat() 方法相似。
`slice()` 方法，提取字符串的片断，并在新的字符串中返回被提取的部分（字符串章节有详细介绍，这里不过多的赘述，下面的类似情况同样处理）。
`indexOf()` 方法，检索字符串。
`toString()` 方法，返回字符串。
`toLowerCase()` 方法，把字符串转换为小写。
`toUpperCase()` 方法，把字符串转换为大写。
`replace()` 方法，替换字符串中的某部分。
`split()` 方法，把字符串分割为字符串数组。

### Date
`Date()`：返回当日的日期和时间（输出的是中国标准时间）。
`getDate()`：从 Date 对象返回一个月中的某一天 (1 ~ 31)。
`getDay()`：从 Date 对象返回一周中的某一天 (0 ~ 6)。
`getMonth()`：从 Date 对象返回月份 (0 ~ 11)。
`getFullYear()`：从 Date 对象以四位数字返回年份。
`getHours()`：返回 Date 对象的小时 (0 ~ 23)。
`etMinutes()`：返回 Date 对象的分钟 (0 ~ 59)。
`getSeconds()`：返回 Date 对象的秒数 (0 ~ 59)。
`getMilliseconds()`：返回 Date 对象的毫秒(0 ~ 999)。
日期对象的格式化: `yyyy/MM/dd HH:mm:ss`
```JavaScript
function formatDate(d) {
    if (!d instanceof Date) return;
    var year = d.getFullYear(),
        month = d.getMonth() + 1,
        date = d.getDate(),
        hour = d.getHours(),
        minute = d.getMinutes(),
        second = d.getSeconds();
    month = month < 10 ? "0" + month: month;
    date = date < 10 ? "0" + date: date;
    hour = hour < 10 ? "0" + hour: hour;
    minute = minute < 10 ? "0" + minute: minute;
    second = second < 10 ? "0" + second: second;
    return year + "/" + month + "/" + date + "/" + hour + "/" + ":" + minute + ":" + second;
}

console.log(formatDate(new Date()));
```


### Math
#### 属性
E: 2.718281828
LN2: ln 2
LN10: ln 10
LOG2E: log_{2}e
LOG10E: log_{10}e
PI: 3.1415926535
SQRT1_2: sqrt(0.5)
SQRT2: 1.4142135624

### 方法
`abs(x)` ：返回 x 的绝对值。
`round(x)` ：返回 x 四舍五入后的值。
`sqrt(x)` ：返回 x 的平方根。
`ceil(x)` ：返回大于等于 x 的最小整数。
`floor(x)` ：返回小于等于 x 的最大整数。
`sin(x)` ：返回 x 的正弦。
`cos(x)` ：返回 x 的余弦。
`tan(x)` ：返回 x 的正切。
`acos(x)` ：返回 x 的反余弦值（余弦值等于 x 的角度），用弧度表示。
`asin(x)` ：返回 x 的反正弦值。
`atan(x)` ：返回 x 的反正切值。
`exp(x)` ：返回 e 的 x 次幂 (e^x)。
`pow(n, m)` ：返回 n 的 m 次幂 (nm)。
`log(x)` ：返回 x 的自然对数 (ln x)。
`max(a, b)` ：返回 a, b 中较大的数。
`min(a, b)` ：返回 a, b 中较小的数。
`random()` ：返回大于 0 小于 1 的一个随机数。

### 自定义
```JavaScript
// 通过对象字面量来创建
var student = {
    name: "张三",
    age: 19,
    gender: "male",
    sayHello: function () {
        document.write("Hi! My Name is " + this.name);
    },
};

// new Object()
var student = new Object();
(student.name = "张三"),
(student.age = 18),
(student.gender = "male"),
(student.sayHello = function () {
    console.log("Hi! My Name is " + this.name);
});

// 通过构造函数创建对象
function createStudent(name, age, gender) {
    var student = new Object();
    student.name = name;
    student.age = age;
    student.gender = gender;
    student.sayHello = fucntion () {
        console.log("Hi! My Name is " + this.name);
    };
    return student;
}
var s1 = createStudent("张三", 18, "male");
```
删除对象属性
```JavaScript
delete student.name;
```

## BOM
### window 对象
#### 对话框
`alert()`：显示带有一段消息和一个确认按钮的警告框。
`prompt()`：显示可提示用户输入的对话框。
`confirm()`：显示带有一段消息以及确认按钮和取消按钮的对话框。

#### 页面加载事件
`onload`
```JavaScript
window.onload = function () {
  // 当页面加载完成执行
  // 当页面完全加载所有内容（包括图像、脚本文件、CSS 文件等）执行
};
```
`onunload`
```JavaScript
window.onunload = function () {
  // 当用户退出页面时执行
};
```
#### 浏览器尺寸
```JavaScript
var width = window.innerWidth;
document.documentElement.clientWidth;
document.body.clientWidth;

var height = window.innerHeight;
document.documentElement.clientHeight;
document.body.clientHeight;
```
上述代码可以获取所有浏览器的宽高（不包括工具栏/滚动条）。

#### 定时器

`setTimeout()` 方法在指定的毫秒数到达之后执行指定的函数，只执行一次。
`clearTimeout()` 方法取消由 `setTimeout()` 方法设置的 timeout。

```JavaScript
// 创建一个定时器，2000毫秒后执行，返回定时器的标示
var timerId = setTimeout(function () {
  console.log("Hello shiyanlou");
}, 2000);

// 取消定时器的执行
clearTimeout(timerId);
```
`setInterval()` 方法设置定时调用的函数也就是可以按照给定的时间（单位毫秒）周期调用函数，`clearInterval()` 方法取消由 `setInterval()` 方法设置的 timeout。
```JavaScript
// 创建一个定时器，每隔 2 秒调用一次
var timerId = setInterval(function () {
  var date = new Date();
  console.log(date.toLocaleTimeString());
}, 2000);

// 取消定时器的执行
clearInterval(timerId);
```

## DOM Document Object Model
`document.write()` 可用于直接向 HTML 输出流写内容
`innerHTML` 属性
```html
<p id="p1">Hello</p>
<script>
    document.getElementById("p1").innerHTML = "Hello World";
</script>
```
`style` 属性
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title></title>
  </head>
  <body>
    <p id="myId" style="color: blue;">Test Words</p>
    <script>
      document.getElementById("myId").style.color = "tomato";
    </script>
  </body>
</html>
```
### DOM 节点

| Node         | Name          | Description             |
| ------------ | ------------- | ----------------------- |
| Document     | Document      | Window.document         |
| DocumentType | Document Type | Type                    |
| Element      | Elements      | `<head>, <body>, <h1>`  |
| Attribute    | Attribute     | `class="myClass"`       |
| Text         | Text          | Texts in HTML documents |

`document.getElementById();`
`document.getElementsByTagName()[0];`
`document.getElementsByClassName()[0];`

### DOM 事件

| 事件名      | 说明                                 |
| ----------- | ------------------------------------ |
| onclick     | 鼠标单击                             |
| ondblclick  | 鼠标双击                             |
| onkeyup     | 按下并释放键盘上的一个键时触发       |
| onchange    | 文本内容或下拉菜单中的选项发生改变   |
| onfocus     | 获得焦点，表示文本框等获得鼠标光标。 |
| onblur      | 失去焦点，表示文本框等失去鼠标光标。 |
| onmouseover | 鼠标悬停，即鼠标停留在图片等的上方   |
| onmouseout  | 鼠标移出，即离开图片等所在的区域     |
| onload      | 网页文档加载事件                     |
| onunload    | 关闭网页时                           |
| onsubmit    | 表单提交事件                         |

## Function 对象

### arguments 对象
```JavaScript
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
```
