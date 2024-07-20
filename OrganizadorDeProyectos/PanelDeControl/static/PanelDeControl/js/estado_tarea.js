function toggleTareaCompletada(id, checkbox) {
    var completed = checkbox.checked;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", actualizarTareasUrl, true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.setRequestHeader("X-CSRFToken", csrfToken);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (!response.success) {
                alert("Error actualizar_tareas: " + response.error);
                checkbox.checked = !completed;  // Revierte el estado del checkbox si hay un error
            }
        }
    };

    xhr.send("id=" + id + "&completed=" + completed);
}