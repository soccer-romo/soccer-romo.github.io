//-------------Variable for messages, errors, and form submit bool---------------//
var isValid = true;
var error1 = document.getElementById("error1");
var error2 = document.getElementById("error2");
var error3 = document.getElementById("error3");
var message1 = "Username cannot be blank"
var message2 = "Email needs an '@' and '.com'"
var message3 = "Phone Number has {0} digets, needs 10 digets"
//----------------------------//

//--------------Var for dropdown--------------//
var bestContact = document.getElementById("bestContact")
var blank = ""
var contact = ["Email", "Phone", "Social Media","Fax"];
var myString = ""
//----------------------------//
//--------------Regex--------//
var phoneTest = /\d{3}[-.]\d{3}[-.]\d{4}/;
var emailTest = /[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/;


//-------------DropDown Function---------------//
contact.forEach(function(el)
{
    myString += `<option>${el}</option>`;
})

bestContact.innerHTML = myString;
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
            error1.innerHTML = message1;
        }
        else if (frm.userName.value != "")
        {
            frm.userName.style.backgroundColor = "white"; 
            error1.innerHTML = blank; 
        }

        if(frm.email.value == "" | emailVal == false){
            frm.email.style.backgroundColor = "lightpink";
            error2.innerHTML = message2;
        }

        else if (frm.email.value != "")
        {
            frm.email.style.backgroundColor = "white";
            error2.innerHTML = blank; 
        }

        if(frm.phoneNum.value == "" | phoneVal == false){
            frm.phoneNum.style.backgroundColor = "lightpink";
        }

        else if (frm.phoneNum.value != "")
        {
            frm.phoneNum.style.backgroundColor = "white";
        }
        isValid = false
    }
    if(isValid == true)
    {
        frm.submit();
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