import { Link, useLocation, useNavigate } from "react-router-dom";

export default function PublicNavbar() {
  const navigate = useNavigate();
  const location = useLocation();

  const goHome = () => {
    if (location.pathname !== "/") {
      navigate("/");
      return;
    }

    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const scrollToSection = (id) => {
    if (location.pathname !== "/") {
      navigate("/");
      setTimeout(() => {
        document.getElementById(id)?.scrollIntoView({ behavior: "smooth" });
      }, 100);
      return;
    }

    document.getElementById(id)?.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <nav className="sticky top-0 z-50 flex items-center justify-between border-b bg-white px-6 py-4">
      <button
        type="button"
        onClick={goHome}
        className="text-xl font-bold tracking-normal"
      >
        ALGO
      </button>

      <div className="flex items-center space-x-6">
        <button type="button" onClick={goHome} className="hover:text-gray-600">
          Home
        </button>

        <button
          type="button"
          onClick={() => scrollToSection("features")}
          className="hover:text-gray-600"
        >
          Features
        </button>

        <button
          type="button"
          onClick={() => scrollToSection("about")}
          className="hover:text-gray-600"
        >
          About
        </button>

        <button
          type="button"
          onClick={() => scrollToSection("contact")}
          className="hover:text-gray-600"
        >
          Contact
        </button>

        <Link to="/login" className="hover:text-gray-600">
          Login
        </Link>

        <Link
          to="/register"
          className="rounded-lg bg-black px-4 py-2 text-white hover:bg-gray-800"
        >
          Sign Up
        </Link>
      </div>
    </nav>
  );
}
