var myAppName = "indext";
var main = document.getElementById('mainImage');
var image1 = document.getElementById('congress');
var image2 = document.getElementById('ponc');
var image3 = document.getElementById('lake');
var image4 = document.getElementById('whiteHouse');



        function myGreeting(myName = "Nicu")
        {
            //document.write("<h2>Greetings from " + myName + " from " +myAppName +  "</h2>");
            var aString = "<h2>Greetings from " + myName + " from " +myAppName +  "</h2>"
            var name = document.getElementById('fName');
            document.getElementById('greet').innerHTML = aString;
        }

        function imageSwap(image)
        {
            main.src = image
        }

        document.getElementById('mainImage').addEventListener('dblclick',newImages)
        function newImages()
        {
            image1.src = "image/detroit.jpeg"
            image2.src = "image/band.png"
            image3.src = "image/ship.jpeg"
            image4.src = "image/soccer.jpeg"
        }