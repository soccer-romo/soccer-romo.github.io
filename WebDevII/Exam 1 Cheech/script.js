//-------------Variable for messages, errors, and form submit bool---------------//
var isValid = true;
//----------------------------//

//--------------Var for dropdown--------------//
var blank = ""
var amount = ["1", "2", "3","4","5","6", "7", "8","9","10"];
var pizza = ["Pepperoni","Cheese","BBQ Chicken","Hawaiian","Deluxe","Margherita"]
var amountString = ""
var myString = ""
//----------------------------//
//--------------Regex--------//
var phoneTest = /\d{3}[-.]\d{3}[-.]\d{4}/;
var emailTest = /[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/;


//-------------DropDown Functions---------------//
amount.forEach(function(el)
{
    amountString += `<option>${el}</option>`;
})

amountPizzas.innerHTML = amountString;

pizza.forEach(function(el)
{
    myString += `<option>${el}</option>`;
})

pizzaType.innerHTML = myString;
//----------------------------//

//--------------Validation for the Form--------------//
function valForm(frm)
{
    isValid = true
    var phoneVal = phoneTest.test(frm.phoneNum.value);
    var emailVal = emailTest.test(frm.email.value);
    console.log(phoneVal)

    if (frm.userName.value == "" | frm.email.value == "" | frm.phoneNum.value == "" | 
    phoneVal == false | emailVal == false)
    {
        
        if(frm.userName.value == ""){
            frm.userName.style.backgroundColor = "lightpink";

        }
        else if (frm.userName.value != "")
        {
            frm.userName.style.backgroundColor = "white"; 
        }

        if(frm.email.value == "" | emailVal == false){
            frm.email.style.backgroundColor = "lightpink";
        }

        else if (frm.email.value != "")
        {
            frm.email.style.backgroundColor = "white";        }

        if(frm.phoneNum.value == "" | phoneVal == false){
            frm.phoneNum.style.backgroundColor = "lightpink";
        }

        else if (frm.phoneNum.value != "")
        {
            frm.phoneNum.style.backgroundColor = "white";
        }
        isValid = false
    }
    else
    {
        frm.userName.style.backgroundColor = "white"; 
        frm.email.style.backgroundColor = "white";  
        frm.phoneNum.style.backgroundColor = "white"; 
    }
}
//----------------------------//

//--------------Brings over to the next page to work with--------------//
function printQuery()
{
    var query = window.location.search.substring(1);
    var valPairs = query.split("&");
    for (var i = 0; i < valPairs.length; i++)
    {
        var pair = valPairs[i].split("=");
        document.write(`${pair[0]}: ${pair[1]}<br>`);
    }
}
//----------------------------//

//--------Submitting User Info---//
//html ids for the input boxes
var userName = document.getElementById('userName');
var phoneNum = document.getElementById('phoneNum');
var email = document.getElementById('email');
var numPizza = document.getElementById('amountPizzas');
var pizzaType = document.getElementById("pizzaType")
//html ids to paste on screen under form box
var U = document.getElementById('user');
var P = document.getElementById('phon');
var E = document.getElementById('emai');
var A = document.getElementById('amoun');
var T = document.getElementById('typ');


//function that pastes from input boxes to <p>
function changeName(u,p,e,a,t)
{
    u.innerHTML = userName.value;
    p.innerHTML = phoneNum.value;
    e.innerHTML = email.value;
    a.innerHTML = numPizza.value;
    t.innerHTML = pizzaType.value;

}