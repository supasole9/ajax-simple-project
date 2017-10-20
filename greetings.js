var button = document.getElementById("button");
var translate = document.getElementById("translate");
var culture = document.getElementById("culture");
var fname = document.getElementById("name");
var answerbox = document.getElementById("answer");

button.onclick = function () {
       var request = new XMLHttpRequest();
       request.onreadystatechange = function () {
         if (request.readyState == XMLHttpRequest.DONE) {
           if (request.status >= 200 && request.status < 400) {
             var dataFromServer = request.responseText;
             var parsedData = JSON.parse(dataFromServer);
             var selectedCulture = culture.options[culture.selectedIndex].value
             var data = parsedData[selectedCulture]
             console.log(fname.value)
             printToScreen(data)


           } else {
             console.log("blah")
           }
         }
       };
       request.open("GET", "http://localhost:8000/" + translate.options[translate.selectedIndex].value);
       request.send()
}

var printToScreen = function (data) {
     answerbox.innerHTML = "";
     var datadiv = document.createElement("div");
     var greet = document.createElement("h2");
     greet.innerHTML = data + " " + fname.value + "!"
     console.log(greet)
     datadiv.appendChild(greet)
     answerbox.appendChild(datadiv)
}
