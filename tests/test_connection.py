import pyodbc

connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=AI_Wardrobe;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

try:
    connection = pyodbc.connect(connection_string)

    print("Success!")

    cursor = connection.cursor()
    cursor.execute("SELECT DB_NAME(), @@SERVERNAME")

    result = cursor.fetchone()

    print("Database:", result[0])
    print("Server:", result[1])

    connection.close()

except pyodbc.Error as error:
    print("Connection failed:")
    print(error)
