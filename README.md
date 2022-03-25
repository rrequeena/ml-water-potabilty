# Water Potability Predictive Model: From EDA to ML deployment.
![Water Potability Model](https://user-images.githubusercontent.com/64110737/159376128-8c24170c-7013-425e-b0ce-5934f6be77c3.png)
Water is our best resource on this planet, nature in general. Doing projects based on improving things to take care of our environment can help create exciting things to help our world.

Nowadays, we can create devices that support machine learning models; the primary goal of this project is to train a model which, based on some values, can tell us if the water is potable or not.

## Try the model
If you want to try the model without any download, click on this [URL](https://water-potability-model.herokuapp.com) or scan the QR, and you will get to a webpage where you can write your data and get the prediction result.

<p align="center">
  <img width="200" height="200" src="https://user-images.githubusercontent.com/64110737/159400129-8c7094b7-19cc-4139-8679-ac7633243481.png">
</p>

### Data to enter

**[ pH ]:** It's a parameter to evaluate the acid–base balance of water. It is also the indicator of acidic or alkaline condition of water status. Normal range are from 0 to 14.

**[ Hardness ]:** Hardness is mainly caused by calcium and magnesium salts. The length of time water is in contact with hardness producing material helps determine how much hardness there is in raw water.

**[ Solids ]:** Total dissolved solids - TDS. You must write your value in mg/L

**[ Chloramines ]:** Chloramines are most commonly formed when ammonia is added to chlorine to treat drinking water. Up to 4 mg/L

**[ Sulfates ]:** Sulfates are naturally occurring substances that are found in minerals, soil, and rocks. Desirable range [3 - 30] mg/L

**[ Conductivity ]:** Pure water is not a good conductor of electric current rather’s a good insulator. EC value should not exceeded 400 μS/cm

**[ Organic Carbon ]:** Total Organic Carbon (TOC). For drinking water < 2 mg/L

**[ Trihalomethanes ]_** THMs are chemicals which may be found in water treated with chlorine. Up to 80 ppm for drinking water.

**[ Turbidity ]:** Turbidity of water depends on the quantity of solid matter present in the suspended state. WHO recommended 5.00 NTU for drinking water

## Repository content

On this repository, you can find all the files used to develop this project, from Jupyter Notebooks for Data Analysis to the FastAPI code used on deployment.

### Data folder

The original dataset from [Kaggle](https://www.kaggle.com/adityakadiwal/water-potability) and the cleaned data, both as .csv files.

### Models 

After training the machine learning model and deploying it, the model must be saved into files that will be loaded using the python _joblib_ package

### FastAPI code
In the "webapp" folder, you can find all the code used to deploy the model with FastAPI at the backend and the HTML files used in the frontend.

### Jupyter notebooks
The project was divided into three jupyter notebooks to get the steps to build the model more organized.
- **1. Data Cleaning.ipynb** is where missing values were treated.
- **2. Exploratory Data Analysis.ipynb** contains all the code that was used to make EDA.
- **3. Modeling.ipynb** was used for the final part of the project, train the machine learning model.

### Project Requirements
Before running the project locally, you have to install all the dependencies; the requirements.txt file has all the packages used on the project. You can install all of it using pip: `pip install -r requirements.txt`
