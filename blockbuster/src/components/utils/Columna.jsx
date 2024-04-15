// Columna.js
import React from "react";
import "./Columna.css"; // Asegúrate de tener un archivo CSS para estilar tus componentes

const Columna = ({ titulo, gifUrl }) => {
  return (
    <div className="columna">
      <div className="carta">
        <h2 className="titulo">{titulo}</h2>
        <img src={gifUrl} alt="GIF" className="gif" />
      </div>
    </div>
  );
};

export default Columna;
