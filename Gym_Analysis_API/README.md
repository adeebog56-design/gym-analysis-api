# Gym Analysis API

An end-to-end Machine Learning API that integrates a trained classification model with FastAPI and an SQLite database to predict gym members' attendance status.

## About the Project

This is a skill-based project focused on demonstrating practical Machine Learning integration, REST API development, and database management.

The project uses a gym membership dataset sourced from Kaggle. Its main goal is to connect a trained ML model to a working API rather than achieve high prediction accuracy.

## Technologies Used

* Python
* FastAPI and Pydantic
* SQLAlchemy and SQLite
* Pandas
* Scikit-learn
* Joblib
* Uvicorn

## Machine Learning Model

The project uses a Logistic Regression pipeline with OneHotEncoder, StandardScaler, and ColumnTransformer.

**Input features:**

* Age
* Gender
* Membership Type
* Workout Type
* Workout Duration
* Calories Burned

**Observed accuracy:** Approximately 50%.

The model's performance is limited, so its predictions are experimental and should not be treated as reliable real-world forecasts.

## Database

The SQLite database contains three tables:

* `gym_members` — Original dataset records.
* `new_members` — Members submitted through the API.
* `predictions` — Predicted attendance classes and corresponding member IDs.

## API Endpoints

| Method | Endpoint       | Description                                   |
| ------ | -------------- | --------------------------------------------- |
| GET    | `/show`        | Retrieves original gym member records.        |
| POST   | `/predict`     | Saves member data and generates a prediction. |
| GET    | `/predictions` | Retrieves saved predictions.                  |
| GET    | `/new-members` | Retrieves newly submitted members.            |

Interactive API documentation is available at `/docs` when the server is running.

## Installation

**1. Clone the repository**

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Gym_Analysis_API
```

**2. Create and activate a virtual environment**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the API**

```bash
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/docs` to test the endpoints.

Ensure the required model file and database are available at the paths configured in the code.

## Dataset

Source: Kaggle

Dataset link: Add the original Kaggle dataset URL here.

## Future Improvements

* Improve model accuracy.
* Add better error handling and input validation.
* Add automated API tests.
* Resolve model-version compatibility warnings.
* Deploy the API online.

## Limitations

This is a learning and portfolio project, not a production-ready gym management system. Its current model accuracy is approximately 50%, and its predictions have limited practical reliability.

## Author

**Aiden**

Student developer interested in Machine Learning, Python, and backend development.
