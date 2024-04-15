import React, { useState } from "react";
import UserTable from "./rentaTable";
import AddUserForm from "./agregarRentaForm";
import EditUserForm from "./editarRentaForm";
import { set } from "react-hook-form";

function CrudRenta() {
  const usersData = [
    {
      id: 1,
      pelicula: "Caperucita",
      usuario: "Bad Bunny",
      fechaRenta: "2021-10-10",
    },
    {
      id: 2,
      pelicula: "Harry Potter",
      usuario: "Jaun Perez",
      fechaRenta: "2009-02-01",
    },
    { id: 3, pelicula: "Ironman", usuario: "Alan", fechaRenta: "1893-02-01" },
  ];

  const num_id = usersData.length + 1;

  // State
  const [users, setUsers] = useState(usersData);
  const [editing, setEditing] = useState(false);
  const [currentUser, setCurrentUser] = useState({
    id: null,
    pelicula: "",
    usuario: "",
    fechaRenta: "",
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
      pelicula: user.pelicula,
      usuario: user.usuario,
      fechaRenta: user.fechaRenta,
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
      <h1>CRUD Rentas</h1>

      <div className="flex-row">
        <div className="flex-large">
          {editing ? (
            <div>
              <h2>Editar rentas</h2>
              <EditUserForm currentUser={currentUser} updateUser={updateUser} />
            </div>
          ) : (
            <div>
              <h2>Agregar rentas</h2>
              <AddUserForm addUser={addUser} />
            </div>
          )}
        </div>

        <div className="flex-large">
          <h2>Ver rentas</h2>
          <UserTable users={users} deleteUser={deleteUser} editRow={editRow} />
        </div>
      </div>
    </div>
  );
}

export default CrudRenta;
