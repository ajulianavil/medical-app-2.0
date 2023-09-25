var cardRadioButtonMap = new Map();

document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('form');
  const radioButtons = document.querySelectorAll('input[type="radio"]');
  
  form.addEventListener('change', function (event) {
    const target = event.target;
    var cardContainer = target.closest('.card-two');
    var radioButtonValue = target.value;
    var cardIndex = Array.from(document.querySelectorAll('.card-two')).indexOf(cardContainer);

    const findInMapResult = findInMap(cardRadioButtonMap, radioButtonValue)
    if (findInMapResult.hasValue) {
      cardRadioButtonMap.delete(findInMapResult.key);
    } 
    cardRadioButtonMap.set(cardIndex, radioButtonValue);


    if (target && target.type === 'radio') {
      radioButtons.forEach(function (radioButton) {
        // Your event handling code here for each radio button
        if (radioButton.checked) {
          if (findInMapResult.hasValue) {
            radioButton.checked = false;
          } 
        } 
      });
      //Volvemos a marcar el target
      target.checked = true;
    }
  });
});


const findInMap = (map, val) => {
  for (let [k, v] of map) {
    if (v === val) {
      return { key: k, hasValue: true };
    }
  }
  return { key: null, hasValue: false };
}

function handleRadioButton(radioButton) {

  // var cardContainer = radioButton.closest('.card-two');
  // var radioButtons = cardContainer.querySelectorAll('.right-div input[type="radio"]');
  // //var totalCards = document.querySelectorAll('.card-two').length;

  // var cardIndex = Array.from(document.querySelectorAll('.card-two')).indexOf(cardContainer);
  // var radioButtonIndex = radioButton.value;

  // console.log(cardIndex, radioButtonIndex);

  // var radioId = 'radio_' + cardIndex + '_' + radioButtonIndex;
  // var radd = document.getElementById(radioId);
  // cardRadioButtonMap.set(cardIndex, radioButtonIndex);

  // // var xx = document.getElementById(radioId);
  // console.log("xx", radd)

  // if (isRadioButtonIndexValid(radioButtonIndex)) {




  //   cardRadioButtonMap.forEach(function (value, key) {
  //     // console.log(value, key)

  //     var elementId = 'radio' + radioButtonIndex;
  //     if(key != cardIndex && value ===radioButtonIndex ){
  //       console.log('aqui toca eliminar este hpta id' + key);
  //     }
  //     // var radioButton = document.getElementById(elementId);

  //     // if (radioButton) {
  //     //   console.log("rad", radioButton)
  //     //   // Perform operations on the radio button element
  //     //   radioButton.checked = true;
  //     //   // ... additional operations ...
  //     // }
  //   });
  //   // radioButton.checked = false; 
  // } else {
  //   console.log("here")
  //   cardRadioButtonMap.set(cardIndex, radioButtonIndex);
  // }

  // console.log('Card Index:', cardIndex);
  // console.log('Radio Button Index:', radioButtonIndex);

  // console.log("cardmap", cardRadioButtonMap)
}

function isRadioButtonIndexValid(radioButtonIndex) {
  // Check if the radioButtonIndex is already present in the map for the given cardIndex
  return cardRadioButtonMap.has(radioButtonIndex);
}