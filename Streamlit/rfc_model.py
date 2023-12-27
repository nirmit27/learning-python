import pandas as pd
import streamlit as st
import sklearn.datasets as datasets
from sklearn.ensemble import RandomForestClassifier as rfc

# Utility functions that I made ...
import streamlit_utils.utils as utils


def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)  # lower limit, upper limit, default value
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width
    }
    features = pd.DataFrame(data, index=[0])
    return features


st.set_page_config(page_title="Flower Prediction", page_icon="🎴")

utils.heading(title='Simple Iris Flower Prediction',
              sub_title='This app makes predictions about the <b>type</b> of <b style="color:blue">Iris</b> '
                        'flower.',
              title_color='lightblue'
              )

utils.line_break(2)

st.sidebar.header('User Input Parameters')
df = user_input_features()

st.subheader("User Input Parameters")
st.write(df)

# Model fitting and Prediction ...

iris = datasets.load_iris()
X = iris.data
y = iris.target
names = iris.target_names

model = rfc()
model.fit(X, y)

prediction = model.predict(df)
prediction_prob = pd.DataFrame(model.predict_proba(df), index=["Probability (in %)"])
prediction_prob = prediction_prob.rename(columns={0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'})
prediction_prob = (prediction_prob * 100).astype('int64')

labels = pd.DataFrame({"Flower Name": iris.target_names})
labels["Flower Name"] = labels["Flower Name"].apply(lambda x: x.title())

# Page UI ...

st.subheader("Class **labels** and their corresponding **indices**")
st.write(labels)

st.subheader("Prediction")
st.dataframe(pd.DataFrame(labels["Flower Name"][prediction], columns=["Flower Name"]))

st.subheader("Prediction Probability")
st.dataframe(prediction_prob)
