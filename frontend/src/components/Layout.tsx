import { Link, useLocation } from 'react-router-dom';
import { ReactNode } from 'react';

const links = [
  { to: '/', label: 'Каналы' },
  { to: '/events', label: 'События' },
  { to: '/search', label: 'Поиск' },
  { to: '/lists', label: 'Списки' },
  { to: '/settings', label: 'Настройки' },
  { to: '/diagnostics', label: 'Диагностика' }
];

export function Layout({ children }: { children: ReactNode }) {
  const location = useLocation();
  return (
    <div className="app-shell">
      <aside>
        <h1>ANPR</h1>
        <nav>
          {links.map((link) => (
            <Link key={link.to} to={link.to} className={location.pathname === link.to ? 'active' : ''}>
              {link.label}
            </Link>
          ))}
        </nav>
      </aside>
      <main>{children}</main>
    </div>
  );
}
