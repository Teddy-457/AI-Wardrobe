from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import URL

#връзка с sql
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

#създаване на engine
engine = create_engine(connection_url, echo=True)

#фабрика за създаване на сесии
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Базов клас за всички модели
Base = declarative_base()