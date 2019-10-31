// var timer = setInterval(runTimer, 300)

// function runTimer()
// {
//     document.getElementById('theTimer').innerHTML = Math.floor(Math.random() * 10);
// }

Math.floor(Math.random() * 10);

function valForm(frm)
{
    var isValid = true;
    if (frm.userName.value == "")
    {
        document.getElementById("err").innerHTML = "Cannot be Blank";
        frm.userName.style.backgroundColor = "lightpink";
        isValid = false
    }

    // if(isValid)
    // {
    //     frm.submit();
    // }

    return isValid;
}

function printQuery()
{
    var query = window.location.search.substring(1);
    var valPairs = query.split("&");
    for (var i = 0; i < valPairs.length; i++)
    {
        var pair = valPairs[i].split("=");
        document.write(`${pair[0]} gets ${pair[1]}<br>`);
    }
}