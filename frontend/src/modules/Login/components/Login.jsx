import '../utils/Login.css'
import {useState} from "react";
import api from "../../../services/api";

function Login() {
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

            console.log("Login exitoso:", response.data);
            localStorage.setItem("access_token", response.data.token); // Guarda el token
            alert("Inicio de sesión exitoso"); // Puedes redirigir al usuario aquí
        } catch (error) {
            console.error("Error al iniciar sesión:", error);
            setError("Credenciales incorrectas. Inténtalo de nuevo.");
        } finally {
            setLoading(false);
        }
    };

  return (
    <>
        <form onSubmit={handleLogin} className='Login'>
            <h2>Inicie Sesion</h2>
            {/* Muestra el error si existe */}
            {error && <p className="error">{error}</p>}
            <input type="text" placeholder='Email' value={email} onChange={e=>setEmail(e.target.value)}/>
            <br/>
            <input type="text" placeholder='Contraseña' value={password} onChange={e=>setPassword(e.target.value)}/>
            <br/>
            <button type='submit'disabled={loading}>
                    {loading ? "Cargando..." : "Ingresar"}
                </button>
        </form>
    </>
  )
}

export default Login