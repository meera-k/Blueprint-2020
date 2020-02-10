$(document).ready(function() { //document object becomes jquery object in $(); this line allows for buttons to actually do things rather than just be there
    console.log("doc is ready");
    // $('#start-button').click(function() {
    //     console.log("start is clicked");
    //     $.get('/start', {}).done(function() {
    //         document.location.reload();
    //     });
    // });

});


function submit_form() {
    //const sign = $('#message').val()
    // debugger;
    var signs = [];
    var choices = document.querySelectorAll('[type^=checkbox]')
    console.log(choices)
    for (var choice in choices) {
        console.log(choices[choice].value)
        signs.push(choices[choice].value);
    }
    // $.post('/submit', {
    //     // message: sign,
    //     // raw_single: signs
    // }).done(function() {
    //     console.log("in submit form function")
    // });
    window.location = "/results";
};