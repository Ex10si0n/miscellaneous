$(function (){
    $("#c1").on("click", function () {
        $(".toggleable").toggle();
    });

    $("#c2").on("click", function () {
        $("ul li:first").css("background-color", "tomato");
        $("ul li:first").css("color", "white");
    });

    $("#hover").on("mouseenter", function () {
        $(this).css("color", "tomato");
    }).on("mouseleave", function () {
        $(this).css("color", "black");
    });

    $("input").on("focus", function () {
        $(this).css("background-color", "#f8df72");
    });
    $("input").on("blur", function () {
        $(this).css("background-color", "#ededed");
    });

    $("#fade").on("click", function () {
        $("#div1").fadeIn().fadeTo("slow", 0.15);
        $("#div2").fadeIn("slow").fadeTo("slow", 0.15);
        $("#div3").fadeIn(1000).fadeTo("slow", 0.15);
    });

    $("#slide").on("click", function () {
        $("#panel").slideToggle("slow");
    });

    $("#node1").insertBefore($("#node0"))



});