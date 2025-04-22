import MobileNav from "./MobileNav"
import MainNav from "./MainNav"

const Header = () => {
  return (
    <header className="bg-white shadow p-10">
      <div className="container mx-auto flex justify-between items-center">
        <h1 className="text-xl font-bold text-gray-900 -tracking-tight">Hosi</h1>
      </div>
      <div className="md:hidden">
        <MobileNav/>
      </div>
      <div className="hidden md:block">
        <MainNav/>
      </div>
    </header>
  )
}

export default Header