import React, { useState, useEffect } from "react";

const FormCrud = ({ columns, onSubmit, onCancel, initialData }) => {
  const [form, setForm] = useState(initialData || {}); // Iniciar con datos previos si existen

  useEffect(() => {
    setForm(initialData || {}); // Actualizar el formulario cuando cambie initialData
  }, [initialData]);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(form); // Envía los datos al componente padre
  };

  return (
    <div className="contenido visible">
      <form onSubmit={handleSubmit}>
        {columns.map((col) => (
          <input
            key={col}
            type="text"
            name={col}
            placeholder={col}
            value={form[col] || ""}
            onChange={handleChange}
            required
          />
        ))}
        <button type="submit">{initialData ? "Actualizar" : "Agregar"}</button>
        <button type="button" onClick={onCancel}>Cancelar</button>
      </form>
    </div>
  );
};

export default FormCrud;
