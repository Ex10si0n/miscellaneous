$(function() {

    $(".father").on("click", function() {
        alert("father on click");
    });

    $(".son").on("click", function() {
        alert("son on click");
        // event.stopPropagation();
    })

    $(".grandson").on("click", function() {
        alert("grandson on click");
        event.stopPropagation();
    })

    $(document).on("click", function() {
        alert("document on click");
    });
});