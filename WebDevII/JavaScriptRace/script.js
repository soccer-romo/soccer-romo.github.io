var ben10Img = document.getElementById('ben10Image');
var einstieinImage = document.getElementById('einstieinImage')
var stoplight = document.getElementById('stoplight')


var pxNum1 = 160;
var pxNum2 = 160;
var startR = document.getElementById('startRace')
var winner = document.getElementById('winner');
var timer;

startR.addEventListener('click',startRace)
ben10Img.addEventListener('click',racingPosition)
einstieinImage.addEventListener('click',racingPosition)

startingPosition()
//this places them on top before they're clicked so that they appear ready for a race
function startingPosition()
{
    ben10Img.style.left = 500 + "px"
    ben10Img.style.top = 30 + "px"
    einstieinImage.style.left = 430 + "px"
    einstieinImage.style.top = 30 + "px"
}
//This gets them set at the start line
function racingPosition()
{
    ben10Img.style.top = 100 + "px"
    ben10Img.style.left = 160 + "px"
    ben10Img.src = "images/ben10.2.jpg"

    einstieinImage.style.top = 170 + "px"
    einstieinImage.src = "images/rocketship.jpg"
    einstieinImage.style.left = 160 + "px"

    winner.innerHTML = ""
}
//this starts the timer and sets the race
function startRace()
{
    timer = setInterval(timedRace,50);
    stoplight.src = "images/greenlight.png"
    winner.innerHTML = ""
}

//this allows the pictures to move across the computer randomly
function timedRace()
{
    racingPosition()
    var random1 = Math.ceil((Math.random()*10));
    pxNum1 += random1;
    ben10Img.style.left =  pxNum1 + "px";

    var random2 = Math.ceil((Math.random()*10));
    pxNum2 += random2;
    einstieinImage.style.left =  pxNum2 + "px";
    
    if(pxNum1 > 1000 & pxNum2 > 1000)
    {
        clearInterval(timer)
        winner.innerHTML = "They Tied!";
        pxNum1 = 160;
        pxNum2 = 160;
        stoplight.src = "images/redlight.png"

    }

    else if(pxNum1 > 1000)
    {
        clearInterval(timer)
        ben10Img.src = "images/ben10.png"
        stoplight.src = "images/redlight.png"
        winner.innerHTML = 'Ben Won!';
        pxNum1 = 160;
        pxNum2 = 160;
        ben10Img.style.left = 500 + "px"
        ben10Img.style.top = 30 + "px"
    }
    
    else if(pxNum2 >1000)
    {
        pxNum2 = 100
        clearInterval(timer)
        einstieinImage.src = "images/einstein1.png"
        stoplight.src = "images/redlight.png"
        winner.innerHTML = 'Einstein Won!'
        pxNum1 = 160;
        pxNum2 = 160;
        einstieinImage.style.left = 430 + "px"
        einstieinImage.style.top = 30 + "px"
    }
}



