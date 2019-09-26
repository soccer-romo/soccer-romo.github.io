var newStr = "My name is Stitch - Rambo was tough to watch";
// console.log(newStr.length);
// console.log(newStr.charAt(5));

for(var i = 0; i < newStr.length; i++)
{
    //console.log(newStr.charAt(i));
}

///----------------------Cases---//

//-----Validation----//
var phoneNumber = "417-123-4567";
var regex = /\d{3}[-.]\d{3}[-.]\d{4}/;
var isValid = regex.test(phoneNumber)
console.log(isValid)

//----Extraction---//
var address = "1001 N Chestnut Expressway, Springfield, MO 65872";
var nameTest = address.match(/[A-Z]+\s\d{5}$/g);
console.log(nameTest)

//----Replace----//

//----Replace---//
// g = global/all i = insensitive

var name = "Kirsten does JavaScript, and the class as well"
var replaceIt = name.replace(/Kirsten/gi, "David");
console.log(replaceIt)