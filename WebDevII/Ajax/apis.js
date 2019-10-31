var obj = {
    movie: "Hawaii 5-0",
    budget: 63000000,
    genres: {
        id:18,
        name: "Drama"
    }
}

//convert javascrip Object to Json
var jsonString = JSON.stringify(obj);

//convert json to a javascript object

var backToObject = JSON.parse(jsonString);
console.log(backToObject)

window.addEventListener('load',initializaPage)

function initializaPage()
{
    document.getElementById('movieTitle').innerHTML = backToObject.movie;
    document.getElementById('desc').innerHTML = backToObject.genres.name;

}