import React from "react";
import { useForm } from "react-hook-form";

const EditUserForm = (props) => {
  const { register, errors, handleSubmit, setValue } = useForm({
    defaultValues: props.currentUser,
  });

  setValue("name", props.currentUser.name);
  setValue("director", props.currentUser.director);

  const onSubmit = (data, e) => {
    data.id = props.currentUser.id;
    e.target.reset();
    props.updateUser(props.currentUser.id, data);
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
      <label>Nombre de director</label>
      <input
        type="text"
        {...register("director", {
          required: { value: true, message: "Campo Requerido" },
        })}
      />
      <div>{errors?.director?.message}</div>
      <button>Edita pelicula</button>
    </form>
  );
};
export default EditUserForm;
