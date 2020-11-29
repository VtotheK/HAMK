function poptables(){
    var maindiv = document.createElement("div");
    maindiv.id = "popmusiccontainer"
    document.body.appendChild(maindiv);
    maindiv.className = "row col-12 showcontainer";
    for(i = 1; i < Object.keys(popsets).length + 1; i++)
    {
        let tbl = document.createElement("table");
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
        header.innerHTML="Setti " + i;
        row.appendChild(header);
        let row2 = document.createElement("tr");
        let head1 = document.createElement("th");
        let head2 = document.createElement("th");
        header.innerHTML="Kappale";
        row2.appendChild(head1).appendChild(head2);
        tbl.appendChild(row2)
        for(j = 1; j<Object.keys(popsets).length + 1; j++){
            let newrow = document.createElement("tr");
            let data = popsets["Setti " + j];
            for(k = 0; k<data.length;k++)
            {
                let tbldata1 = document.createElement("td");
                tbldata1.innerHTML = j;
                let tbldata2 = document.createElement("td");
                tbldata2.innerHTML = data[k];
                newrow.appendChild(tbldata1);
                newrow.appendChild(tbldata2);
                tbl.appendChild(newrow)
            }
        }
        maindiv.appendChild(tbl);
    }
}

function populatetables(){
    poptables();
}

$(document).ready(function() { 

    populatetables();

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
