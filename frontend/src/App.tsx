import { Route, Routes } from 'react-router-dom';
import { Layout } from './components/Layout';
import DashboardPage from './pages/DashboardPage';
import EventsPage from './pages/EventsPage';
import ListsPage from './pages/ListsPage';
import SettingsPage from './pages/SettingsPage';
import SearchPage from './pages/SearchPage';
import DiagnosticsPage from './pages/DiagnosticsPage';

function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<DashboardPage />} />
        <Route path="/events" element={<EventsPage />} />
        <Route path="/lists" element={<ListsPage />} />
        <Route path="/search" element={<SearchPage />} />
        <Route path="/settings" element={<SettingsPage />} />
        <Route path="/diagnostics" element={<DiagnosticsPage />} />
      </Routes>
    </Layout>
  );
}

export default App;
