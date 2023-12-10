
var imagenInput = document.querySelector('input[name="imagen"]');
imagenInput.addEventListener('change', previewImage);

function previewImage() {
    var imagenPreview = document.getElementById('imagen-preview');
    var reader = new FileReader();
    reader.onload = function (e) {
        imagenPreview.src = e.target.result;
    }
    reader.readAsDataURL(this.files[0]);
}
