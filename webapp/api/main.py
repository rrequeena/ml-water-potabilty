import joblib

from fastapi import FastAPI

app = FastAPI()

@app.get("/predict/")
async def predict(ph: float, hardness: float, solids: float,
                    chloramines: float, sulfate: float, conductivity: float,
                    organic_carbon: float, trihalomethanes: float,
                    turbidity: str):
    
    scaler = joblib.load("models/scaler.save")
    # Normalize data
    data = scaler.transform(
        [[ph, hardness, solids, chloramines, sulfate, conductivity,
        organic_carbon, trihalomethanes, turbidity]]
    )

    # Predictive model
    model = joblib.load("models/svc.save")
    prediction = model.predict(data)
    #probabilities = model.predict_proba(data)
    
    return {
        "prediction": int(prediction[0])
        #"probabilities": probabilities
    }
