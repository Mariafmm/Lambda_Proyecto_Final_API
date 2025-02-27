import { useEffect, useState } from "react";
import CrudTable from "../../Tabla/componets/tabla";
import api from "../../../services/api";
// import api from "../services/api";

const Notas = () => {
  const [data, setData] = useState([]);
  const [columns, setColumns] = useState([]);

  useEffect(() => {
    api.get("/notas/list/")
      .then((res) => {
        console.log("Respuesta de la API:", res.data); // Verifica la estructura
        const results = res.data.results || [];
        setData(results); 

        if (results.length > 0) {
          setColumns(Object.keys(results[0])); 
        }
      })
      .catch((error) => {
        console.error("Error al obtener datos:", error);
        setData([]); // Evita que data sea undefined
      });
  }, []);

  // const handleCreate = (newUser) => {
  //   api.create("users", newUser).then(() => {
  //     setData([...data, { id: Date.now(), ...newUser }]); // Agregar al estado
  //   });
  // };

  // const handleUpdate = (id, updatedUser) => {
  //   api.update("users", id, updatedUser).then(() => {
  //     setData(data.map((u) => (u.id === id ? updatedUser : u)));
  //   });
  // };

  // const handleDelete = (id) => {
  //   api.delete("users", id).then(() => {
  //     setData(data.filter((u) => u.id !== id));
  //   });
  // };

  return (
    <>
      <h1>Gestion de Notas</h1>
      <CrudTable
        columns={columns}
        data={data}
        // onCreate={handleCreate}
        // onUpdate={handleUpdate}
        // onDelete={handleDelete}
      />
      </>
  );
};

export default Notas;
