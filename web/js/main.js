// document.getElementById("button-name").addEventListener("click", ()=>{eel.get_random_name()}, false);
// document.getElementById("button-number").addEventListener("click", ()=>{eel.get_random_number()}, false);
// document.getElementById("button-date").addEventListener("click", ()=>{eel.get_date()}, false);
// document.getElementById("button-ip").addEventListener("click", ()=>{eel.get_ip()}, false);
//
// eel.expose(prompt_alerts);
// function prompt_alerts(description) {
//   alert(description);
// }

var buttons = document.querySelectorAll(".button").length;
var inputs = document.getElementById("inputs");

for (var i = 0; i < buttons ; i++) {
    document.querySelectorAll(".button")[i].addEventListener("click", function() {
        interpret(this.innerHTML);
    });
}

function append(text){
  inputs.value = inputs.value + text;
}

function interpret(input){
  console.log(input);

  switch(input){
    case "C": inputs.value = ""; break;
    case "DEL": inputs.value = (inputs.value).slice(0,-1); break;
    case "x<sup>2</sup>": append("^2"); break;
    case "trig.": var trig = prompt("sin cos tan cotan",""); append(trig); break;
    case "=": eel.parseInput(inputs.value); break;
    default: append(input); break;
  }
}
