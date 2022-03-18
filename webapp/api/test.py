import joblib

scaler = joblib.load("models/scaler.save")

data = [[3.71608007538699,129.42292051494425,18630.057857970347,6.635245883862,
368.51644134980336,592.8853591348523,15.18001311635726,56.32907628451764,4.500656274942408]]

scaled = scaler.transform(data)
print(scaled)

model = joblib.load("models/svc.save")
pred = model.predict(scaled)
print(f"Prediction: {pred[0]}")