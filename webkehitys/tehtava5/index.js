window.onload = function(){
    var cont = document.getElementById("innercontainer");
    var logo = document.getElementById("logo");
    var y = (screen.height/100) * 70;
    var x = (screen.width/100) * 80;

    cont.style.height= y + "px"
    cont.style.width= x + "px"
    logo.style.left = (screen.width / 2) - 150 + "px"
    logo.style.top =  10 + "px"
}
