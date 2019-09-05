function displayGreeting(name)
{

    document.getElementById('greeting').innerHTML = "Hi " + name + ". Welcome to earth"
}

document.getElementById('clippy').addEventListener('click', doSomthing)
function doSomthing()
{
    alert("I did something");
}

//anonymous function 
document.getElementById('newAnon').addEventListener('dblclick', function ()
{
    alert("I got doubleclicked!");
});

function theobj(anObject){
    alert(anObject.innerHTML);
}