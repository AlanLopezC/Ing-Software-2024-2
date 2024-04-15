import React from "react";
import { useForm } from "react-hook-form";

const AddUserForm = (props) => {
  const { register, errors, handleSubmit } = useForm();

  const onSubmit = (data, e) => {
    props.addUser(data);
    e.target.reset();
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label>Pelicula</label>
      <input
        type="text"
        {...register("pelicula", {
          required: { value: true, message: "Campo Requerido" },
        })}
      />
      <div>{errors?.pelicula?.message}</div>
      <label>Usuario</label>
      <input
        type="text"
        {...register("usuario", {
          required: { value: true, message: "Campo Requerido" },
        })}
      />
      <div>{errors?.username?.message}</div>
      <label>Fecha de renta</label>
      <input
        type="text"
        {...register("fechaRenta", {
          required: { value: true, message: "Campo Requerido" },
        })}
      />
      <div>{errors?.fechaRenta?.message}</div>
      <button>Agregar nueva renta</button>
    </form>
  );
};

export default AddUserForm;
