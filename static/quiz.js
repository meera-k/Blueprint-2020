console.log("hello world");

let month;

function startQuiz() {
    alert("go to quiz");
    //document.querySelector("#body").style.backgroundImage = ---
}

window.transitionToPage = function (href) {
    document.querySelector('body').style.opacity = 0;
    this.setTimeout(function () {
        window.location.href = href
    }, 500)
}

document.addEventListener('DOMContentLoaded', function (event) {
    document.querySelector('body').style.opacity = 1;
})

function getNumDays() {
    console.log(month);
    switch (month) {
        case "2":
            console.log(28)
            return 28;
        case "4":
        case "6":
        case "9":
        case "11":
            console.log(30)
            return 30;
        default:
            console.log(31)
            return 31;
    }
}

function setDay() {
    console.log("hi");
    month = document.getElementById("month").options[document.getElementById("month").selectedIndex].value;
    console.log(month);
    
}

function getMonth() {
    return month;
}

function printDays() {
    for(var d=1;d<=getNumDays();d++) {
        document.write("<option>"+d+"</option>");
    }
}