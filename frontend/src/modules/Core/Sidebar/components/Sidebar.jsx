import { useNavigate, Outlet } from 'react-router-dom';
import { useState } from 'react';
import { LogOut, User } from 'lucide-react'; // Iconos bonitos 😎
import '../utils/Sidebar.css';

export default function Sidebar() {
    const navigate = useNavigate();
    const [open, setOpen] = useState(false); // Controla el despliegue
    const username = localStorage.getItem("username") || "Usuario"; // Nombre del usuario

    const handleLogout = () => {
        localStorage.removeItem("access_token");
        localStorage.removeItem("username");
        navigate("/login");
    };

    return (
        <>
            <nav className="titulo_p">
                <h1 className="actividad">Actividades de React</h1>
                <ul className="titulo_p-items">
                    <li><button className="dias" onClick={() => navigate('/usuarios')}>Usuarios</button></li>
                    <li><button className="dias" onClick={() => navigate('/notas')}>Notas</button></li>
                    <li><button className="dias" onClick={() => navigate('/tareas')}>Tarea</button></li>
                    <li><button className="dias" onClick={() => navigate('/categorias')}>Categoria</button></li>
                    <li><button className="dias" onClick={() => navigate('/recordatorios')}>Recordatorios</button></li>
                </ul>

                {/* Menú desplegable de usuario */}
                <div className="dropdown-container">
                    <button
                        className="user-button"
                        onClick={() => setOpen(!open)}
                    >
                        <User style={{ width: "24px", height: "24px", color: "#333" }} />
                    </button>

                    {open && (
                        <div className="dropdown-menu">
                            <div className="dropdown-header">
                                <p style={{ color: "white", fontWeight: "bold" }}>{username}</p>
                            </div>
                            <button
                                onClick={handleLogout}
                                className="logout-button"
                            >
                                <LogOut style={{ width: "20px", height: "20px", marginRight: "8px" }} />
                                Cerrar Sesión
                            </button>
                        </div>
                    )}
                </div>
            </nav>

            <div className="flex">
                <Outlet />
            </div>
        </>
    );
}
