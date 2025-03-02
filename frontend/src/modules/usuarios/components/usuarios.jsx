import { useEffect, useState } from "react";
import CrudTable from "../../Tabla/componets/tabla";
import api from "../../../services/api";

const Usuarios = () => {
  const [data, setData] = useState([]);
  const [columns, setColumns] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [nextPage, setNextPage] = useState(null);
  const [prevPage, setPrevPage] = useState(null);
  const columns_forms = ['first_name', 'last_name', 'email', 'phone', 'password', 'role']
  const requiredFields = ['first_name', 'last_name', 'email', 'password'];

  const fetchData = (page) => {
    api.get(`/users/list/?page_size=${page}`)
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
    api.post("/users/crear/", newUser).then(() => {
      fetchData(currentPage);
    });
  };

  const handleUpdate = (id, updatedUser) => {
    console.log(id)
    api.patch(`/users/editar/${id}/`, updatedUser) // Asegúrate de que la URL esté bien construida

      .then(() => {
        setData(data.map((u) => (u.id === id ? { ...u, ...updatedUser } : u)));
      })
      .catch((error) => {
        console.error("Error al actualizar el usuario:", error);
      });
  };
  const handleDelete = (id) => {
    const isConfirmed = window.confirm("¿Estás seguro de que quieres eliminar este usuario?");

    if (isConfirmed) {
      api.delete(`/users/borrar/${id}/`)
        .then(() => {
          setData(data.filter((u) => u.id !== id));
        })
        .catch((error) => {
          console.error("Error al eliminar el usuario:", error);
        });
    }
  };

  return (
    <>
      <br/>
      <h1>Gestión de Usuarios</h1>
      <CrudTable
        columns={columns}
        columns_forms = {columns_forms}
        requiredFields={requiredFields}
        data={data}
        currentPage={currentPage}
        nextPage={nextPage}
        prevPage={prevPage}
        onPagina={handlePagina}
        onCreate={handleCreate}
        onUpdate={handleUpdate}
        onDelete={handleDelete}
      />
    </>
  );
};

export default Usuarios;

