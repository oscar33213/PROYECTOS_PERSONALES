import { peliculas } from "./datos";
import { pintarListaPeliculas } from "./ui";

document.addEventListener("DOMContentLoaded", () => {
    pintarListaPeliculas(peliculas, {titulo: "Todas las peliculas"});
    pintarListaPeliculas(
        peliculas, 
        {
            titulo: "Peliculas De Aventura",
            filtro: {genero: "Aventuras", caracteristicas: "genero"}
        })

    pintarListaPeliculas(peliculas, {
        titulo: "Peliculas Familiares",
        filtro: {
            genero: "Familiar",
            caracteristicas: "genero",
        }
    });

    pintarListaPeliculas(peliculas, {
        titulo: "Peliculas de Animación",
        filtro : {
            genero: "Animacion",
            caracteristicas: "genero"
        }
    });

    pintarListaPeliculas(peliculas, {
        titulo: "Peliculas mas vistas",
        filtro: {
            caracteristicas: "masVistas"
        }
    });

    pintarListaPeliculas(peliculas, {
        titulo: "Peliculas con Premio",
        filtro: {caracteristicas: "premios"}
    });

    pintarListaPeliculas(peliculas, {
        titulo: "Peliculas Ordenadas por Calificacion",
        filtro: {caracteristicas: "calificacion"}
    })
});