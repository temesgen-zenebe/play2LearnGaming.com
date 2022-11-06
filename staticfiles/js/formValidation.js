// Example starter JavaScript for disabling form submissions if there are invalid fields
window.addEventListener('load',() => {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')
    
    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        if (form.checkValidity()) {
            //alert('1'+form.checkValidity())
            event.preventDefault()
            event.stopPropagation()
            gameLaunch();
            //getOption();
        }
        
        //alert('2'+form.checkValidity())
        form.classList.add('was-validated')
        
      }, true)
    })
});
