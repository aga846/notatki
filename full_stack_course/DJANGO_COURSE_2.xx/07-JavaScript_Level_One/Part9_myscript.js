
var first = prompt("What is your first name?")
var last = prompt("What is your last name?")
var age = prompt("What is your age?")
var tall = prompt("How tall are you (in cm)?")
var pet = prompt("What is your pet's name?")
alert("Thank you for the information")

if ((first[0] === last[0]) && (age > 20 && age < 30) && (tall >= 170) && (pet[pet.length-1]) === "y") {
  console.log("Hello spy, you passed the test!");
}
else{
  console.log("Nothing to see here.");
}
