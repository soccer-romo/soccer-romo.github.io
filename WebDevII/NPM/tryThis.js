const chalk = require('chalk');
 
console.log(chalk.blue('Hello world!'));

var moment = require('moment');
moment().format();

var future = moment().add(5,"y");
future = moment(future).format("MM-DD-YY")
console.log(future)

var x = moment("12-25-1995", "MM-DD-YYYY");
console.log(x);

var format1 = moment(x).format('YY Do MMM');
console.log(format1)

format2 = moment(x).format("YYYY DD MMM");
console.log(format2)

const readline = require('readline').createInterface({
    input:process.stdin,
    output: process.stdout
})

readline.question("What is your name? ", (date) => 
{
    console.log(chalk.blue("Hello " + date));
    date= moment(date)
    readline.close();
});