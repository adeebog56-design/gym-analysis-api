from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import text

DATABASE_URL = "sqlite:///./gym_databse.db"

engine = create_engine(DATABASE_URL)

def gc():
    with Session(engine) as connection:
        yield connection

def create_tables():
    with engine.begin() as connection:

        connection.execute(text("""
            CREATE TABLE IF NOT EXISTS new_members (
                member_id INTEGER,
                age INTEGER,
                gender TEXT,
                membership_type TEXT,
                workout_type TEXT,
                workout_duration_minutes INTEGER,
                calories_burned INTEGER
            )
        """))

        connection.execute(text("""
            CREATE TABLE IF NOT EXISTS predictions (
                member_id INTEGER,
                predicted_attendance_score INTEGER
            )
        """))

create_tables()