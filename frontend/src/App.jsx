
// import Home from './modules/componets/Home'
import './modules/Home/utils/Home.css'
import Login from './modules/Login/components/Login'
import './modules/Login/utils/Login.css'
import './App.css'
import { Routes, Route } from 'react-router-dom'
import Notas from './modules/Notas/components/notas'
// import { useState } from 'react'

function App() {  
  return (
    <>
      <Routes>
          <Route path='' element={<Login/>}/>
          <Route path='/notas' element={<Notas/>}/>
      </Routes>     
    </>
  )
};

export default App;