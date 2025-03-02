import React from 'react'
import { Navigate, useLocation } from 'react-router-dom'


export default function ProtectedRouter({ children }) {
    const location = useLocation();
    const isAuthenticated = !!localStorage.getItem('access_token');

    if (!isAuthenticated) {
        return <Navigate to="/login" state={{from:location}} />;
    }
  return ( children )
}
