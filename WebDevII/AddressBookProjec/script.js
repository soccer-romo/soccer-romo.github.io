

function AddressBook(firstN,lastN,phoneNum,email,src)
{
    var contactImg = document.getElementById('contactImg')
    var contactFirstName = document.getElementById('FirstP')
    var contactLastName = document.getElementById('LastP')
    var contactEmail = document.getElementById('EmailP')
    var contactPhone = document.getElementById('PhoneP')
    this.firstN = firstN;
    this.lastN = lastN;
    this.phoneNum = phoneNum;
    this.email = email;
    this.imgSrc = src
    this.DisplayInfo = function()
    {
        contactImg.src = this.imgSrc;
        contactFirstName.innerHTML = this.firstN;
        contactLastName.innerHTML = this.lastN;
        contactEmail.innerHTML = this.email;
        contactPhone.innerHTML = this.phoneNum;
    }
    this.DisplayName = function()
    {
        return `${this.firstN} ${this.lastN}`
    }
}

const contact1 = new AddressBook("David","Niculcea","417-379-5743","davsocc@gmail.com","images/")
contact1.DisplayInfo()