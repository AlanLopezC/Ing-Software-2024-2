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
      <label>Titulo</label>
      <input
        type="text"
        {...register("name", {
          required: { value: true, message: "Campo Requerido" },
        })}
      />
      <div>{errors?.name?.message}</div>
      <label>Director</label>
      <input
        type="text"
        {...register("director", {
          required: { value: true, message: "Campo Requerido" },
        })}
      />
      <div>{errors?.director?.message}</div>
      <button>Agregar nueva pelicula</button>
    </form>
  );
};

export default AddUserForm;
