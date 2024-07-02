function toggleAnswer(element) {
    const answer = element.nextElementSibling;
    if (answer.style.display === "block") {
        answer.style.display = "none";
    } else {
        answer.style.display = "block";
    }
}
function validarFormulario() {
    // Obtener los valores de los campos
    let nombre = document.getElementsByName("Nombre")[0].value;
    let apellido = document.getElementsByName("Apellido")[0].value;
    let direccion = document.getElementsByName("Direccion")[0].value;
    let provincia = document.getElementsByName("Provincia")[0].value;
    let zipCode = document.getElementsByName("ZipCode")[0].value;
    let fechaNacimiento = document.getElementsByName("fecha_nacimiento")[0].value;
    let email = document.getElementsByName("Email")[0].value;
    let telefono = document.getElementsByName("Telefono")[0].value;
   

    let genero = document.querySelector('input[name="genero"]:checked');
  
    let oficio = document.querySelector('input[name="Oficio"]:checked');
    
    let firma = document.getElementsByName("Signature")[0].value;
   


    let fechaAuth = document.getElementsByName("DateAuth")[0].value;
   

   
   
    // Validar que los campos no estén vacíos
    if (nombre === "" || apellido === "" || direccion === "" || provincia === "" || zipCode === "" ||
        fechaNacimiento === "" || email === "" || telefono === "" || !genero || !oficio || firma === "" || fechaAuth === "") {
        alert("Todos los campos son obligatorios.");
        return false;
    }

    // Validar que el email tenga un formato válido
    let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert("Por favor, ingresa un correo electrónico válido.");
        return false;
    }

    // Validar que el código postal sea un número
    if (isNaN(zipCode)) {
        alert("Por favor, ingresa un código postal válido.");
        return false;
    }

    // Validar que el teléfono sea un número
    if (isNaN(telefono)) {
        alert("Por favor, ingresa un número de teléfono válido.");
        return false;
    }
    let hoy = new Date();
    let fechaNacimientoDate = new Date(fechaNacimiento);
    let fechaLimiteNacimiento = new Date();
    fechaLimiteNacimiento.setFullYear(hoy.getFullYear() - 100);
    if (fechaNacimientoDate > hoy || fechaNacimientoDate < fechaLimiteNacimiento) {
            alert("La fecha de nacimiento no puede ser más de 100 años antes de la actual ni en el futuro.");
            return false;
        }

            // Validar la fecha de autorización (no en el futuro y no más de un año atrás)
    let fechaAuthDate = new Date(fechaAuth);
    let fechaLimiteAuth = new Date();
    fechaLimiteAuth.setFullYear(hoy.getFullYear() - 1);
    if (fechaAuthDate > hoy || fechaAuthDate < fechaLimiteAuth) {
        alert("La fecha de autorización no puede ser en el futuro ni más de un año atrás.");
        return false;
    }


    // Si todas las validaciones pasan, permitir el envío del formulario
    return true;
}

function mostrarDatos() {
    var args = location.search.substr(1).split('&');
    var tabla = document.getElementById("tablaDatos");
    for (var i = 0; i < args.length; ++i) {
        var parts = args[i].split('=');
        if (parts != null) {
            var field = parts[0];
            var value = parts[1];
            if (value == null) {
                value = "null";
            } else {
                value = decodeURIComponent(value.replace(/\+/g, ' '));
            }

            var row = tabla.insertRow();
            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);
            cell1.innerHTML = field;
            cell2.innerHTML = value;
        }
    }
}

document.addEventListener("DOMContentLoaded", function() {
    const radioTurnoMañana = document.getElementById("turnoMañana");
    const radioTurnoTarde = document.getElementById("turnoTarde");
    const radioTurnoNoche = document.getElementById("turnoNoche");
    const selectCursos = document.getElementById("cursos");

    radioTurnoMañana.addEventListener("change", cargarCursos);
    radioTurnoTarde.addEventListener("change", cargarCursos);
    radioTurnoNoche.addEventListener("change", cargarCursos);

    function cargarCursos() {
        const selectedTurno = document.querySelector('input[name="turno"]:checked').value;
        fetch(`/cursos/${selectedTurno}`)
            .then(response => response.json())
            .then(cursos => {
                selectCursos.innerHTML = ""; // Limpiar el select antes de poblarlo
                cursos.forEach(curso => {
                    const option = document.createElement("option");
                    option.value = curso.id; // Asegúrate de que 'id' es el identificador correcto
                    option.text = curso.nombre;
                    selectCursos.appendChild(option);
                });
            });
    }
});