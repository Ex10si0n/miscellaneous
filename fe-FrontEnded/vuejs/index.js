var app = new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue!',
        visible: true,
        tasks: [
            {description: 'Learn JavaScript'},
            {description: 'Learn Vue'},
            {description: 'Build Mobile App'}
        ],
        counter: 0
    },
    methods: {
        add_counter: function() {
            this.counter += 2;
        },
        say: function(what) {
            alert(what);
        }
    },
    created: function() {
        alert("Page Created");
    },
    // updated: function() {
    //    alert("Updated");
    // }
})
