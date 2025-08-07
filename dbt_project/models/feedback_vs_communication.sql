SELECT
  f.flight_id,
  COUNT(DISTINCT f.customer_id) AS total_feedbacks,
  COUNT(DISTINCT m.customer_id) AS missed_customers
FROM {{ source('raw','customer_feedback') }} f
LEFT JOIN {{ ref('missed_communications') }} m
  ON f.customer_id = m.customer_id AND f.flight_id = m.flight_id
GROUP BY f.flight_id
