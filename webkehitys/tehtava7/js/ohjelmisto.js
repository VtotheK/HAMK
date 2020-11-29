$(document).ready(function() { 
    $("#showPopMusicButton").click(function(){
        $("#dancemusiccontainer:visible").hide();
        $("#backgroundmusiccontainer:visible").hide();
        $("#popmusiccontainer:hidden").show();
    })

    $("#showDanceMusicButton").click(function(){
        $("#popmusiccontainer:visible").hide();
        $("#backgroundmusiccontainer:visible").hide();
        $("#dancemusiccontainer:hidden").show();
    })
    $("#showBackgroundMusicButton").click(function(){
        $("#dancemusiccontainer:visible").hide();
        $("#popmusiccontainer:visible").hide();
        $("#backgroundmusiccontainer:hidden").show();
    })
})
