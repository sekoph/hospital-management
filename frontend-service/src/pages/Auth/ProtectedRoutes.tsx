import { useAuth } from "@/contexts/AuthContext"
import { Navigate } from "react-router-dom";

const ProtectedRoutes = ({children, allowedRoles}) => {

    // const {currentUser} = useAuth();
    const currentUser = {
        role: "admin"
    }

    if(!currentUser) return <Navigate to="/"/>


    if(allowedRoles && !allowedRoles.includes(currentUser.role)){

        switch(currentUser.role){
            case "admin":
                return <Navigate to="/admin" />;
            case "doctor":
                return <Navigate to="/doctor" />
            default:
                return <Navigate to="/patient"/>
        }
    }
  return children
}

export default ProtectedRoutes