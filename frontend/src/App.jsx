
import Home from './modules/componets/Home'
import './modules/utils/Home.css'
import './App.css'

function App() {
  

  const Nombre_Usuario = "Maria_F";{/*quemado mientras conectamos a los endpoints*/}  
  const admin = false;
  return (
    <>
      <Home nombre = {Nombre_Usuario} is_admin = {admin}></Home>

      <div className='imagen_inicio'>dfsfds</div>
    </>
  )
}

export default App
