$(document).ready(function (){
  
    $(".error").hide();
    $("#boton-producto").click(function (event) {
      event.preventDefault();
      var nombre = $('#nombre_producto').val();
      var precio = $('#precio_producto').val();

      
      if (nombre == "") {
          mensaje = 'Por favor, ingresa nombre producto.';
          $(".error2").text(mensaje).show();
          $("#idMensaje").hide();
          return; // Detiene la ejecución del código
      } else {
          $(".error2").hide();
      }

      if (precio <= 0){
        mensaje = 'porfavor ingrese precio.';
        $(".error2").text(mensaje).show();
        $("#idMensaje").hide();
        return
      } else {
        $(".error2").hide();
        
      }$("#formulario-producto")[0].submit();
     
  });
});