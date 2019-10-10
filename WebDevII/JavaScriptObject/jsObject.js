
//Object literal
// const pen = 
// {
//     type: "ballpoint",
//     color: "blue",
//     brand: "bic"
// };

// // console.log(pen.type);
// // console.log(pen.brand);

// pen.color = "red";

// // console.log(pen.color)

// // console.log(`I write the a ${pen.color} ${pen.brand} ${pen.type} pen`);

// pen.price = 2.50
// console.log(`My pen costs $${pen.price}`);

//----------------------------------------//

const aurora = 
{
    name: "Aurora",
    health: 150,
    strength: 25,
    xp: 0,
    describe()
    {
    return(`${aurora.name} has ${aurora.health} health points, ${aurora.strength} as strength and ${aurora.xp} XP points`);

}   
}

// console.log(`${aurora.name} has ${aurora.health} health points and ${aurora.strength} as strength`);
// Aurora is harmed by an arrow - reduced health by 20
aurora.health -= 20;

// console.log(`${aurora.name} has ${aurora.health} health points remaining`);

// Aurora equips a strenght necklace - icrease strength by 10
aurora.strength += 10;
// console.log(`${aurora.name} has ${aurora.strength} strength`);
aurora.xp += 15;

// describe(aurora);


console.log(aurora.describe());

// const boris =
// {
//     name: "Boris",
//     health: 100,
//     strength: 150,
//     describe(newName) {
//         // console.log(`My name is ${this.name}!`)
//         this.name = newName;
//         return `My name is ${this.name}!`;
//     }
// }

// console.log(boris.describe("John"));

//-------------dog object -------//
const dog =
{
    name: "Fang",
    species: "boarhound",
    size: 75,
    describe(){
        console.log(`${dog.name} is a ${dog.species} dog measuring ${dog.size}`);
        console.log(`Look, a cat! ${dog.name} barks: ${dog.bark()}`);
    },
    bark()
    {
        return ("Grrr! Grrr!")
    }
}
dog.describe();

//-------------dog object -------//

//-------------Bank Account object -------//
const account = {
    name: "Alex",
    balance: 0,
    credit(balance)
    {
        this.balance += balance
        return this.balance
    },
    describe(credit)
    {
        console.log(`Owner: ${this.name}, balance: ${this.balance}`);
    }
}

account.credit(-80)
account.describe()
account.credit(250)
account.describe()