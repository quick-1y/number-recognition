import { useQuery } from '@tanstack/react-query';
import api from '../hooks/useApi';

interface PlateList {
  id: number;
  name: string;
  list_type: string;
  priority: number;
  items: { id: number; pattern: string; comment?: string | null }[];
}

export default function ListsPage() {
  const { data } = useQuery<PlateList[]>({
    queryKey: ['lists'],
    queryFn: async () => {
      const response = await api.get('/lists');
      return response.data;
    }
  });

  return (
    <section>
      <h2>Списки номеров</h2>
      {data?.map((plateList) => (
        <article key={plateList.id}>
          <header>
            <h3>{plateList.name}</h3>
            <span className={`tag tag-${plateList.list_type}`}>{plateList.list_type}</span>
            <small>Приоритет: {plateList.priority}</small>
          </header>
          <ul>
            {plateList.items.map((item) => (
              <li key={item.id}>
                <strong>{item.pattern}</strong>
                {item.comment && <span> — {item.comment}</span>}
              </li>
            ))}
          </ul>
        </article>
      )) || <p>Списки не созданы</p>}
    </section>
  );
}
