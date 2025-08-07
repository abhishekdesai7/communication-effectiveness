import duckdb

# Connect to local DuckDB file
con = duckdb.connect("data/comm_effectiveness.duckdb")

# Load CSVs into DuckDB tables
result=con.execute("SELECT * FROM customer_feedback LIMIT 10;").fetchall()
print(result)

# Close the connection
con.close()


# import duckdb

# # Connect to the DuckDB file
# con = duckdb.connect("data/comm_effectiveness.duckdb")

# # List tables
# tables = con.execute("SHOW TABLES;").fetchall()
# print(tables)