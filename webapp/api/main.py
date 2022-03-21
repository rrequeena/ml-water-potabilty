import joblib

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="../templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict/")
async def predict(request: Request, ph: float = Form(...), hardness: float = Form(...),
                solids: float = Form(...), chloramines: float = Form(...),
                sulfate: float = Form(...), conductivity: float = Form(...),
                organic_carbon: float = Form(...), trihalomethanes: float = Form(...),
                turbidity: float = Form(...)):
    
    scaler = joblib.load("models/scaler.save")
    # Normalize data
    data = scaler.transform(
        [[ph, hardness, solids, chloramines, sulfate, conductivity,
        organic_carbon, trihalomethanes, turbidity]]
    )

    # Load Predictive model
    model = joblib.load("models/svc.save")
    # Get predictions
    prediction = model.predict(data)

    positive_title = "The water is potable!"
    positive_img_url = "https://www.snf.co.uk/wp-content/uploads/2017/06/rsz_potabledrinkingwater.jpg"

    negative_title = "The water is not potable, careful!"
    negative_img_url = "https://cdn-reichelt.de/bilder/web/xxl_ws/C180/W-74105.png"

    result = "POTABLE" if prediction[0] == 1 else "NOT POTABLE"
    img_url = positive_img_url if prediction[0] == 1 else negative_img_url
    alert_type = "alert-primary" if prediction[0] == 1 else "alert-danger"
    title = positive_title if prediction[0] == 1 else negative_title


    
    return templates.TemplateResponse("prediction.html", {
        "request": request,
        "alert_type": alert_type,
        "result": result,
        "img_url": img_url,
        "title": title
        })
