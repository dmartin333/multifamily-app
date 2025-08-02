import React from 'react';

const Navbar: React.FC = () => {
  const navItems = [
    { name: 'Projects', href: '/projects' },
    { name: 'Data Import', href: '/data-import' },
    { name: 'Modeling', href: '/modeling' },
    { name: 'Scenarios', href: '/scenarios' },
    { name: 'Reports', href: '/reports' },
    { name: 'Collaboration', href: '/collaboration' },
    { name: 'Admin', href: '/admin' }
  ];

  return (
    <nav className="bg-white shadow-sm border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          {/* Logo */}
          <div className="flex items-center">
            <div className="flex-shrink-0">
              <h1 className="text-xl font-bold text-gray-900">
                MF Underwriting
              </h1>
            </div>
          </div>

          {/* Navigation Links */}
          <div className="hidden md:flex items-center space-x-8">
            {navItems.map((item) => (
              <a
                key={item.name}
                href={item.href}
                className="text-gray-700 hover:text-gray-900 px-3 py-2 rounded-md text-sm font-medium transition-colors"
              >
                {item.name}
              </a>
            ))}
          </div>

          {/* User Menu */}
          <div className="flex items-center">
            <div className="ml-3 relative">
              <div className="flex items-center space-x-4">
                <span className="text-gray-700 text-sm">User</span>
                <div className="w-8 h-8 bg-gray-300 rounded-full"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar; 