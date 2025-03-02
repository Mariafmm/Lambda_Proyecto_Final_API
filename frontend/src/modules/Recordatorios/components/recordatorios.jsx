

import { useEffect, useState } from "react";
import CrudTable from "../../Tabla/componets/tabla";
import api from "../../../services/api";

const Recordatorios= () => {
  const [data, setData] = useState([]);
  const [columns, setColumns] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [nextPage, setNextPage] = useState(null);
  const [prevPage, setPrevPage] = useState(null);
  const columns_forms = ['fecha_recordatorio', 'usuarios', 'content_type', 'contenido_id']
  const fetchData = (page) => {
    api.get(`/recordatorios/list/?page_size=${page}`)
      .then((res) => {
        console.log("Respuesta de la API:", res.data);
        const results = res.data.results || [];
        setData(results);

        if (results.length > 0) {
          setColumns(Object.keys(results[0]));
        }

        // La API devuelve `next` y `previous`, los usamos correctamente.
        setNextPage(res.data.next);
        setPrevPage(res.data.previous);
      })
      .catch((error) => {
        console.error("Error al obtener datos:", error);
        setData([]);
      });
  };

  useEffect(() => {
    fetchData(currentPage);
  }, [currentPage]);

  const handlePagina = (url) => {
    if (url) {
      const urlParams = new URL(url);
      let page = urlParams.searchParams.get("page_size");
      page = page ? Number(page) : 1;
      setCurrentPage(Number(page));
    }
  };

  const handleCreate = (newUser) => {
    api.post("/recordatorios/crear/", newUser).then(() => {
      fetchData(currentPage);
    });
  };

  const handleUpdate = (id, updatedUser) => {
    console.log(id)
    api.patch(`/recordatorios/editar/${id}/`, updatedUser) // Asegúrate de que la URL esté bien construida

      .then(() => {
        setData(data.map((u) => (u.id === id ? { ...u, ...updatedUser } : u)));
      })
      .catch((error) => {
        console.error("Error al actualizar el recordatorio:", error);
      });
  };
  // const handleDelete = (id) => {
  //   const isConfirmed = window.confirm("¿Estás seguro de que quieres eliminar esta nota?");

  //   if (isConfirmed) {
  //     api.delete(`/notas/borrar/${id}/`)
  //       .then(() => {
  //         setData(data.filter((u) => u.id !== id));
  //       })
  //       .catch((error) => {
  //         console.error("Error al eliminar la nota:", error);
  //       });
  //   }
  // };

  return (
    <>
      <br/>
      <h1>Gestión de Recordatorios</h1>
      <CrudTable
        columns={columns}
        columns_forms = {columns_forms}
        data={data}
        currentPage={currentPage}
        nextPage={nextPage}
        prevPage={prevPage}
        onPagina={handlePagina}
        onCreate={handleCreate}
        onUpdate={handleUpdate}
        // onDelete={handleDelete}
      />
    </>
  );
};

export default Recordatorios;
