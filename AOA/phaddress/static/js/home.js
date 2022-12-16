
function searchcontact(){

    var input,table,tr,td,filter,i,txtdata;
    input=document.getElementById("searchtxt");
    filter=input.value.toUpperCase();
    table=document.getElementById("table");
    tr=document.getElementsByTagName("tr");

    for(i=0; i<tr.length;i++)
    {
      td=tr[i].getElementsByTagName("td")[0];
      if(td)
      {
        txtdata=td.innerText;
        if(txtdata.toUpperCase().indexOf(filter)>-1)
        {
          tr[i].style.display="";
        }
        else
        {
          tr[i].style.display="None";
        }

      }
    }

  }
