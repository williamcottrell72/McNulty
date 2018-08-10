# Kickstarting A**!

## **Project Summary**:

### Goals
  1.  To determine when, where, and which types of kickstarter campaigns are likely to be successfully funded.
  2. Develop a predictive model to compute probability of successfully getting funded.
  3. Make a flask app to serve the model to the web.

### Project Design

The steps used in this project are as follows:

  1. Download some datasets online, from Kaggle and other places.
  2. Clean data, convert categorical variables to numbers.
  3. Create visualizations of spatial distribution of campaigns using plotly and geopandas.
  3. Scan over models, choose best model based on cross-val auc.
  4. Analyze, best models more carefully with grid search cv, optimizing for accuracy.
  5. Pick best model, pickle.
  6. Make flask app using best model!


### Tools
  1. sklearn
  2. plotly, geopandas
  3. gmaps api
  4. flask

### Data

Our data consisted of one set of 45,000 completed campaigns as well as a second set of 300,000 campaigns, including both completed and ongoing campaigns.  I primarily focused on the former since the learning curve was already saturating on this set.  The relevant features and target variables are:

X: category, location, goal, funded date, number of levels, starting date.
y: status=success/fail.

### Algorithms

Various standard sklearn classifiers such as Random Forest, ADABooster, Logistic Regression, KNN etc were all used.  For metrics we used the cross-val-score with objective function determined by accuracy.

### Challenges and Solutions

  1. Many, many categorical variables such as 'location'.  There are too many to binarize effectively.  Instead of binarizing, we will convert 'cities' to 'population' and 'population density'.  In order to do this some additional webscraping was necessary in order to get the required data on a sufficiently large set of cities.

  2.  Tableau Public is not available for Ubuntu so some additional work was needed to make an interactive map. In order to plot the city location we needed lattitude and longitude for each city.  This was found using the google maps api.  The coordinates of each city were then fed into both geopandas and plotly.

  3. For the categories we convert these to a 'popularity' variable which is defined as the percentage of projects in a given category.  (These methods where compared to standard binarizing and turned out to be better.)



### Flask App:

https://dry-bayou-22893.herokuapp.com/
