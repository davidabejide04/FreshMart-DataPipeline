import psycopg2

conn = psycopg2.connect(
    dbname="freshmart_db",
    user="postgres",
    password="#Access@25",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Products (
    ProductID SERIAL PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Price DECIMAL,
    StockQuantity INT
)
""")
conn.commit()


for _, row in df.iterrows():
    cur.execute("""
    INSERT INTO Products (ProductName, Category, Price, StockQuantity)
    VALUES (%s, %s, %s, %s)
    """, (row["ProductName"], row["Category"], row["Price"], row["StockQuantity"]))
conn.commit()