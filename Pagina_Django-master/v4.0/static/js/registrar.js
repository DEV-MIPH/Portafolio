$(document).ready(function() {
  $(".error").hide();

  $("#register-form").submit(function(event) {
    event.preventDefault();

    var email = $('#email').val();
    var password = $('#password').val();
    var confirmPassword = $('#confirm-password').val();
    var nombre = $('#nombre').val();
    var region = $('#region').val();
    var comuna = $('#comuna').val();

    // Validar campos del formulario
    if (!email || !isValidEmail(email)) {
      $(".error1").text('Por favor, ingresa un correo electrónico válido.').show();
      return;
    } else {
      $(".error1").hide();
    }

    if (nombre === "") {
      $(".error2").text('Por favor, ingresa tu nombre completo.').show();
      return;
    } else {
      $(".error2").hide();
    }

    if (!password || password.length < 8) {
      $(".error3").text('La contraseña debe tener al menos 8 caracteres.').show();
      return;
    } else {
      $(".error3").hide();
    }

    if (password !== confirmPassword) {
      $(".error4").text('Las contraseñas no coinciden.').show();
      return;
    } else {
      $(".error4").hide();
    }

    if (region <= 0) {
      $(".error5").text('Por favor, ingresa tu región.').show();
      return;
    } else {
      $(".error5").hide();
    }

    if (comuna === "") {
      $(".error6").text('Por favor, ingresa tu comuna.').show();
      return;
    } else {
      $(".error6").hide();
    }

    // Si llega hasta aquí, los datos son válidos
    $("#register-form")[0].submit();
  });

  // Cargar regiones y comunas desde la API
  $.getJSON('https://my-json-server.typicode.com/MisterPoro/API-REGIONES-CHILE/db', function(data) {
    var options = '';
    $.each(data.regiones, function(index, value) {
      options += '<option value="' + value.id + '">' + value.nombre + '</option>';
    });
    $('#region').append(options);
  });

  $('#region').change(function() {
    var region_id = $(this).val();
    if (region_id != '') {
      $.getJSON('https://my-json-server.typicode.com/MisterPoro/API-REGIONES-CHILE/regiones/' + region_id, function(data) {
        var options = '';
        $.each(data.comunas, function(index, value) {
          if (value != '') {
            options += '<option value="' + value + '">' + value + '</option>';
          }
        });
        $('#comuna').html(options);
      });
    } else {
      $('#comuna').html('<option value="">Seleccione una comuna</option>');
    }
  });

  // Validar correo suscripción
  $("#subscribe-form").submit(function(event) {
    event.preventDefault();
    var email = $('#suscribirse_input').val();
    if (!email || !isValidEmail(email)) {
      $("#errorValidarCorreo").text('Por favor, ingresa un correo electrónico válido.').show();
    } else {
      $("#errorValidarCorreo").text("Gracias por suscribirte").show();
      // Puedes enviar el formulario o realizar otras acciones aquí
      $("#subscribe-form")[0].submit();
    }
  });
});

function isValidEmail(email) {
  var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}






  