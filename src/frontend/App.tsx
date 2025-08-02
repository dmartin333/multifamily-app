import React from 'react';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';

const App: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Navbar */}
      <Navbar />
      
      <div className="flex">
        {/* Sidebar */}
        <Sidebar />
        
        {/* Main Content Area */}
        <main className="flex-1 p-6">
          <div className="max-w-7xl mx-auto">
            <h1 className="text-3xl font-bold text-gray-900 mb-6">
              Multifamily Underwriting Dashboard
            </h1>
            <div className="bg-white rounded-lg shadow p-6">
              <p className="text-gray-600">
                Welcome to the Multifamily Underwriting SaaS platform. 
                Use the navigation above and sidebar to access different modules.
              </p>
            </div>
          </div>
        </main>
      </div>
    </div>
  );
};

export default App; 