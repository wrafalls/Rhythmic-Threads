import Logo from '../../public/webSystemLogo.png'
import Cart from '../../public/icons/cart.png'
const AuthNavbar = () => {
  return (
    <div className="navbar  px-[70px] bg-white">
  <div className="">
    <div className="dropdown">
      <div tabIndex={0} role="button" className="btn btn-ghost lg:hidden">
      </div>

    </div>

  </div>
  <div className="navbar-center hidden lg:flex space-x-[24px]">
  <img src={Logo} className='h-[4rem] w-[4rem]'/>
  <label className="input input-bordered flex w-[500px] items-center gap-2">
  <input type="text" className="grow" placeholder="Search" />
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" className="w-4 h-4 opacity-70"><path fillRule="evenodd" d="M9.965 11.026a5 5 0 1 1 1.06-1.06l2.755 2.754a.75.75 0 1 1-1.06 1.06l-2.755-2.754ZM10.5 7a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0Z" clipRule="evenodd" /></svg>
</label>
  </div>
  <div className="navbar-end space-x-5">
    <a className="btn">LOGIN</a>
    <button className="btn text-white" style={{ backgroundColor: "#F68347" }}>SIGN UP</button>
  </div>
</div>
  )
}

export default AuthNavbar
