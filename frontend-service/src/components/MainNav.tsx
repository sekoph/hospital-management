import { Link } from "react-router-dom"

const MainNav = () => {
  return (
    <section className="absolute z-20 top-11 left-60">
      <nav className="flex container mx-auto justify-between">
        <ul className="flex-1 justify-center items-center space-x-8">
          <Link to="" className="">Admin Dashboard</Link>
          <Link to="" className="">Manage Patients</Link>
          <Link to="" className="">Manage Doctors</Link>
        </ul>

        {/* <div className="flex justify-end items-end">
          <h1>user</h1>
        </div> */}
      </nav>
    </section>
  )
}

export default MainNav