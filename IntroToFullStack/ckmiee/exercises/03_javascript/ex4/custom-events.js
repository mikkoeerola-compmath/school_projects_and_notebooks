let rollButton = document.getElementById("roll-button");

rollButton.addEventListener("click", function() {
    rollDice();
});

document.addEventListener("rollDice", function(event) {
    let rollResult = event.detail.value;
    if (rollResult === 1) {
        let count = document.querySelector("#ones > p");
        let oldC = parseInt(count.textContent);
        oldC = oldC? oldC:0;
        count.textContent = (oldC + 1).toString();
    }
})

document.addEventListener("rollDice", function(event) {
    let rollResult = event.detail.value;
    if (rollResult === 2) {
        let count = document.querySelector("#twos > p");
        let oldC = parseInt(count.textContent);
        oldC = oldC? oldC:0;
        count.textContent = (oldC + 1).toString();
    }
})

document.addEventListener("rollDice", function(event) {
    let rollResult = event.detail.value;
    if (rollResult === 3) {
        let count = document.querySelector("#threes > p");
        let oldC = parseInt(count.textContent);
        oldC = oldC? oldC:0;
        count.textContent = (oldC + 1).toString();
    }
})

document.addEventListener("rollDice", function(event) {
    let rollResult = event.detail.value;
    if (rollResult === 4) {
        let count = document.querySelector("#fours > p");
        let oldC = parseInt(count.textContent);
        oldC = oldC? oldC:0;
        count.textContent = (oldC + 1).toString();
    }
})

document.addEventListener("rollDice", function(event) {
    let rollResult = event.detail.value;
    if (rollResult === 5) {
        let count = document.querySelector("#fives > p");
        let oldC = parseInt(count.textContent);
        oldC = oldC? oldC:0;
        count.textContent = (oldC + 1).toString();
    }
})

document.addEventListener("rollDice", function(event) {
    let rollResult = event.detail.value;
    if (rollResult === 6) {
        let count = document.querySelector("#sixes > p");
        let oldC = parseInt(count.textContent);
        oldC = oldC? oldC:0;
        count.textContent = (oldC + 1).toString();
    }
})

document.addEventListener("rollDice", function(event) {
    let rollResult = event.detail.value;
    let count = document.querySelector("#totals span");
    let oldC = parseInt(count.textContent);
    count.textContent = (oldC + 1).toString();
})

document.addEventListener("rollDice", function(event) {
    let rollResult = event.detail.value;
    console.log(rollResult);
    let tempID = "template" + rollResult.toString();
    console.log(tempID);
    const temp = document.getElementById(tempID);
    let tempClone = temp.content.cloneNode(true);
    rollButton.innerHTML = "";
    rollButton.appendChild(tempClone);
})