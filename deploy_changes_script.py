import mysql.connector

# MySQL Configuration
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""  # Leave empty if no password is set
DB_NAME = "prog8850_assignment"

# Connect to MySQL
try:
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    cursor = connection.cursor()

    # Define the SQL command
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Employees (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(255),
        Department VARCHAR(255),
        Salary DECIMAL(10, 2)
    );
    """

    cursor.execute(create_table_query)
    connection.commit()

    print("Table 'Employees' created successfully.")

except mysql.connector.Error as error:
    print(f"Failed to create table: {error}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
