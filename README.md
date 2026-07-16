# Movie Prediction

This project aims to predict the success of the movie on the box office.The success of the movie is determine on the basis of its gross collection.

<div align="center">
  <img src= "https://media.licdn.com/dms/image/v2/C4D12AQGRvo4AfaTd2Q/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1642587252148?e=2147483647&v=beta&t=HBwScRGPXfENN10cZ2A591eVsq-RhDJ5ngGK5XgO6BQ" width= auto/>
</div>  

## About Model

- The model is trained using LinearRegression and having r2 score of 0.5135.
- The input to the model were normalized using StandardScaler.
- The model is saved in the format `.pkl`.

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

## Data Preprocessing

- We removed NULL values instead of filling them.
- We also Remove the following columns:
   - Poster_Link
   - Overview
- We didn't handle outliers.
