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
        'Sepal length': sepal_length,
        'Sepal width': sepal_width,
        'Petal length': petal_length,
        'Petal width': petal_width
    }
    features = pd.DataFrame(data, index=['Parameters'])
    return features


# Page Config ...
st.set_page_config(layout="wide", page_title="Flower Prediction", page_icon="🎴")

utils.heading(title='Simple Iris Flower Prediction',
              sub_title='This app makes predictions about the <b>type</b> of <b style="color:#87CEEB">Iris</b> '
                        'flower.<br>Use the the <b '
                        'style="color:#87CEEB">sliders</b> on the '
                        'sidebar to select the input parameters.',
              title_color='lightblue',
              top=50
              )

st.sidebar.header('User Input Parameters')

# Model fitting and Prediction ...

df = user_input_features()
iris = datasets.load_iris()
X = iris.data
y = iris.target

model = rfc()
model.fit(X, y)

prediction = model.predict(df)
prediction_prob = pd.DataFrame(model.predict_proba(df), columns=iris.target_names, index=["Probability (in %)"])
prediction_prob = prediction_prob.rename(columns={'setosa': 'Setosa',
                                                  'versicolor': 'Versicolor',
                                                  'virginica': 'Virginica'})
prediction_prob = prediction_prob.apply(lambda p: round(p * 100, 2), axis=1)

labels = pd.DataFrame({"Species Name": iris.target_names})
labels["Species Name"] = labels["Species Name"].apply(lambda x: x.title())
labels.reset_index(inplace=True)
labels.set_index('index', inplace=True)

# Page UI ...

utils.line_break()
col1, padding, col2 = st.columns((12, 4, 12), gap="small")

with col1:
    st.subheader("User Input Parameters")
    st.write(df)

    st.subheader("Class **labels** and their corresponding **indices**")
    st.write(labels)

with col2:
    st.subheader("Prediction")
    st.dataframe(pd.DataFrame(labels["Species Name"][prediction], columns=["Species Name"]))

    st.subheader("Prediction Probability")
    st.dataframe(prediction_prob)
