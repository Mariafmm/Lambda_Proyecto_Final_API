import Login from './modules/Login/components/Login'
import './modules/Login/utils/Login.css'
import './App.css'
import { Routes, Route } from 'react-router-dom'
import Notas from './modules/Notas/components/notas'
import Sidebar from './modules/Core/Sidebar/components/Sidebar'
import Tareas from './modules/Tareas/components/tareas'
import Recordatorios from './modules/Recordatorios/components/recordatorios'
import Categorias from './modules/Categoria/components/categoria'
import ProtectedRouter from './modules/Core/ProtectedRoute/ProtectedRouter'
import Usuarios from './modules/usuarios/components/usuarios'

function App() {  
  return (
    <>
      <Routes>
          <Route path='/login' element={<Login/>}/>
          <Route path='/' element={ <ProtectedRouter>  <Sidebar/> </ProtectedRouter>}>
              <Route path='/notas' element={<Notas/>}/>
              <Route path='/tareas' element={<Tareas/>}/>
              <Route path='/categorias' element={<Categorias/>}/>
              <Route path='/recordatorios' element={<Recordatorios/>}/>
              <Route path='/usuarios' element={<Usuarios/>}/>
          </Route>
      </Routes>     
    </>
  )
};

export default App;