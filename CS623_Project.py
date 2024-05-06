import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)

try:
    # atomicity
    conn.autocommit = False
    # isolation
    conn.set_isolation_level(3)
    
    # Create a cursor object
    cur = conn.cursor()

    # Add a new depot to the Depot table
    cur.execute("""
        INSERT INTO Depot (#dep, addr, volume)
        VALUES ('d100', 'Chicago', 100)
    """)

    # Insert the new product into the Stock table for the newly added depot
    cur.execute("""
        INSERT INTO Stock (#prod, #dep, quantity)
        VALUES ('p1', 'd100', 100)
    """)

    # Commit the transaction
    conn.commit()

except (Exception, psycopg2.DatabaseError) as e:
    # Rollback the transaction if there is an error
    conn.rollback()
    print(f"Error: {e}")

finally:
    if conn:
        # close the connection
        cur.close()
        conn.close()
        print("PostgreSQL closed")

print("End")
