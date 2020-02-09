let appRun = true;
let startButton = document.getSelection("#startProgram");
let searchTerm;
let arrayToRemove = [];
let background,  inputBox, searchButton, exitButton, items;
function stopApplication(){
    console.log("Stopping loop");
    appRun = false;
    document.getElementById("startProgram").style.display = "initial";
    for(let x of arrayToRemove)
    {
        console.log(x);
        document.getElementById("main").removeChild(x);
    }
    arrayToRemove = [];
}

function refreshApplication(){
    console.log("Starting loop");
    console.log(inputBox);
    document.getElementById("startProgram").style.display = "none";
    drawApp();
    //Poll For New Item Requests
    setSearchTerm();
    //Add/Delete Items from cart ----> Includes search as a separate "window"

    //Reevaluate Price

    //reevaluate map

    //Draw Changes

}

function drawApp()
{
    document.getElementById("main").style.display = "flex";
    document.getElementById("main").style.flexDirection = "column";
    console.log("Redrawing App");
    background = document.createElement("DIV");
    background.id = "background";
    background.style.backgroundColor = "grey";
    background.style.width = "90vw";
    background.style.height = "150vh"
    background.style.marginTop = "15px";
    background.style.marginLeft = "auto";
    background.style.marginRight = "auto";
    arrayToRemove.push(background);
    document.getElementById("main").append(background);

    inputBox = document.createElement("INPUT");
    inputBox.style.width = "60vw";
    inputBox.style.height= "5vh";
    inputBox.style.marginLeft = "10vw";
    inputBox.style.marginRight = "auto";
    inputBox.style.marginTop = "3vh";
    inputBox.style.innerText = "Search for Items";
    inputBox.id = "input";
    document.getElementById("background").append(inputBox);
    //input.onkeypress = setSearchTerm;

    searchButton = document.createElement("BUTTON");
    searchButton.style.width = "10vw";
    searchButton.style.height = "5vh";
    searchButton.style.marginLeft = "0";
    searchButton.style.marginRight = "auto";
    searchButton.style.marginTop = "3vh";
    searchButton.innerText = "Search";
    searchButton.fontSize = "1.5rem";
    searchButton.onclick = setSearchTerm;
    document.getElementById("background").append(searchButton);

    exitButton = document.createElement("BUTTON");
    exitButton.onclick = stopApplication;
    exitButton.innerHTML = "Exit";
    exitButton.style.width = "150px";
    exitButton.style.height = "90px";
    exitButton.style.marginLeft = "auto";
    exitButton.style.marginRight = "auto";
    arrayToRemove.push(exitButton);
    document.getElementById("main").append(exitButton);
    console.log(arrayToRemove);
}

function drawItems(x, searchTerm) {
    let resultItem, checkbox, name, price, location, image;
    let info = getProductsInfo(searchTerm);
    if(info.length > 0) {
        for (let i = 0; i < x; i++) {
            console.log(info[i]);
            resultItem = document.createElement("DIV");
            checkbox = document.createElement("INPUT");
            name = document.createElement("P");
            price = document.createElement("P");
            location = document.createElement("P");
            checkbox.type = "checkbox";
            arrayToRemove.push(resultItem);

            name.innerText = info[i].name;
            price.innerText = info[i].price;
            location.innerText = info[i].location;
            image = info[i].image;
            resultItem.appendChild(name);
            resultItem.appendChild(price);
            resultItem.appendChild(location);
            resultItem.appendChild(checkbox);
            document.getElementById("background").appendChild(resultItem);
        }
    }
}

function setSearchTerm(){
        searchTerm = inputBox.value;
        drawItems(3, searchTerm);
        let input = document.getElementById('input');
        input.addEventListener(("keyup"), function(e) {
            if(e.key==="Enter"){
                let string = input.value;
                drawItems(3,string);
            }
        });
}