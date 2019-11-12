function order(item,qty,price)
{
    this.orderItem = item;
    this.orderQty = qty;
    this.orderPrice = price;
    this.displayOrder = function()
    {
        return "Item: " + this.orderItem + "\nQty: " + this.orderQty + "\nPrice: " + this.orderPrice
    }

}

const order1 = new order("hungry",2,1);
// console.log(order1.displayOrder())

const order2 = new order("thirsty", 3,4);

// console.log(order1.displayOrder())
// console.log(order2.displayOrder())

var aryOrders = [order1,order2]

for (var i = 0; i < aryOrders.length; i++)
{
    // console.log(aryOrders[i].displayOrder())

}


document.querySelector('h4').addEventListener('click',function()
    {
        var myList = "";

        for (var i = 0; i < aryOrders.length; i++)
        {
            myList += `<li id = ${i}> ${aryOrders[i].orderItem}</li>`;
        }
        document.getElementById('orders').innerHTML = myList;
    }
)

document.getElementById("orders").addEventListener('click',function(e)
{
    alert(e.target.id)
    document.querySelector('h3').innerHTML = aryOrders[e.target.id].displayOrder();
})







// Week 7
const dog =
{
    name: "Lilo",
    breed:"Golden Retriver",
    speak(sound)
    {
        return "I like to " + sound;
    },
    setDate(birthday)
    {
        this.birthdate = new Date(birthday);
    }

}

// console.log(dog.speak("woof woof"));

// var d = new Date();
// console.log(d);
// d = new Date("2018-05-01");
// console.log(d)

// aryMon = ['Jan','Feb','M','A','may','june','july','aug','sep','oct','nov','dec']

// console.log(dog.birthdate);
// // console.log(aryMon[dog.birthdate.getMonth()]);
// dog.setDate("2018-01-17");
// console.log(dog.birthdate);

//--------constructor function-----//

function order(item,qty,price,purchaseDate)
{
    this.orderItem = item;
    this.orderQty = qty;
    this.orderPrice = price;
    this.orderDate = new Date(purchaseDate);
    this.displayOrder = function()
    {
        var subTotal = this.orderQty * this.orderPrice;
        return `${this.orderItem}\nTotal is ${subTotal}\n`;
    }
    this.updateQuantity = function(qty){
        this.orderQty = qty;
    }
}

const order1 = new order("DVD", 1, 10.99, Date.now());
// console.log(order1);

for(items in order1){

    // console.log(items);
    // console.log(order1[items])
}

console.log(order1.displayOrder());
order1.updateQuantity(4);
console.log(order1.displayOrder());

const order2 = new order("Vinyl Record", 5, 29.99,Date.now());
console.log(order2.displayOrder())
order2.updateQuantity(1);
console.log(order2.displayOrder());

order3 = new order(dog,1,100,Date.now())
console.log(order3);
console.log(order3.orderItem.name)
console.log("")


//--------In-Class Lab------//

const sword = {
    strength: 15,
    item: "Sword"
}

function Character(name,strength,item)
{
    this.name = name;
    this.strength = strength;
    this.item = item;
    this.collectItems = function(newItem)
    {
        this.strength = newItem.strength
        this.item = newItem.item
    }
    this.displayCharacter = function()
    {
        return `Name: ${this.name}\nStrength: ${this.strength}\nItem: ${this.item}\n`
    }
}

charDavid = new Character("David", 0, "")
console.log(charDavid.displayCharacter());
charDavid.collectItems(sword)
console.log(charDavid.displayCharacter());

charWolly = new Character("Wolly", 5, "Poppin")
console.log(charWolly.displayCharacter())