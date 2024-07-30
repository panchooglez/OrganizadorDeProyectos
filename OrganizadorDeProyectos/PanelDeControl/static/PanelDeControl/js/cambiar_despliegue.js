function cambiar_despliegue(id, nuevoValor, boton, checkbox) {
    var desplegada = nuevoValor;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", cambiar_despliegue_url, true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.setRequestHeader("X-CSRFToken", csrfToken);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (!response.success) {
                console.log(response)
                alert("Error cambiar_despliegue: " + response.error);
            }
            actualizarVista(id, nuevoValor, boton, checkbox);
        }
    };

    xhr.send("id=" + id + "&desplegada=" + desplegada);
}

function actualizarVista(id, nuevoValor, boton, checkbox) {
    if (nuevoValor) {
        boton.textContent = 'Apagar';
        boton.setAttribute('onclick', `cambiar_despliegue(${id}, false, this, document.querySelector('#check${id}'))`);
        checkbox.checked = true;
    } else {
        boton.textContent = 'Desplegar';
        boton.setAttribute('onclick', `cambiar_despliegue(${id}, true, this, document.querySelector('#check${id}'))`);
        checkbox.checked = false;
    }
}