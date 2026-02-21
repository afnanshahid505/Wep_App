import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="min-h-screen flex flex-col justify-center items-center bg-gray-100 px-4">
      
      {/* App Title */}
      <h1 className="text-4xl font-bold text-gray-800 mb-4">
        Task Manager App
      </h1>

      {/* Subtitle */}
      <p className="text-lg text-gray-600 mb-8 text-center max-w-xl">
        Manage your tasks efficiently with secure authentication and a
        personalized dashboard.
      </p>

      {/* Buttons */}
      <div className="flex gap-4">
        <Link
          to="/signup"
          className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
        >
          Sign Up
        </Link>

        <Link
          to="/login"
          className="px-6 py-2 bg-gray-800 text-white rounded-lg hover:bg-gray-900 transition"
        >
          Login
        </Link>
      </div>

    </div>
  );
}

export default Home;