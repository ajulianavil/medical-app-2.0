function validateNumberInput(input) {
    // Remove non-numeric characters from the input value
    input.value = input.value.replace(/\D/g, '');
  }
