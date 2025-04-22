import Header from "@/components/Header"
import { Outlet } from "react-router-dom"

const DoctorLayout = () => {
  return (
    <div className="flex flex-col min-h-screen">
        <Header/>
        <main className="container mx-auto flex-1 py-10">
            <Outlet/>
        </main>
    </div>
  )
}

export default DoctorLayout