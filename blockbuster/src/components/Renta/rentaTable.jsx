import React from "react";

const UserTable = (props) => (
  <table>
    <thead>
      <tr>
        <th>ID</th>
        <th>Pelicula</th>
        <th>Usuario</th>
        <th>Fecha de renta</th>
        <th>Acciones</th>
      </tr>
    </thead>
    <tbody>
      {props.users.length > 0 ? (
        props.users.map((user) => (
          <tr key={user.id}>
            <td>{user.id}</td>
            <td>{user.pelicula}</td>
            <td>{user.usuario}</td>
            <td>{user.fechaRenta}</td>
            <td>
              <button
                className="button muted-button"
                onClick={() => {
                  props.editRow(user);
                }}
              >
                Editar
              </button>
            </td>
          </tr>
        ))
      ) : (
        <tr>
          <td colSpan={3}>No hay rentas</td>
        </tr>
      )}
    </tbody>
  </table>
);

export default UserTable;
