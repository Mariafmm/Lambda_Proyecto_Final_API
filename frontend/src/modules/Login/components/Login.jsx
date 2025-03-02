import '../utils/Login.css'
import {useState} from "react";
import api from "../../../services/api";
import { useNavigate } from "react-router-dom";


function Login() {
    const navigate = useNavigate();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");


    const handleLogin = async (e) => {
        e.preventDefault(); // Evita la recarga de la página

        setLoading(true);
        setError(""); // Limpia errores previos

        try {
            const response = await api.post("users/login/", {
                email,
                password
            });
            localStorage.setItem("access_token", response.data.token_de_acceso); // Guarda el token
            const username = `${response.data.datos_de_tu_cuenta.first_name} ${response.data.datos_de_tu_cuenta.last_name}`;
            console.log(username)
            localStorage.setItem("username", username); //Guarda el email del usuario
            alert("Inicio de sesión exitoso"); // Puedes redirigir al usuario aquí
            navigate("/usuarios");
        } catch (error) {
            console.error("Error al iniciar sesión:", error);
            alert("Credenciales incorrectas. Inténtalo de nuevo.")
        } finally {
            setLoading(false);
        }
    };

  return (
    <>
        <div className="imagen_inicio">
        <div className='contenido'>
        <form onSubmit={handleLogin} className='Login'>
            <h2>Bienvenido</h2>
            {/* Muestra el error si existe */}
            {error && <p className="error">{error}</p>}
            <input type="text" placeholder='Email' value={email} onChange={e=>setEmail(e.target.value)}/>
            <br/>
            <input type="password" placeholder='Contraseña' value={password} onChange={e=>setPassword(e.target.value)}/>
            <br/>
            <button type='submit'disabled={loading}>
                    {loading ? "Cargando..." : "Ingresar"}
            </button>
        </form>
        </div>
        </div>
    </>
  )
}

export default Login