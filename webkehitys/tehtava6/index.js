window.onload = function(){
    randomFact();
}

var currentimage = 0;
var imagepaths = ["img/Kuva1.jpg","img/Kuva2.jpg","img/Kuva3.jpg","img/Kuva4.jpg","img/Kuva5.jpg","img/Kuva6.jpg","img/Kuva7.jpg","img/Kuva8.jpg"];
var curfact = 0;


function randomFact(){
    var len = facts.length;
    var rndfact = curfact;
    while(rndfact == curfact){
        rndfact = Math.floor(Math.random() * len);
    }
    document.getElementById("randomtext").innerHTML = facts[rndfact]
    curfact = rndfact;
}

function nextimg(){
    var imgs = document.getElementById("slideshow");
    if(++currentimage >= imagepaths.length){
        currentimage = 0;
    }
    imgs.src = imagepaths[currentimage];
}

function previousimg(){
    var imgs = document.getElementById("slideshow");
    if(--currentimage < 0){
        currentimage = imagepaths.length - 1; 
    }
    imgs.src = imagepaths[currentimage];
}
