var timerSet;

$(function () {
    $("#setTimeout").on("click", function() {
        timerSet = $("#timeout").val();
        $("#timer").html(timerSet.split(":")[0] + " : " + timerSet.split(":")[1]);
    });
})


var interval = setInterval(function() {
    var timer = timerSet.split(":");
    var minutes = parseInt(timer[0], 10);
    var seconds = parseInt(timer[1], 10);
    --seconds;
    minutes = (seconds < 0) ? --minutes : minutes;
    minutes = (minutes < 10) ? "0" + minutes : minutes;
    seconds = (seconds < 0) ? 59 : seconds;
    seconds = (seconds < 10) ? "0" + seconds : seconds;
    $("#timer").html(minutes + " : " + seconds);
    timerSet = $("#timer").html();
    if (minutes + seconds == 0 ? true : false) clearInterval(interval);
}, 1000);
