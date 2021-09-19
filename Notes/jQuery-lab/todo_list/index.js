$(function () {
    var inputText = $("#txt1");
    var btn = $("#btn1");
    var ul = $("#list");

    function top() {
        console.log(this.father.name)
    }

    btn.on("click", function() {
        var val = inputText.val();
        if (val == "") {
            alert("Need text input");
            return;
        }
        var li = `<li style="padding: 20px"><span>${val}</span><button class="top" style="float:right; margin-right:2px">Top</button><button class="done" style="float:right; margin-right:10px">Done</button></li>`;
        var a = li.find(".del");
        a.on("click", function() {
            $(this).parent().remove();
        })
        ul.append(li);
        inputText.val('');
    });




});