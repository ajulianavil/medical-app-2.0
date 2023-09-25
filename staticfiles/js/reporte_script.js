var initialObsValue
var initialFirstName
var initialSecondName
var initialLastName
var initialSecondLastName
var initialLmp
var initialGestations
var Initialmotive


document.addEventListener('DOMContentLoaded', function() {
    // Store the initial value of the textarea when enabling report fields
    initialObsValue = document.getElementById("obs").value
    initialFirstName = document.getElementById("name-uno").value
    initialSecondName = document.getElementById("name-dos").value
    initialLastName = document.getElementById("last-uno").value
    initialSecondLastName = document.getElementById("last-dos").value
    initialLmp = document.getElementById("lmp").value
    initialGestations = document.getElementById("gest").value
    Initialmotive = document.getElementById("motivo").value

    const textarea = document.getElementById('obs');
    textarea.addEventListener('input', function() {
        console.log("aaaaaaaaaa")
        if (this.value.length > 999) {
          this.value = this.value.slice(0, 999); // Truncate the text to 1000 characters
        }
      });
});



function enableFields(){
    var fullAnalysisButton = document.getElementById('full_analysis');

    var form = document.getElementById('report-form');
    var fields = form.getElementsByTagName('input');

    for (var i = 0; i < fields.length; i++) {
        if (fields[i].name === "cedula" || fields[i].name === "emb" || fields[i].name === "gest" || fields[i].name === "lmp") {
            continue;
        }
    fields[i].disabled = false;
    }

    document.getElementById('editButton').style.display = 'none';
    document.getElementById('sendButton').style.display = 'block';
    document.getElementById('cancelInfo').style.display = 'block';

    document.getElementById('download_button').disabled = true;
    document.getElementById('full_analysis').disabled = true;
    document.getElementById('editReport').disabled = true;

    fullAnalysisButton.classList.add('hiding');
} 

function saveFields(){
    var fullAnalysisButton = document.getElementById('full_analysis');

    document.getElementById('editButton').style.display = 'block'; 
    document.getElementById('sendButton').style.display = 'none';

    document.getElementById('download_button').disabled = false;
    document.getElementById('full_analysis').disabled = false;
    document.getElementById('editReport').disabled = false;

    fullAnalysisButton.classList.remove('hiding');   
}

function onCancelInfo(){
    var fullAnalysisButton = document.getElementById('full_analysis');

    var form = document.getElementById('report-form');
    var fields = form.getElementsByTagName('input');

    document.getElementById("name-uno").value =initialFirstName 
    document.getElementById("name-dos").value  =initialSecondName 
    document.getElementById("last-uno").value = initialLastName 
    document.getElementById("last-dos").value =initialSecondLastName
    document.getElementById("lmp").value =initialLmp
    document.getElementById("gest").value =initialGestations 
    document.getElementById("motivo").value =Initialmotive

    for (var i = 0; i < fields.length; i++) {
        if (fields[i].name === "cedula") {
            continue;
        }
      fields[i].disabled = true;
    }
    
    document.getElementById('editButton').style.display = 'block'; 
    document.getElementById('sendButton').style.display = 'none';
    document.getElementById('cancelInfo').style.display = 'none';

    document.getElementById('download_button').disabled = false;
    document.getElementById('full_analysis').disabled = false;
    document.getElementById('editReport').disabled = false;

    fullAnalysisButton.classList.remove('hiding');   
}
  
function enableReportFields(){
    var fullAnalysisButton = document.getElementById('full_analysis');
    document.getElementById("obs").disabled = false;
    document.getElementById("obs").focus();

    document.getElementById('editReport').style.display = 'none';
    document.getElementById('editButton').disabled = true; 

    document.getElementById('saveReport').style.display = 'block';
    document.getElementById('cancelReport').style.display = 'block';

    document.getElementById('download_button').disabled = true;
    // document.getElementById('full_analysis').disabled = true;
    fullAnalysisButton.classList.add('hiding');
}
  
function saveReport(){
    var fullAnalysisButton = document.getElementById('full_analysis');

    document.getElementById('editReport').style.display = 'block';
    document.getElementById('saveReport').style.display = 'none';
    document.getElementById('cancelReport').style.display = 'none';

    document.getElementById('editButton').disabled = false; 
    document.getElementById('download_button').disabled = false;
    document.getElementById('full_analysis').disabled = false;
    fullAnalysisButton.classList.remove('hiding');   
}

function onCancelReport(){
    var fullAnalysisButton = document.getElementById('full_analysis');

    document.getElementById("obs").disabled = true;
    document.getElementById('editButton').disabled = false; 

    document.getElementById("obs").value = initialObsValue;

    document.getElementById('editReport').style.display = 'block';
    document.getElementById('saveReport').style.display = 'none';
    document.getElementById('cancelReport').style.display = 'none';

    document.getElementById('download_button').disabled = false;
    document.getElementById('full_analysis').disabled = false;
    fullAnalysisButton.classList.remove('hiding');   
}