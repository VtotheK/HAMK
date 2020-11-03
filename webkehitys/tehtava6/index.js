include('facts.js')

function RandomFact(){
    var rand = Math.floor(Math.random()*facts.length);
	var txt = document.getElementById("factparagraph");
	txt.innerHTML= facts[rand];
}




