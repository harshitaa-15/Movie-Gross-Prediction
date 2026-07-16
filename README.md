<div align="center">

# Movie Gross Prediction

### End-to-End Machine Learning Project for Predicting Movie Box Office Revenue

<img src="https://media.licdn.com/dms/image/v2/C4D12AQGRvo4AfaTd2Q/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1642587252148?e=2147483647&v=beta&t=HBwScRGPXfENN10cZ2A591eVsq-RhDJ5ngGK5XgO6BQ"
     alt="Movie Gross Prediction"
     width="100%">

</div>

---

## Project Overview

Movie Gross Prediction is an end-to-end Machine Learning project that predicts the estimated box office gross revenue of a movie using historical IMDb movie data.

The project demonstrates the complete data science workflow, including data preprocessing, feature engineering, model development, model evaluation, and deployment using Streamlit. It enables users to estimate a movie's gross revenue based on key attributes such as genre, runtime, IMDb rating, director, and cast information.

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Libraries | Pandas, NumPy, Scikit-learn, Joblib |
| Framework | Streamlit |
| Visualization | Matplotlib, Plotly |
| Development | Jupyter Notebook, Git, GitHub |

---


## Project Structure

```
Movie-Gross-Prediction
│
├── Dataset
│   └── imdb_top_1000.csv
│
├── Image
│   └── boxoffice_image.png
│
├── Model
│   └── movie_model.pkl
│
├── Notebook
│   └── movies-success-prediction.ipynb
│
├── Social media icons
│   ├── csv.png
│   ├── github.png
│   └── linkedin.png
│
├── Video
│   └── movie_video.mp4
│
├── src
│   ├── main.py
│   ├── page_config.py
│   └── sidebar_ui.py
│
├── app.py
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Machine Learning Model

Algorithm Used

- Linear Regression

Model Evaluation

- R² Score: **0.5135**
  
- The input to the model were normalized using StandardScaler.
- The trained model was serialized using Joblib and saved as a `.pkl` file for deployment in the Streamlit application.

---

## Application Workflow

1. Load the dataset
2. Clean and preprocess the data
3. Select relevant features
4. Scale numerical features
5. Train the Linear Regression model
6. Save the trained model
7. Launch the Streamlit application
8. Accept user inputs
9. Predict movie gross revenue

---

## Dataset Description

The dataset for this model is taken from kaggle and can ne found on this link: 'https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows'.

**Data** :-

- `Poster_Link` - Link of the poster that imdb using
- `Series_Title` = Name of the movie
- `Released_Year` - Year at which that movie released
- `Certificate` - Certificate earned by that movie
- `Runtime` - Total runtime of the movie
- `Genre` - Genre of the movie
- `IMDB_Rating` - Rating of the movie at IMDB site
- `Overview` - mini story/ summary
- `Meta_score` - Score earned by the movie
- `Director` - Name of the Director
- `Star1,Star2,Star3,Star4` - Name of the Stars
- `No_of_votes` - Total number of votes
- `Gross` - Money earned by that movie

---

## Data Preprocessing

- We removed NULL values instead of filling them.
- We also Remove the following columns:
   - Poster_Link
   - Overview
- We didn't handle outliers.

---

## Repository Contents

| Folder | Description |
|----------|-------------|
| Dataset | Contains the IMDb dataset used for training |
| Model | Stores the trained Machine Learning model |
| Notebook | Contains exploratory analysis and model development |
| Image | Application images used in the project |
| Video | Demonstration video of the application |
| src | Source code for application components |
| app.py | Main Streamlit application |
| requirements.txt | Project dependencies |

---
## Future Enhancements

- Improve prediction accuracy using ensemble learning models such as Random Forest, XGBoost, and Gradient Boosting.
- Perform hyperparameter tuning.
- Implement automated feature selection.
- Add model explainability using SHAP.
- Deploy the application on Streamlit Community Cloud.
- Compare multiple regression algorithms for performance evaluation.




