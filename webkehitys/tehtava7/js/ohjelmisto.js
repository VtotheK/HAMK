$(document).ready(function() { 
    $("#showPopMusicButton").click(function(){
        $("#popmusiccontainer:hidden").show();
        $("#dancemusiccontainer:visible").hide();
    })

    $("#showDanceMusicButton").click(function(){
        $("#dancemusiccontainer:hidden").show();
        $("#popmusiccontainer:visible").hide();
    })
})
