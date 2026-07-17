import streamlit as st
import numpy as np
import joblib
import plotly.graph_objects as go # Plots
from src.page_config import page_config
from src.main import main_config
from src.sidebar_ui import sidebar_config



page_config()

main_config()

sidebar_config()

#======================================================================================
#                            Model Prediction secition UI
#======================================================================================

inputs = ["Series_Title", "Released_Year", "Certificate", "Runtime", "Genre", "IMDB_Rating", "Meta_score", "Director",
            "Star1", "Star2", "Star3", "Star4", "No_of_votes"]

cols = st.columns(3)

with cols[0]: 
     Series_Title_Values = st.number_input("Series Title", min_value = 0, max_value = 713)
     Released_Year_Values = st.number_input("Released Year", min_value = 1930, max_value = 2019)
     Certificate_Values = st.number_input("Certificate", min_value = 0, max_value = 11)
     Runtime_Values = st.number_input("Runtime", min_value = 72, max_value = 238)

with cols[1]: 
     Genre_Values = st.number_input("Genre", min_value = 0, max_value = 171)
     IMDB_Rating_Values = st.number_input("IMBD Rating", min_value = 6, max_value = 10)
     Meta_score_Values = st.number_input("Meta Score", min_value = 28, max_value = 100)
     Director_Values = st.number_input("Director", min_value = 0, max_value = 401)

with cols[2]: 
     Star1_Values = st.number_input("Star1", min_value = 0, max_value = 471)
     Star2_Values = st.number_input("Star2", min_value = 0, max_value = 598)
     Star3_Values = st.number_input("Star3", min_value = 0, max_value = 625)
     Star4_Values = st.number_input("Star4", min_value = 0, max_value = 670)

No_of_votes_Values = st.number_input("No_of_votes", min_value = 25229, max_value = 2343110)



input_values = [Series_Title_Values, Released_Year_Values, Certificate_Values, Runtime_Values,
                 Genre_Values, IMDB_Rating_Values, Meta_score_Values , Director_Values,
                 Star1_Values,Star2_Values, Star3_Values, Star4_Values, No_of_votes_Values ]

input_values_array = np.array(input_values).reshape(1, -1)

st.markdown("---")

# error handling for proper model loading
try:
    model = joblib.load("model/movie_model.pkl")
    
    # model weights graph

    fig = go.Figure(
            data = [
                go.Bar(
                    x = inputs,
                    y = model.coef_,
                    marker = dict(color = "royalblue")
                )
            ]
        )
    
    st.plotly_chart(fig)
    st.markdown("---")



    if st.button("Predict"):
        preds = model.predict(input_values_array)
        st.success(f"Gross Collection is $ {int(preds[0])}")
      
        avg_gross_value = 78379890
        max_gross_value = 936662225

        if preds[0] < avg_gross_value:
            st.warning("Movie is not Successful👎")
            fig = go.Figure(
                data = [
                go.Bar(
                    x = ["Failure", "average", "maximum"],
                    y = [preds[0], avg_gross_value, max_gross_value],
                    marker = dict(color = ["red", "blue", "orange"])
                )
            ]
            )
            st.plotly_chart(fig)

        else:
            st.success("Movie is Successful👍")
            st.snow()

            fig = go.Figure( 
                data = [
                go.Bar(
                    x = ["average", "Success", "maximum"],
                    y = [avg_gross_value, preds[0], max_gross_value],
                    marker = dict(color = ["blue", "green","orange" ])
                )
            ]
            )
            st.plotly_chart(fig)


except OSError as e:
    st.warning(e)











