// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array
function addNew(name) {
  roster.push(name);
}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster
function remove(name) {
  nameIndex = roster.indexOf(name);
  roster.splice(nameIndex, 1);
}
// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.
function display() {
  console.log(roster)
}

// Start by asking if they want to use the web app
answer = prompt("Do you want to use the web app (y/n)?")
// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
while (answer == "y") {
  whatFunction = prompt("Which action do you want to perform (add, remove, display, quit)?");
  if (whatFunction == "add") {
    name = prompt("Give a name:")
    addNew(name);
  }
  else if (whatFunction == "remove") {
    name = prompt("What name do you want to remove?");
    remove(name);
  }
  else if (whatFunction == "display") {
    display();
  }
  else if (whatFunction == "quit") {
    break;
  }
}
