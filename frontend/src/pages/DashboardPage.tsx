import { useQuery } from '@tanstack/react-query';
import api from '../hooks/useApi';

interface Channel {
  id: number;
  name: string;
  rtsp_url: string;
  enabled: boolean;
}

export default function DashboardPage() {
  const { data } = useQuery<Channel[]>({
    queryKey: ['channels'],
    queryFn: async () => {
      const response = await api.get('/channels');
      return response.data;
    }
  });

  return (
    <section>
      <h2>Сетка каналов</h2>
      <div className="grid">
        {data?.map((channel) => (
          <article key={channel.id}>
            <h3>{channel.name}</h3>
            <p>{channel.rtsp_url}</p>
            <span className={channel.enabled ? 'status-online' : 'status-offline'}>
              {channel.enabled ? 'Активен' : 'Отключен'}
            </span>
          </article>
        )) || <p>Нет сконфигурированных каналов</p>}
      </div>
    </section>
  );
}
