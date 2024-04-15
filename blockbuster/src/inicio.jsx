import React from "react";
import { Link } from "react-router-dom";
import Columna from "./components/utils/Columna";
import gifUsuario from "./assets/gifs/usuario.gif";
import gifPeliculas from "./assets/gifs/peliculas.gif";
import gifRenta from "./assets/gifs/renta.gif";

function Inicio() {
  return (
    <div className="main-container">
      <h1>¡Bienvenido a Blockbuster!</h1>
      <div className="options-container">
        <Link to="/crudUsuarios">
          <Columna titulo="Usuarios" gifUrl={gifUsuario} />
        </Link>
        <Link to="/crudPeliculas">
          <Columna titulo="Peliculas" gifUrl={gifPeliculas} />
        </Link>
        <Link to="/crudRentas">
          <Columna titulo="Rentas" gifUrl={gifRenta} />
        </Link>
      </div>
    </div>
  );
}

export default Inicio;
