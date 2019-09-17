//Callbacks ************
// any function that uses a fumction as an argument

function greeting(greet)
{
    console.log(greet);
}

function createGreeting(fname , functionName)
{
    var myGreeting = "Hello " + fname;
    //greeting(myGreeting);
    //var functionName = greeting;
    functionName(myGreeting);
}

//greeting(" David ")

createGreeting("WazUP" , greeting)

/************************* */
//*************** Timers **************//
var myTimer = setInterval(aFunction, 3000)

function aFunction()
{
    alert("working");

}

//click event that will stop the timer

document.getElementById('stop').addEventListener('click', function(){
    clearInterval(myTimer)
})

//*************************************/

//*****************Arrays**************/

var myDiv = document.getElementById('ary');

var movies = ["Lilo and Stitch", "Pearl Harbor", "Jurassic Park"];

// store different types of elements shows that it's possible
//var elements = ["Hello",7,{message: "Hi Mom"}, true]


myString = "<select id='movie'>";

//using for loop
//for (var i = 0; i < movies.length; i++)
//{
//    myString += "<option>" + movies[i] + "</option>";
//}

movies.forEach(function(el)
{
    //myString += "<option>" + el + "</option>";
    myString += `<option>${el}</option>`;
})

myString += "</select>"

myDiv.innerHTML = myString;

document.getElementById('getIt').addEventListener('click',function(){
    alert(document.getElementById('movie').value);
})


//Manipulation An Array----//
// add to an array

movies.push("Jumangi");
console.log(movies);

//get the last element in the array
var last = movies.length -1;
console.log(movies[last]);

//add an element to the beginning unshift
movies.unshift("50 first dates");
//console.log(movies);

//remove an element from the end
var aVar = movies.pop();
console.log(`${aVar}: ${movies}`)

movies.splice(1,2)
console.log(movies)