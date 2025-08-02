import React from 'react';

const Sidebar: React.FC = () => {
  const menuItems = [
    { name: 'Dashboard', href: '/', icon: '📊' },
    { name: 'Projects', href: '/projects', icon: '📁' },
    { name: 'Data Import', href: '/data-import', icon: '📥' },
    { name: 'Modeling', href: '/modeling', icon: '📈' },
    { name: 'Scenarios', href: '/scenarios', icon: '🔄' },
    { name: 'Reports', href: '/reports', icon: '📋' },
    { name: 'Collaboration', href: '/collaboration', icon: '👥' },
    { name: 'Admin', href: '/admin', icon: '⚙️' }
  ];

  return (
    <aside className="w-64 bg-white shadow-sm border-r border-gray-200 min-h-screen">
      <div className="p-4">
        <h2 className="text-lg font-semibold text-gray-900 mb-4">Menu</h2>
        <nav className="space-y-2">
          {menuItems.map((item) => (
            <a
              key={item.name}
              href={item.href}
              className="flex items-center px-3 py-2 text-gray-700 hover:bg-gray-100 hover:text-gray-900 rounded-md transition-colors"
            >
              <span className="mr-3">{item.icon}</span>
              <span className="text-sm font-medium">{item.name}</span>
            </a>
          ))}
        </nav>
      </div>
    </aside>
  );
};

export default Sidebar; 