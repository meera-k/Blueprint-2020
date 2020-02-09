console.log("hello world");

function getRandomDog() {
    //alert("NOW GETTING A DOG!!!!!!11!!!1!");
    fetch("https://dog.ceo/api/breeds/image/random")
        .then(res => res.json())
        .then(function(data) {
            document.querySelector("#dog-image").style.backgroundImage = `url(${data.message})`;
          });
}

function getSpecificDog() {
    const name = document.querySelector("#dog-name").value;
    fetch(`https://dog.ceo/api/breed/${name}/images/random`)
        .then(res => res.json())
        .then(function (data) {
            if (data.status === "error") {
                alert("Can't find dog...");
            } else {
                document.querySelector("#dog-image").style.backgroundImage = `url(${data.message})`;
            }
        })
}