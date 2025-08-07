SELECT
  ns.flight_id,
  COUNT(*) AS total_sent,
  SUM(CASE WHEN ne.opened THEN 1 ELSE 0 END) AS total_opened,
  SUM(CASE WHEN ne.clicked THEN 1 ELSE 0 END) AS total_clicked,
  ROUND(100.0 * SUM(CASE WHEN ne.opened THEN 1 ELSE 0 END) / COUNT(*), 2) AS open_rate_pct
FROM main.notifications_sent ns
LEFT JOIN main.notification_events ne
  ON ns.customer_id = ne.customer_id AND ns.flight_id = ne.flight_id
GROUP BY ns.flight_id
