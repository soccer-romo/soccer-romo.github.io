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

