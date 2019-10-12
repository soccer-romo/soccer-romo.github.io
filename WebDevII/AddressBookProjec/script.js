contacts = document.getElementById('contacts')

function AddressBook(firstN,lastN,phoneNum,email,src)
{
    
    this.firstN = firstN;
    this.lastN = lastN;
    this.phoneNum = phoneNum;
    this.email = email;
    this.imgSrc = src;
    this.DisplayInfo = function()
    {
        return `Name: ${this.firstN} ${this.lastN}\n
        Phone: ${this.phoneNum}
        Email: ${this.email}`
    }
    this.DisplayName = function()
    {
        return `${this.firstN} ${this.lastN}\n`
    }
}

const contact1 = new AddressBook("David","Niculcea","417-379-5743","davsocc@gmail.com","images/david.")
const contact2 = new AddressBook("Marius","Lupescu","417-861-4650","marius@yahoo.com","images/marius.")
const contact3 = new AddressBook("Ruben","Niculcea","441-234-7643","Ruben@gmail.com","images/ruben.")
const contact4 = new AddressBook("Jessica", "Niculcea", "574-285-4957","jess@AOL.net","images/jessica.")

contactAry = [contact1,contact2,contact3,contact4];

var contactList = "";
for(var i = 0; i < contactAry.length; i ++)
{
    contactList += `<li id = ${i}> ${contactAry[i].DisplayName()} </li>`
}
contacts.innerHTML = contactList;

document.getElementById("contacts").addEventListener('click',function(e)
{
    document.getElementById('contactInfo').innerHTML = contactAry[e.target.id].DisplayInfo();
})