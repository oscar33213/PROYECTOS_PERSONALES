interface Clinica {
  turno: number;
}

// Función para crear una clínica
function crearClinica(): Clinica {
  return {
    turno: 0,
  };
}

function siguienteTurno(clinica: Clinica): void {
  clinica.turno++;
  mostrarTurno(clinica);
}

function anteriorTurno(clinica: Clinica): void {
  if (clinica.turno > 0) {
    clinica.turno--;
    mostrarTurno(clinica);
  }
}

function resetearTurno(clinica: Clinica): void {
  clinica.turno = 0;
  mostrarTurno(clinica);
}

function cambiarTurno(clinica: Clinica, valor: number): void {
  clinica.turno = valor;
  mostrarTurno(clinica);
}

function formatearTurno(turno: number): string {
  return turno.toString().padStart(2, "0");
}

function mostrarTurno(clinica: Clinica): void {
  const numeroTurno = document.querySelector<HTMLSpanElement>(".numero-turno");
  if (numeroTurno !== null) {
    numeroTurno.textContent = formatearTurno(clinica.turno);
  }
}

// Crear una instancia de la clínica
const clinica: Clinica = crearClinica();

// Manejador de evento para el botón Siguiente
const botonSiguiente = document.getElementById("siguiente");
if (botonSiguiente instanceof HTMLButtonElement) {
  botonSiguiente.addEventListener("click", function () {
    siguienteTurno(clinica);
  });
}

// Manejador de evento para el botón Anterior
const botonAnterior = document.getElementById("anterior");
if (botonAnterior instanceof HTMLButtonElement) {
  botonAnterior.addEventListener("click", function () {
    anteriorTurno(clinica);
  });
}

// Inicializar la interfaz de usuario
mostrarTurno(clinica);
