let appRun = true;
let startButton = document.getSelection("#startProgram");
console.log(startButton);

const exitButton = document.createElement("BUTTON");
exitButton.onclick = stopApplication;
exitButton.innerHTML = "Exit";
exitButton.width = 1;
exitButton.height = 1;
document.body.append(exitButton);
console.log("Set up buttons");

function stopApplication(){
    console.log("Stopping loop");
    appRun = false;
}

function runApplication(){
    //While user still desires to shop keep looping

    startButton.backgroundColor = "blue";
    while(appRun){
        //Poll For New Item Requests
    console.log("Starting loop");
        //Add/Delete Items from cart
        //Reevaluate Price

        //reevaluate map
    }
}