var currentimage = 0;
var imagepaths = ["img/test.jpg","img/test2.jpg"];

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
