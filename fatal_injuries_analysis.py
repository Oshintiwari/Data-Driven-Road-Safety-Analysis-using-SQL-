import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Dataset
file_path = "fatal_occupational_injuries.csv"
df = pd.read_csv(file_path)

# Step 2: Create SQLite Database
conn = sqlite3.connect("workplace_safety.db")
df.to_sql("fatalities", conn, if_exists="replace", index=False)

# Step 3: SQL Queries for Analysis
# Query 1: Number of Fatalities Per Year
query1 = """
SELECT `Year`, COUNT(*) as Fatalities
FROM fatalities
GROUP BY `Year`
ORDER BY `Year`;
"""
result1 = pd.read_sql_query(query1, conn)

# Query 2: Top 5 Causes of Fatalities
query2 = """
SELECT `Cause`, COUNT(*) as Fatalities
FROM fatalities
GROUP BY `Cause`
ORDER BY Fatalities DESC
LIMIT 5;
"""
result2 = pd.read_sql_query(query2, conn)

# Query 3: Fatalities by Industry
query3 = """
SELECT `Industry`, COUNT(*) as Fatalities
FROM fatalities
GROUP BY `Industry`
ORDER BY Fatalities DESC
LIMIT 5;
"""
result3 = pd.read_sql_query(query3, conn)

# Step 4: Visualization
# Plot Fatalities Per Year
plt.figure(figsize=(10, 6))
plt.plot(result1["Year"], result1["Fatalities"], marker="o", color="blue")
plt.title("Number of Fatalities Per Year", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Fatalities", fontsize=12)
plt.grid(True)
plt.show()

# Plot Top 5 Causes of Fatalities
plt.figure(figsize=(10, 6))
plt.bar(result2["Cause"], result2["Fatalities"], color="orange")
plt.title("Top 5 Causes of Fatalities", fontsize=14)
plt.xlabel("Cause", fontsize=12)
plt.ylabel("Fatalities", fontsize=12)
plt.xticks(rotation=45)
plt.show()

# Plot Fatalities by Industry
plt.figure(figsize=(10, 6))
plt.bar(result3["Industry"], result3["Fatalities"], color="green")
plt.title("Fatalities by Industry", fontsize=14)
plt.xlabel("Industry", fontsize=12)
plt.ylabel("Fatalities", fontsize=12)
plt.xticks(rotation=45)
plt.show()

# Step 5: Close Connection
conn.close()
