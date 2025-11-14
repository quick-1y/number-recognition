export default function SettingsPage() {
  return (
    <section>
      <h2>Настройки платформы</h2>
      <div className="settings-grid">
        <article>
          <h3>Ресурсы обработки</h3>
          <p>Переключение режимов CPU/GPU, количество одновременных каналов.</p>
        </article>
        <article>
          <h3>Шаблоны стран</h3>
          <p>Управление регулярными выражениями для форматов RU, BY, KZ, UA, EU.</p>
        </article>
        <article>
          <h3>Webhooks и API</h3>
          <p>Конфигурация подписок, HMAC секретов, расписаний повторов.</p>
        </article>
        <article>
          <h3>Тревожные выходы</h3>
          <p>Настройка реле камер, режимы замыкания/размыкания, задержки.</p>
        </article>
      </div>
    </section>
  );
}
