import joblib

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict/")
async def predict(request: Request, ph: float = Form(...), hardness: float = Form(...),
                solids: float = Form(...), chloramines: float = Form(...),
                sulfate: float = Form(...), conductivity: float = Form(...),
                organic_carbon: float = Form(...), trihalomethanes: float = Form(...),
                turbidity: float = Form(...)):

    message = "Based on the data that you wrote before, your water is: "
    
    data = [ph, hardness, solids, chloramines, sulfate, conductivity,
        organic_carbon, trihalomethanes, turbidity]
    # Check if all the fields are zero
    all_zero = 1
    for d in data:
        if d != 0:
            all_zero = 0
    if all_zero == 1:
        return templates.TemplateResponse("prediction.html", {
            "request": request,
            "alert_type": "alert-danger",
            "result": "Wait! 🤔 It seems like you fill all the data with zeros. Try again!",
            "img_url": "https://www.eucim.es/wp-content/uploads/2019/08/2378651-1500x1500-785x394.jpg",
            "title": "All data is zero"
            })
    # Load a model to normalize data
    scaler = joblib.load("models/scaler.save")
    # Normalize data
    norm_data = scaler.transform([data])
    print("\n\n", data, "\n\n")
    # Load Predictive model
    model = joblib.load("models/svc.save")
    # Get predictions
    prediction = model.predict(norm_data)
    # Values to take on templates based in the prediction value
    positive_title = "The water is potable!"
    positive_img_url = "https://www.snf.co.uk/wp-content/uploads/2017/06/rsz_potabledrinkingwater.jpg"

    negative_title = "The water is not potable, careful!"
    negative_img_url = "https://cdn-reichelt.de/bilder/web/xxl_ws/C180/W-74105.png"
    # Set the variables to set to the templates
    result = message + "POTABLE" if prediction[0] == 1 else message + "NOT POTABLE"
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
