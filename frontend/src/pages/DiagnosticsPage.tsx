import { useQuery } from '@tanstack/react-query';
import api from '../hooks/useApi';

interface Health {
  status: string;
}

export default function DiagnosticsPage() {
  const { data: health } = useQuery<Health>({
    queryKey: ['health'],
    queryFn: async () => {
      const response = await api.get('/diagnostics/health');
      return response.data;
    }
  });

  return (
    <section>
      <h2>Диагностика</h2>
      <p>Статус API: {health?.status ?? 'неизвестно'}</p>
      <p>Метрики Prometheus доступны по пути <code>/metrics</code> сервиса backend.</p>
    </section>
  );
}
