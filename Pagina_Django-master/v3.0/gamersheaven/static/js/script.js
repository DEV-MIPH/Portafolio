function validateEmail(email) {
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
  }
  
  function validarCorreo() {
    var email_request = document.getElementById("email");
    var email = email_request.value;
    var password_request = document.getElementById("password");
    var password = password_request.value;
    var mensaje
    var error2=document.getElementById("error2");
    var error3=document.getElementById("error3");
    
  
    
    if(email === ""){
      mensaje = 'Por favor, ingresa un correo electrónico válido.';
      error2.innerHTML=mensaje;
      email_request.focus();
      return false
    }else{
      error2.innerHTML="";
    }
    if (!validateEmail(email)) {
      error2.innerHTML = "El correo electrónico no es válido";
      email_request.focus();
      return false;
    }
    if(password === ""){
      mensaje = 'Por favor, ingresa tu contraseña.';
      password_request.focus();
      error3.innerHTML=mensaje;
      return false
    }else{
      error3.innerHTML="";
    }
    document.getElementById("login-form").submit();
    return true;
  }
  
  function validarIngreso() {
    var correcto=document.getElementById("correcto");
    if (validarCorreo() == true) {
      correcto.innerHTML = "Ingresando...";
      return true;
    }else{
      correcto.innerHTML = "";
      return false;
    }
  }

  function validarRegistro() {
    var correo = document.getElementById("suscribirse_input");
    var mensaje;
    var error=document.getElementById("errorValidarCorreo");
    if(validateEmail(correo.value)){
      
      mensaje = '¡Gracias por suscribirte!';
      error.innerHTML= mensaje;
      error.style.color="green";
      return true;
  }else{
    mensaje = 'Por favor, ingresa un correo electrónico válido.';
    error.innerHTML=mensaje;
    error.style.color = "red";
    correo.focus();
    return false;
  }
}
  
  