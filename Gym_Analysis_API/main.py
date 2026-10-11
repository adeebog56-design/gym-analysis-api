# Importing requered modules

from sqlalchemy import create_engine,text
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
import joblib
import pandas as pd

from database import engine, gc

class ResultResponse(BaseModel):
   member_id : int                        
   age : int                      
   gender : str                   
   membership_type : str           
   workout_type : str              
   workout_duration_minutes : int
   calories_burned : int  

model = joblib.load("Models/Gym_Logestic_Regression.pkl")

app = FastAPI()

@app.get("/show")
def show (connection : Session = Depends(gc)):

    result = connection.execute(text("SELECT * FROM gym_members"))

    display = []

    for row in result:
      display.append(dict(row._mapping))

    return display

@app.post("/predict")
def getting_and_saving(data:ResultResponse,connection : Session = Depends(gc)):
        
        query = text(""" INSERT INTO new_members ( member_id, age, gender, membership_type, workout_type, workout_duration_minutes, calories_burned )
                 VALUES ( :member_id, :age, :gender, :membership_type, :workout_type, :workout_duration_minutes, :calories_burned ) """)

        connection.execute(query, data.model_dump())
        
        input_data = pd.DataFrame([data.model_dump()])

        input_data = input_data.drop(columns=["member_id"])

        prediction = int(model.predict(input_data)[0])

        querry2 = text("""INSERT INTO predictions (member_id,predicted_attendance_score)
                          VALUES (:member_id, :predicted_attendance_score)""")

        connection.execute(querry2, {"member_id" : data.member_id,
                                     "predicted_attendance_score" : prediction})

        connection.commit()

        return{
            "member_id" : data.member_id,
            "predicted_attendance_score" : prediction
        }

@app.get("/predictions")
def showing_predictions(connection : Session = Depends(gc)):
        result = connection.execute(text("SELECT * FROM predictions"))

        display = []

        for row in result:
             display.append(dict(row._mapping))

        return display

@app.get("/new-members")
def showing_new_members(connection : Session = Depends(gc)):
        result = connection.execute(text("SELECT * FROM new_members"))

        display = []

        for row in result:
             display.append(dict(row._mapping))

        return display