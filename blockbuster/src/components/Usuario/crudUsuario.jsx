import React, { useState } from "react";
import UserTable from "./usuarioTable";
import AddUserForm from "./agregarUsuarioForm";
import EditUserForm from "./editarUsuarioForm";
import { set } from "react-hook-form";

function CrudUsuario() {
  const usersData = [
    { id: 1, name: "Pepe", username: "locomoras" },
    { id: 2, name: "Lau", username: "tuttifrutti" },
    { id: 3, name: "Ben", username: "parker" },
  ];

  const num_id = usersData.length + 1;

  // State
  const [users, setUsers] = useState(usersData);
  const [editing, setEditing] = useState(false);
  const [currentUser, setCurrentUser] = useState({
    id: null,
    name: "",
    username: "",
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
      username: user.username,
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
      <h1>CRUD Usuarios</h1>

      <div className="flex-row">
        <div className="flex-large">
          {editing ? (
            <div>
              <h2>Editar usuarios</h2>
              <EditUserForm currentUser={currentUser} updateUser={updateUser} />
            </div>
          ) : (
            <div>
              <h2>Agregar usuarios</h2>
              <AddUserForm addUser={addUser} />
            </div>
          )}
        </div>

        <div className="flex-large">
          <h2>Ver usuarios</h2>
          <UserTable users={users} deleteUser={deleteUser} editRow={editRow} />
        </div>
      </div>
    </div>
  );
}

export default CrudUsuario;
