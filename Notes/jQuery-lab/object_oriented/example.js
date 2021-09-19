let circle = {
    x: 2, y: 3,
    radius: 5,
    fillColor: 'red',
    area: function () {
        return Math.PI * this.radius ** 2
    },
    resize: function (factor) {
        this.radius = this.radius * factor;
        return this
    },
};

console.log(`Area of the circle is ${circle.area()}`)
console.log(`Area of the new circle is ${circle.resize(2).area()}`)
