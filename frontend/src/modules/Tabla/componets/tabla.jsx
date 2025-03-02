import React, { useState } from "react";
import FormCrud from "./formulario";
import "../utils/tabla.css";

const CrudTable = ({ columns = [], data = [], columns_forms=[], requiredFields = [], onCreate, onUpdate, onDelete, onPagina, currentPage, nextPage, prevPage }) => {
  const [editingId, setEditingId] = useState(null);
  const [isFormVisible, setIsFormVisible] = useState(false);
  const [formData, setFormData] = useState(null);

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
      onUpdate(editingId, form);  // Aquí debe ejecutarse correctamente
    } else {
      onCreate(form);
    }
    setIsFormVisible(false);
  };

  return (
    <>
      <button onClick={handleCreate} className="crear btn">
        Crear Nuevo
      </button>
      <div className="contenido">
        {isFormVisible && (
          
        <div className="formulario">
          <FormCrud
            columns={columns_forms}
            onSubmit={handleSubmit}
            onCancel={() => setIsFormVisible(false)}
            initialData={formData}
            requiredFields={requiredFields}
          />          
        </div>
        )}
        <div className="scroll"> 
        <table className="tabla">
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
                  <td key={col}>{typeof item[col] === "boolean" ? (item[col] ? "Sí" : "No") : item[col]}</td>
                ))}
                <td>
                  <button className="btn editar" onClick={() => handleEdit(item)}>Editar</button>
                  <button className="btn borrar" onClick={() => onDelete(item.id)}>Eliminar</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        </div>
      </div>
      <br />
      <div className="paginacion">
        <button onClick={() => onPagina(prevPage)} disabled={!prevPage}>
          Anterior
        </button>
        <span>Página {currentPage}</span>
        <button onClick={() => onPagina(nextPage)} disabled={!nextPage}>
          Siguiente
        </button>
      </div>
    </>
  );
};

export default CrudTable;

