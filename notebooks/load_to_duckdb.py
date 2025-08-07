import duckdb
import os

# Connect to local DuckDB file
con = duckdb.connect("data/comm_effectiveness.duckdb")

# Load CSVs into DuckDB tables
con.execute("CREATE OR REPLACE TABLE flights AS SELECT * FROM read_csv_auto('data/flights.csv');")
con.execute("CREATE OR REPLACE TABLE notifications_sent AS SELECT * FROM read_csv_auto('data/notifications_sent.csv');")
con.execute("CREATE OR REPLACE TABLE notification_events AS SELECT * FROM read_csv_auto('data/notification_events.csv');")
con.execute("CREATE OR REPLACE TABLE customer_feedback AS SELECT * FROM read_csv_auto('data/customer_feedback.csv');")

print("✅ Data loaded into DuckDB: comm_effectiveness.duckdb")
