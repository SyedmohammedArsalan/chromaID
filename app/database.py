from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Database URL (SQLite creates a file named chromaid.db in your root folder)
SQLALCHEMY_DATABASE_URL = "sqlite:///./chromaid.db"

# 2. Create the SQLAlchemy engine
# (connect_args is strictly required for SQLite in FastAPI to prevent thread issues)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. Create a SessionLocal class for database transactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Create a Base class for our database models
Base = declarative_base()

# --- DATABASE MODELS ---

class UserReportDB(Base):
    __tablename__ = "user_reports"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    season_type = Column(String)
    
    # We use JSON to store the complex day/night palette dictionaries 
    # without needing 50 different columns!
    report_data = Column(JSON) 

# --- DEPENDENCY ---
# We will use this in our routes to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()