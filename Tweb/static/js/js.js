var timerWidger = function() {
    var init = function(control) {
        var set = function() {
            var str = Date().toString();
            control.html(str);
        };
        set();
        var t = window.setInterval(set, 1000);
    };
    return {
        init: init
    };
}();

var test = function() {
    var postTest = function() {
        $.ajax({
            type: "POST",
            url: "/postTest",
            data: {},
            success: function(data) {
                console.log(data);
            }
        });
    };
    return {
        postTest: postTest
    };
}();