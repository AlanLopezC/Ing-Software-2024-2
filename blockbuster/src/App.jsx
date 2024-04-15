import React from "react";

import "./App.css";

import { BrowserRouter, Route, Routes } from "react-router-dom";

import CrudUsuario from "./components/Usuario/crudUsuario";
import CrudPelicula from "./components/Pelicula/crudPelicula";
import CrudRenta from "./components/Renta/crudRenta";
import Inicio from "./inicio";

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Inicio />} />
        <Route path="/crudUsuarios" element={<CrudUsuario />} />
        <Route path="/crudPeliculas" element={<CrudPelicula />} />
        <Route path="/crudRentas" element={<CrudRenta />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;
