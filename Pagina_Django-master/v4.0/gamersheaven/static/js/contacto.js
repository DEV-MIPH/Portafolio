$(document).ready(function () {
    $(".error").hide();
    $("#Enviar").click(function (event) {
        event.preventDefault();
        var email = $('#email').val();
        var mensajetxa = $('#mensajes').val();
        var nombre = $('#nombre').val();
        var mensaje;
        var telf = $('#telefono').val();
        var patron = /^(\+?56)?(\s?)(0?9)(\s?)[98765432]\d{7}$/;

        
        if (nombre == "") {
            mensaje = 'Por favor, ingresa tu nombre completo.';
            $(".error2").text(mensaje).show();
            return; // Detiene la ejecución del código
        } else {
            $(".error2").hide();

        }
        if (! email || ! isValidEmail(email)) {
            mensaje = 'Por favor, ingresa un correo electrónico válido.';
            $(".error1").text(mensaje).show();
            return; // Detiene la ejecución del código
        } else {
            $(".error1").hide();

        }
        
        if (!patron.test(telf)) {
            mensaje = 'Telefono Invalido';
            $(".error5").text(mensaje).show();
            return;
          } else {
            $(".error5").hide();
            
            
          }
        if (mensajetxa == "") {
            mensaje = 'No puede enviar el mensaje vacio';
            $(".error4").text(mensaje).show();
            return;
        } else {
            $(".error4").hide();

        }
        alert("Se ha enviado el mensaje")
    });
});
function isValidEmail(email) {
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);


}




