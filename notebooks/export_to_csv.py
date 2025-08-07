import duckdb
import pandas as pd
import os

# Connect to DuckDB
con = duckdb.connect("data/comm_effectiveness.duckdb")

# Output folder
output_dir = "exports"
os.makedirs(output_dir, exist_ok=True)

# Queries to export
queries = {
    "notifications_summary": "SELECT * FROM notifications_summary",
    "missed_communications": "SELECT * FROM missed_communications",
    "feedback_vs_communication": "SELECT * FROM feedback_vs_communication"
}

# Export each query as CSV
for name, query in queries.items():
    df = con.execute(query).fetchdf()
    file_path = os.path.join(output_dir, f"{name}.csv")
    df.to_csv(file_path, index=False)

print("✅ CSVs exported for Apple Numbers.")
