import PropTypes from "prop-types"
import '../utils/Home.css'
import { useState } from 'react'

function Home(props) {
    
    const Tareas = () =>{
        setMenu("tareas");
    };
    const Notas = () =>{
        setMenu("Notas");
    };
    const Categorias = () =>{
        setMenu("categoria");
    };

    const Recordatorios = () =>{
        setMenu("recordatorio");
    };
    const [menu, setMenu] = useState("")
    let contenido;
    let HomeBody;
    if (props.is_admin === false) {
        contenido = (
            <div>
            <button onClick={Tareas}>Ver mis tareas</button>
            <button onClick={Notas}>Ver Notas asignadas</button>
            </div>
        )
    }else{
        contenido = (
            <div className="botones">
            <button onClick={Tareas}>Tareas</button>
            <button onClick={Notas}>Notas</button>
            <button onClick={Categorias}>Categorias</button>
            <button onClick={Recordatorios}>Recordatorios</button>
            </div>
        )
    }

    return (
        <>
        <div className="titulo_p">
        <h2 className="bienvenido" >Bienvenid@ {props.nombre}</h2>
        {contenido}
        {HomeBody}
        </div>
        
        <h1>presionaste {menu}</h1>
         </>
    )

}
Home.propTypes = { 
    nombre: PropTypes.string.isRequired, // Indica que "nombre" debe ser un string obligatorio
    is_admin:PropTypes.bool.isRequired,
}; //si no se valida puede generar un error de sintaxis

export default Home;