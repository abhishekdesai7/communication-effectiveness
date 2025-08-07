SELECT
  ns.customer_id,
  ns.flight_id,
  ns.notif_type,
  ns.notification_sent_at
FROM {{ source('raw','notifications_sent') }} ns
LEFT JOIN {{ source('raw','notification_events') }} ne
  ON ns.customer_id = ne.customer_id AND ns.flight_id = ne.flight_id
WHERE ne.opened IS FALSE OR ne.opened IS NULL
