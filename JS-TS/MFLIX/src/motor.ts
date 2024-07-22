import { FiltroPeliculas, Pelicula,TipoGenero } from "./modelo"

export const filtrarPeliculasPorGenero = (
    peliculas: Pelicula[],
    genero? : TipoGenero

): Pelicula[] => peliculas.filter((pelicula) => pelicula.genero === genero)


const filtrarPeliculasPorPremio = (
    peliculas: Pelicula[],
): Pelicula[] => peliculas.filter((pelicula) => pelicula.premioGalardon === true);


const filtrarPeliculasMasVistas = (
    peliculas: Pelicula[],
): Pelicula[] =>peliculas.filter((pelicula) => pelicula.masVisto === true);

const ordenarPeliculasPorCalificacion = (
    peliculas: Pelicula[],
): Pelicula[] => peliculas.sort((peliculaA, peliculaB) => peliculaB.calificacionImdb - peliculaA.calificacionImdb);

export const filtrarPeliculas = (
    peliculas: Pelicula[],
    filtro?: FiltroPeliculas
): Pelicula[] => {
    if(!filtro) return peliculas;


    switch(filtro.caracteristicas){
        case "genero":
                return filtrarPeliculasPorGenero(peliculas, filtro.genero);
        case "premios":
            return filtrarPeliculasPorPremio(peliculas);
        case "masVistas":
            return filtrarPeliculasMasVistas(peliculas);
        case "calificacion":
            return ordenarPeliculasPorCalificacion(peliculas);
        default:
            return peliculas
    }
}


