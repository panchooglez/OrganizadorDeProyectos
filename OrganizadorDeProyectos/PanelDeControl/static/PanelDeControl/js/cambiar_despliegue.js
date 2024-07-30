function cambiar_despliegue(id, nuevoValor, boton, checkbox, ruta_despliegue) {
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
    console.log(ruta_despliegue);

    xhr.send("id=" + id + "&desplegada=" + desplegada + "&ruta_despliegue=" + ruta_despliegue);
}

function actualizarVista(id, nuevoValor, boton, checkbox, ruta_despliegue) {
    if (nuevoValor) {
        boton.textContent = 'Apagar';
        boton.setAttribute('onclick', onClickApagar);
        checkbox.checked = true;
    } else {
        boton.textContent = 'Desplegar';
        boton.setAttribute('onclick', onClickDesplegar);
        checkbox.checked = false;
    }
}
