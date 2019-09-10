var firstName = document.getElementById('fName');
var lastName = document.getElementById('lName');
var email = document.getElementById('emailA');
var heard = document.getElementById('fromWho');

var F = document.getElementById('FirstN');
var L = document.getElementById('LastN');
var E = document.getElementById('Email');
var X = document.getElementById('Heard');

var Main = document.getElementById('mainImage');
var Pono = document.getElementById('ponca');
var Cong = document.getElementById('congo');
var WHouse = document.getElementById('house');
var Lake = document.getElementById('lake');

function changeName(f,l,e,x)
{
    f.innerHTML = firstName.value;
    l.innerHTML = lastName.value;
    e.innerHTML = email.value;
    x.innerHTML = heard.value;
}

function swappableImage(image)
{
    Main.src = image.src
}

document.getElementById('mainImage').addEventListener("click",newImages)
        function newImages()
        {
            Pono.src = ""
            Cong.src = ""
            WHouse.src = ""
            Lake.src = ""
        }
