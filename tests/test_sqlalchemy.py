from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

connection_url = URL.create(
    "mssql+pyodbc",
    host=r"localhost\SQLEXPRESS",
    database="AI_Wardrobe",
    query={
        "driver": "ODBC Driver 18 for SQL Server",
        "trusted_connection": "yes",
        "TrustServerCertificate": "yes"
    }
)

engine = create_engine(connection_url)

try:
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT DB_NAME()")
        )

        print("Successfully connected!")
        print("Database:", result.scalar_one())

except Exception as error:
    print("Connection failed:")
    print(error)
