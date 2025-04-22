import React, { createContext, useState, useContext, useEffect } from "react";


const AuthContext = createContext(null)

type Props = {
    children: React.ReactNode
} 

export const AuthProvider = ({children}: Props) => {
    const [currentUser, setCurrentUser] = useState(null)
    const [loading, setLoading] = useState(true)

    useEffect(()=>{
        const user = localStorage.getItem('user')

        if(user)
            setCurrentUser(JSON.parse(user))
        setLoading(false)
    },[]);

    const login = (userData) => {
        setCurrentUser(userData);
        localStorage.setItem('user', JSON.stringify(userData));
    };

    const logout = () => {
        setCurrentUser(null)
        localStorage.removeItem('user')
    }

    const value = {
        currentUser,
        login,
        logout,
        isAdmin: currentUser?.role === 'admin',
        isDocter: currentUser?.role === 'doctor',
        isPatient: currentUser?.role === 'user',
    }


    return(
        <AuthContext.Provider value={value}>
            {!loading && children}
        </AuthContext.Provider>
    )
}

export const useAuth = () => {
    return useContext(AuthContext)
}


