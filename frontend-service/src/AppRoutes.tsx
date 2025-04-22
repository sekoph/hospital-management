import { createBrowserRouter } from 'react-router-dom'
import AuthLayout from './Layout/AuthLayout'
import Login from './pages/Auth/Login'
import Register from './pages/Auth/Register'
import AdminLayout from './Layout/AdminLayout'
import DoctorLayout from './Layout/DoctorLayout'
import PatientLayout from './Layout/PatientLayout'
import ProtectedRoutes from './pages/Auth/ProtectedRoutes'
import AdminDashboard from './pages/Admin/AdminDashboard'
import DoctorDashboard from './pages/Doctors/DoctorDashboard'
import PatientDashboard from './pages/Patient/PatientDashboard'


const AppRoutes = createBrowserRouter([
  {
    path: "/",
    element: <AuthLayout/>,
    children: [
      {
        path:"/",
        element: <Login/>
      },
      {
        path:"register",
        element:<Register/>
      }
    ]
  },
  {
    path: "/admin",
    element: (
      <ProtectedRoutes allowedRoles={['admin']}>
        <AdminLayout/>,
      </ProtectedRoutes>),
    children:[
      {
        path:"",
        element:<AdminDashboard/>
      }
    ]
  },
  {
    path: "/doctor",
    element: (
      <ProtectedRoutes allowedRoles={['doctor']}>
        <DoctorLayout/>
      </ProtectedRoutes>
    ),
    children:[
      {
        path:"",
        element:<DoctorDashboard/>
      }
    ]
  },
  {
    path: "patient",
    element:(
      <ProtectedRoutes allowedRoles={['patient']}>
        <PatientLayout/>
      </ProtectedRoutes>
    ),
    children:[
      {
        path:"",
        element:<PatientDashboard/>
      }
    ]
  }
])

export default AppRoutes