var initialFirstName
var initialLastName
var initialPhone
var initialAddress

document.addEventListener('DOMContentLoaded', function() {
    // Store the initial value of the textarea when enabling report fields
    initialFirstName = document.getElementById("nombres").value
    initialLastName = document.getElementById("apellidos").value
    initialPhone = document.getElementById("telefono").value
    initialAddress = document.getElementById("direccion").value

});

function editProfile(){
    var form = document.getElementById('profile-form');
    var fields = form.getElementsByTagName('input');

    for (var i = 0; i < fields.length; i++) {
        if (fields[i].name === "cedula" || fields[i].name === "email" || fields[i].name === "rol" || fields[i].name === "institucion") {
            continue;
        }
      fields[i].disabled = false;
    }

    document.getElementById('editButton').style.display = 'none';
    document.getElementById('sendButton').style.display = 'flex';
    document.getElementById('cancelInfo').style.display = 'flex';

    document.getElementById('passwordButton').disabled = true;
} 

function enablePassword(){
    document.getElementById('passwordButton').disabled = false;
}

function onCancelEdition(){
    console.log(initialFirstName, initialLastName, initialPhone, initialAddress)
    document.getElementById("nombres").value = initialFirstName 
    document.getElementById("apellidos").value = initialLastName
    document.getElementById("telefono").value = initialPhone
    document.getElementById("direccion").value = initialAddress

    var form = document.getElementById('profile-form');
    var fields = form.getElementsByTagName('input');

    for (var i = 0; i < fields.length; i++) {
        if (fields[i].name === "cedula" || fields[i].name === "email" || fields[i].name === "rol" || fields[i].name === "institucion") {
            continue;
        }
      fields[i].disabled = true;
    }

    enablePassword();
    document.getElementById('editButton').style.display = 'flex';
    document.getElementById('sendButton').style.display = 'none';
    document.getElementById('cancelInfo').style.display = 'none';

}