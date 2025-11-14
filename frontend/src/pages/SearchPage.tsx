import { FormEvent, useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import api from '../hooks/useApi';

interface Recognition {
  id: number;
  plate_number: string;
  created_at: string;
}

export default function SearchPage() {
  const [query, setQuery] = useState('');
  const { data, refetch, isFetching } = useQuery<Recognition[]>({
    queryKey: ['search', query],
    queryFn: async () => {
      const response = await api.get('/events', { params: { q: query } });
      return response.data;
    },
    enabled: false
  });

  const onSubmit = (event: FormEvent) => {
    event.preventDefault();
    void refetch();
  };

  return (
    <section>
      <h2>Поиск по номеру</h2>
      <form onSubmit={onSubmit} className="search-form">
        <input value={query} onChange={(event) => setQuery(event.target.value)} placeholder="A123BC" />
        <button type="submit" disabled={isFetching}>
          Найти
        </button>
      </form>
      <ul>
        {data?.map((item) => (
          <li key={item.id}>
            <strong>{item.plate_number}</strong> — {new Date(item.created_at).toLocaleString()}
          </li>
        )) || <li>Результаты отсутствуют</li>}
      </ul>
    </section>
  );
}
