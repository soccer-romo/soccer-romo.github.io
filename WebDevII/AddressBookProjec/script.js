//  Developer: David Niculcea
//  Date:10/12/19
//  Project: Address Book
//  Puropse: Create Address book using Objects
//Variables needed for the script to make my life easier
contacts = document.getElementById('contacts')
var NameP = document.getElementById('NameP')
var PhoneP = document.getElementById('PhoneP');
var EmailP = document.getElementById("EmailP");
var ContactImg = document.getElementById("contactImg")
var firstInputName = document.getElementById('fName')
var lastInputName = document.getElementById('lName')
var phoneInput = document.getElementById('phoneNum')
var emailInput = document.getElementById('email')

//This function recieves an object info and uses it
function AddressBook(firstN,lastN,phoneNum,email,src)
{
    
    this.firstN = firstN;
    this.lastN = lastN;
    this.phoneNum = phoneNum;
    this.email = email;
    this.imgSrc = src;
    //This displays all the contact information
    this.DisplayInfo = function()
    {
        NameP.innerHTML = "Name: " + this.firstN + " " + this.lastN;
        PhoneP.innerHTML = "Phone: " + this.phoneNum;
        EmailP.innerHTML = "Email: " + this.email
        ContactImg.src = this.imgSrc;
    }
    //This displays only the first and last name of the contact info
    this.DisplayName = function()
    {
        return `${this.firstN} ${this.lastN}`
    }
}
//objects that are hardcoded
const contact1 = new AddressBook("David","Niculcea","417-379-5743","davsocc@gmail.com","images/david.jpg")
const contact2 = new AddressBook("Marius","Lupescu","417-918-2837","marius@yahoo.com","images/marius.jpg")
const contact3 = new AddressBook("Ruben","Niculcea","441-234-7643","Ruben@gmail.com","images/ruben.jpg")
const contact4 = new AddressBook("Jessica", "Niculcea", "574-285-4957","jess@AOL.net","images/jessica.jpg")

//The array with all the objects
contactAry = [contact1,contact2,contact3,contact4];

//this displays the names of the contacts in the array
function display(){
//this variable is important because it resets the contacts displayed
var contactList = "";
for(var i = 0; i < contactAry.length; i ++)
{
    //From the reset it rewrites all the contacts again here
    contactList += `<p id = ${i}> ${contactAry[i].DisplayName()} </p>`
}
contacts.innerHTML = contactList;
}

//used to show hardcoded contacts
display()

//this is used to show the information of a specific contact
document.getElementById("contacts").addEventListener('click',function(e)
{
    contactAry[e.target.id].DisplayInfo();
})

//this adds a contact into the array after the form has been filled
function addContact()
{
    
    const contactUp = new AddressBook(firstInputName.value,lastInputName.value,phoneInput.value,emailInput.value,"images/generic.jpg")
    contactAry.push(contactUp)
    display()
}


// new line for testing datafields

//used to make sure that the information in data fields are valid
var isValid = true;

//--------------Regex--------//
var phoneTest = /\d{3}[-.]\d{3}[-.]\d{4}/;
var emailTest = /[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/;

//--------------Validation for the Form--------------//
function valForm(frm)
{
    isValid = true

    //test phone and email data against regex and returns boolean
    var phoneVal = phoneTest.test(phoneInput.value);
    var emailVal = emailTest.test(emailInput.value);

    //tests all available inputs
    if (firstInputName.value == "" | lastInputName.value | emailInput.value == "" | phoneInput.value == "" | 
    phoneVal == false | emailVal == false)
    {
        
        if(firstInputName.value == ""){
            firstInputName.style.backgroundColor = "lightpink";
        }
        else if (firstInputName.value != "")
        {
            firstInputName.style.backgroundColor = "white"; 
        }
        if(lastInputName.value == ""){
            lastInputName.style.backgroundColor = "lightpink";
        }
        else if (lastInputName.value != "")
        {
            lastInputName.style.backgroundColor = "white"; 
        }

        if(emailInput.value == "" | emailVal == false){
            emailInput.style.backgroundColor = "lightpink";
        }

        else if (emailInput.value != "")
        {
            emailInput.style.backgroundColor = "white";
        }

        if(phoneInput.value == "" | phoneVal == false){
            phoneInput.style.backgroundColor = "lightpink";
        }

        else if (phoneInput.value != "")
        {
            phoneInput.style.backgroundColor = "white";
        }
        isValid = false
    }
    //if all is correct it allows it to add contact here
    if(isValid == true)
    {
        addContact();
    }
}