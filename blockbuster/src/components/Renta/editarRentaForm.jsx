import React from "react";
import { useForm } from "react-hook-form";

const EditUserForm = (props) => {
  const { register, errors, handleSubmit, setValue } = useForm({
    defaultValues: props.currentUser,
  });

  setValue("pelicula", props.currentUser.pelicula);
  setValue("usuario", props.currentUser.usuario);
  setValue("fechaRenta", props.currentUser.fechaRenta);

  const onSubmit = (data, e) => {
    data.id = props.currentUser.id;
    e.target.reset();
    props.updateUser(props.currentUser.id, data);
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
      <div>{errors?.usuario?.message}</div>
      <label>Fecha de renta</label>
      <input
        type="text"
        {...register("fechaRenta", {
          required: { value: true, message: "Campo Requerido" },
        })}
      />
      <div>{errors?.fechaRenta?.message}</div>
      <button>Edita renta</button>
    </form>
  );
};
export default EditUserForm;
