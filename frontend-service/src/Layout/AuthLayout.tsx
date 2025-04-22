import { Outlet } from "react-router-dom"

const AuthLayout = () => {
  return (
    <main className="container mx-auto">
      <Outlet/>
    </main>
  )
}

export default AuthLayout