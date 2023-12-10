// Realiza una solicitud GET a la API
fetch('https://misterporo.github.io/API-REGIONES-CHILE/db.json')
  .then(response => response.json())
  .then(data => {
    // Obtiene la respuesta de la API y la muestra en la página
    const responseContainer = document.getElementById('response');
    data.regiones.forEach(region => {
      const regionDiv = document.createElement('div');
      regionDiv.innerHTML = `<h3>${region.nombre}</h3><ul>${region.comunas.map(comuna => `<li>${comuna}</li>`).join('')}</ul>`;
      responseContainer.appendChild(regionDiv);
    });
  })
  .catch(error => {
    console.error(error);
  });
