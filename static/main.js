$(document).ready(function() { //document object becomes jquery object in $(); this line allows for buttons to actually do things rather than just be there
    console.log("doc is ready");
    // $('#start-button').click(function() {
    //     console.log("start is clicked");
    //     $.get('/start', {}).done(function() {
    //         document.location.reload();
    //     });
    // });
    var submit_form = function() {
        //const sign = $('#message').val()
        var signs = [];
        var choices = document.querySelectorAll('[id^=textbox]')
        for (var choice in choices) {
            signs.push(choice.val());
        }
        $.post('/submit', {
            message: sign,
            raw_single: signs
        }).done(function() {
            console.log("in submit form function")
            // document.location.reload();
        });
    };

});