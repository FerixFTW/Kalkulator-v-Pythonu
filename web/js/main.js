
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
function update(text){
  inputs.value = text;
}

// flags
//var result = 0;

function interpret(input){
  //console.log(input);
  //if(result==1){update(""); result=0;}
  switch(input){
    case "C": update(""); break;
    case "DEL": update((inputs.value).slice(0,-1)); break;
    case "x<sup>2</sup>": append("^2"); break;
    case "log<sub>10</sub>(x)": append("log"); break;
    case "trig.": var trig = prompt("sin cos tan cot",""); append(trig); break;
    case "=": eel.parse_input(inputs.value); result = 1; break;
    default: append(input); eel.logicParse(input); break;
  }
}

eel.expose(post_result);
function post_result(args){
  update(args);
}
