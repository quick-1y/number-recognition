import { useQuery } from '@tanstack/react-query';
import api from '../hooks/useApi';

interface Recognition {
  id: number;
  plate_number: string;
  confidence: number;
  created_at: string;
  channel_id: number;
}

export default function EventsPage() {
  const { data } = useQuery<Recognition[]>({
    queryKey: ['events'],
    queryFn: async () => {
      const response = await api.get('/events');
      return response.data;
    }
  });

  return (
    <section>
      <h2>Последние события</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Номер</th>
            <th>Уверенность</th>
            <th>Канал</th>
            <th>Время</th>
          </tr>
        </thead>
        <tbody>
          {data?.map((event) => (
            <tr key={event.id}>
              <td>{event.id}</td>
              <td>{event.plate_number}</td>
              <td>{(event.confidence * 100).toFixed(1)}%</td>
              <td>{event.channel_id}</td>
              <td>{new Date(event.created_at).toLocaleString()}</td>
            </tr>
          )) || (
            <tr>
              <td colSpan={5}>Нет событий</td>
            </tr>
          )}
        </tbody>
      </table>
    </section>
  );
}
