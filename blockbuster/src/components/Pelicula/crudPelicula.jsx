import React, { useState } from "react";
import UserTable from "./peliculaTable";
import AddUserForm from "./agregarPeliculaForm";
import EditUserForm from "./editarPeliculaForm";

function CrudPelicula() {
  const usersData = [
    { id: 1, name: "Caperucita", director: "Pepe Pecas" },
    { id: 2, name: "Buscando a Nemo", director: "Nelson Mandela" },
    { id: 3, name: "La orca", director: "Ben Nelson" },
  ];

  const num_id = usersData.length + 1;

  // State
  const [users, setUsers] = useState(usersData);
  const [editing, setEditing] = useState(false);
  const [currentUser, setCurrentUser] = useState({
    id: null,
    name: "",
    director: "",
  });
  const [newId, setNewId] = useState(num_id);

  // Functions
  const updateUser = (id, updatedUser) => {
    setEditing(false);
    setUsers(users.map((user) => (user.id === id ? updatedUser : user)));
  };

  const editRow = (user) => {
    setEditing(true);
    setCurrentUser({
      id: user.id,
      name: user.name,
      director: user.director,
    });
  };

  const addUser = (user) => {
    user.id = newId;
    setNewId(newId + 1);
    setUsers([...users, user]);
  };

  const deleteUser = (id) => {
    setUsers(users.filter((user) => user.id !== id));
  };

  return (
    <div className="container">
      <h1>CRUD Peliculas</h1>

      <div className="flex-row">
        <div className="flex-large">
          {editing ? (
            <div>
              <h2>Editar pelicula</h2>
              <EditUserForm currentUser={currentUser} updateUser={updateUser} />
            </div>
          ) : (
            <div>
              <h2>Agregar pelicula</h2>
              <AddUserForm addUser={addUser} />
            </div>
          )}
        </div>

        <div className="flex-large">
          <h2>Ver peliculas</h2>
          <UserTable users={users} deleteUser={deleteUser} editRow={editRow} />
        </div>
      </div>
    </div>
  );
}

export default CrudPelicula;
