
// import Home from './modules/componets/Home'
import './modules/Home/utils/Home.css'
import Login from './modules/Login/components/Login'
import './modules/Login/utils/Login.css'
import './App.css'

function App() {
  

  // const Nombre_Usuario = "Maria_F";{/*quemado mientras conectamos a los endpoints*/}  
  // const admin = true;
  return (
    <>
      <div className="imagen_inicio">
        
      </div>
      <div>
      <Login></Login>
      </div>
      
      {/* <Home nombre = {Nombre_Usuario} is_admin = {admin}></Home> */}
      
      
    </>
  )
}

export default App
