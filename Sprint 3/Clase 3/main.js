var contenido = document.getElementById("contenido")

function traer() {
    fetch('archivo.json').then(data => data.json()).then(data => {
        tabla(data)
    })

}

function tabla(datos) {
    console.log(datos)
    contenido.innerHTML = ''
    for (let valor of datos) {
        console.log(valor)
        contenido.innerHTML += '<tr><th scope="row">' + valor.id + '</th><th>'
            + valor.nombre + '</th><th>'
            + valor.email + '</th><th>'
            + (valor.estado ? "Activo" : "Eliminado") + '</th></tr>'
    }
}
