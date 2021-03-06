function populatetables(id,set){
    var maindiv = document.createElement("div");
    maindiv.id = id
    document.body.appendChild(maindiv);
    maindiv.className = "row col-12 showcontainer";
    for(i = 1; i < Object.keys(set).length + 1; i++)
    {
        let cont = document.createElement("div");
        cont.className="con col-md-12 col-sm-12 col-lg-6 col-xl-4";
        let tbl = document.createElement("table");
        tbl.style.boxShadow ="5px 10px 20px black";
        tbl.className = "showtable col-12";
        let col1 = document.createElement("col");
        let col2 = document.createElement("col");
        col1.style.width = "5%";
        col2.style.width = "95%";
        tbl.appendChild(col1);
        tbl.appendChild(col2);
        let row = document.createElement("tr");
        let header = document.createElement("th");
        tbl.appendChild(row);
        header.colSpan="2";
        header.className="tabledesc";
        row.appendChild(header);
        let row2 = document.createElement("tr");
        let head1 = document.createElement("th");
        let head2 = document.createElement("th");
        header.innerHTML="Setti " + i;
        row2.appendChild(head1).appendChild(head2);
        tbl.appendChild(row2)
        let data = set["Setti " + i];
        for(k = 0; k<data.length;k++)
        {
            let r = document.createElement("tr");
            let tbldata1 = document.createElement("td");
            tbldata1.className="songnumbers";
            tbldata1.innerHTML = '&nbsp'+'&nbsp'+(k+1).toString();
            let tbldata2 = document.createElement("td");
            tbldata2.innerHTML = '&nbsp'+'&nbsp'+data[k].toString();
            r.appendChild(tbldata1);
            r.appendChild(tbldata2);
            tbl.appendChild(r)
        }
        cont.appendChild(tbl);
        maindiv.appendChild(cont);
    }
}

function deactivatebuttons(lbl1, lbl2){
    var lbl1 = document.getElementById(lbl1);
    var lbl2 = document.getElementById(lbl2);
    lbl1.style.fontSize = "1rem";
    lbl2.style.fontSize = "1rem";
    lbl1.style.color = "black";
    lbl2.style.color = "black";
}

function activatebutton(label){
    document.getElementById(label).style.fontSize = "1.2rem";
    document.getElementById(label).style.color = "rgb(212, 206, 32)";
}

function showset(arg){
    switch(arg){
        case "popmusic":
            deactivatebuttons("showDanceMusicButton","showBackgroundMusicButton");
            activatebutton("showPopMusicButton");
            break;
        case "dancemusic":
            deactivatebuttons("showPopMusicButton","showBackgroundMusicButton");
            activatebutton("showDanceMusicButton");
            break;
        case "backgroundmusic":
            deactivatebuttons("showPopMusicButton","showDanceMusicButton");
            activatebutton("showBackgroundMusicButton");
            break;
        default:
            console.log("Can't show musicset");
    }
}

$(document).ready(function() { 

    populatetables("popmusiccontainer",popset);
    populatetables("dancemusiccontainer",danceset);
    populatetables("backgroundmusiccontainer",backgroundset);

    $("#showPopMusicButton").click(function(){
        $("#dancemusiccontainer:visible").hide();
        $("#backgroundmusiccontainer:visible").hide();
        $("#popmusiccontainer").show();
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
