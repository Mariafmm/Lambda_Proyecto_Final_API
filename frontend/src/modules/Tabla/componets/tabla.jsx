import React, { useState } from "react";
import FormCrud from "./formulario";
import "../utils/tabla.css";

const CrudTable = ({ columns = [], data = [], onCreate, onUpdate, onDelete }) => {
  const [editingId, setEditingId] = useState(null);
  const [isFormVisible, setIsFormVisible] = useState(false);
  const [formData, setFormData] = useState(null); // Guarda datos para edición

  const handleCreate = () => {
    setFormData(null);
    setEditingId(null);
    setIsFormVisible(true);
  };

  const handleEdit = (item) => {
    setFormData(item);
    setEditingId(item.id);
    setIsFormVisible(true);
  };

  const handleSubmit = (form) => {
    if (editingId) {
      onUpdate(editingId, form);
    } else {
      onCreate(form);
    }
    setIsFormVisible(false);
  };

  return (
    <>
    {/* Botón para abrir el formulario */}
    <button onClick={handleCreate} className="crear-btn">
        Crear Nuevo
      </button>
    <div className="contenido">
      

      {/* Formulario, solo se muestra si isFormVisible es true */}
      {isFormVisible && (
        <FormCrud
          columns={columns}
          onSubmit={handleSubmit}
          onCancel={() => setIsFormVisible(false)}
          initialData={formData}
        />
      )}

      {/* Tabla de Datos */}
      <table className="tabla" border="1">
        <thead>
          <tr>
            {columns.map((col) => (
              <th key={col}>{col}</th>
            ))}
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item) => (
            <tr key={item.id}>
              {columns.map((col) => (
                <td key={col}>{item[col]}</td>
              ))}
              <td>
                <button onClick={() => handleEdit(item)}>Editar</button>
                <button onClick={() => onDelete(item.id)}>Eliminar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
    </>
  );
};

export default CrudTable;
