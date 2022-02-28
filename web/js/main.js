//// Numpad functionality
//Vars
var buttons = document.querySelectorAll(".button").length;
var inputs = document.getElementById("inputs");
//Button functionality
for (var i = 0; i < buttons ; i++) {
    document.querySelectorAll(".button")[i].addEventListener("click", function() {
        interpret(this.innerHTML);
    });
}

//// Append values to input line
function append(text){
  inputs.value = inputs.value + text;
}

//// Update input line
function update(text){
  inputs.value = text;
}

//// Interpret
function interpret(input){
  //console.log(input);
  //if(result==1){update(""); result=0;}
  switch(input){
    case "C": update(""); break;
    case "DEL": update((inputs.value).slice(0,-1)); break;
    case "x<sup>2</sup>": append("^2"); break;
    case "log<sub>10</sub>(x)": append("log"); break;
    case "trig.": var trig = prompt("sin cos tan cot",""); append(trig); break;
    case "=": eel.parse_input(inputs.value,ans); result = 1; break;
    default: append(input); break;
  }
}

//// Post result
eel.expose(post_result);
function post_result(args){
  update(args);
}

//// History
//Vars
var expressions = document.querySelectorAll(".expression");
var results = document.querySelectorAll(".result");
var ans = 0;
//Function
eel.expose(append_history);
function append_history(expression,result){
  for(let i=5;i>0;i--){
    expressions[i].innerHTML = expressions[i-1].innerHTML;
    results[i].innerHTML = results[i-1].innerHTML;
  }
  expressions[0].innerHTML = expression;
  results[0].innerHTML = result;
  ans = result;
}
