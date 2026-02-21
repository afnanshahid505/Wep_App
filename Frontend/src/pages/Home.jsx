import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center px-4">
      <div className="max-w-4xl w-full bg-white rounded-2xl shadow-xl p-10 text-center">

        {/* Badge */}
        <div className="inline-block mb-4 px-4 py-1 rounded-full bg-blue-100 text-blue-700 text-sm font-medium">
          Secure • Fast • Simple
        </div>

        {/* Heading */}
        <h1 className="text-4xl md:text-5xl font-extrabold text-gray-900 mb-4">
          Task Manager App
        </h1>

        {/* Subheading */}
        <p className="text-lg text-gray-600 mb-8 max-w-2xl mx-auto">
          Manage your daily tasks efficiently with secure authentication,
          personalized dashboards, and a clean modern interface.
        </p>

        {/* CTA Buttons */}
        <div className="flex justify-center gap-4 mb-10">
          <Link
            to="/signup"
            className="px-6 py-3 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 transition"
          >
            Get Started
          </Link>

          <Link
            to="/login"
            className="px-6 py-3 border border-gray-300 text-gray-800 rounded-lg font-semibold hover:bg-gray-100 transition"
          >
            Login
          </Link>
        </div>

        {/* Feature Grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 text-left">
          <div className="p-5 rounded-xl bg-gray-50 border">
            <h3 className="font-semibold text-lg mb-2">
               Secure Authentication
            </h3>
            <p className="text-gray-600 text-sm">
              JWT-based login system with password hashing and protected routes.
            </p>
          </div>

          <div className="p-5 rounded-xl bg-gray-50 border">
            <h3 className="font-semibold text-lg mb-2">
               Task Management
            </h3>
            <p className="text-gray-600 text-sm">
              Create, view, and delete tasks seamlessly from your dashboard.
            </p>
          </div>

          <div className="p-5 rounded-xl bg-gray-50 border">
            <h3 className="font-semibold text-lg mb-2">
             Modern Tech Stack
            </h3>
            <p className="text-gray-600 text-sm">
              Built with React, FastAPI, Tailwind CSS, and JWT authentication.
            </p>
          </div>
        </div>

      </div>
    </div>
  );
}

export default Home;