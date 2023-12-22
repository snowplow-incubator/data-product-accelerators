+++
title = "Run Flask app"
weight = 1
post = ""
+++

Run the Flask app with `python flask_app.py` (assuming you are in the /aws_personalize_utilities directory). This will start the app on port 5000. 

There are multiple ways to interact with the app. Depending on which recommender you wish to use you will need to provide the user ID and or item ID, refer to the table below for the full list of recommenders and their required inputs.

#### **Option 1:** 
Make a GET request to the app with Python:
```
import requests
import json

url = "http://localhost:5000/get_recommendations"
user_id = '0000'
recommender = 'customers_who_viewed_x_also_viewed'
item_id = "168f54efd6529951853f254e72f4d47b" # Optional, depending on the recommender you are using

data = {
    "user_id": user_id,
    "recommender": recommender,
    "item_id": item_id
}

response = requests.get(url, params=data)
if response.status_code == 200:
    print(response.json())
else:
    print(response.text)
```

#### **Option 2:** 
Make a GET request to the app with curl:
```
curl -X GET "http://localhost:5000/get_recommendations?user_id=0000&recommender=customers_who_viewed_x_also_viewed&item_id=168f54efd6529951853f254e72f4d47b"
```

#### **Option 3:** 
Navigate to `http://localhost:5000/` in your browser to use the provided form to send a request. 

| ![Request Form](../images/recommendation_flask_ui.png) |
|:--:|
| Request Form |

Which recommenders are available to you will depend on the domain(s) you chose and the dataset types you created. See the below table for more information about each recommender:

| Domain | Recommender | Required dataset types | Optional dataset types | Required input parameters | Optional input parameters |
| ------ | ------ | ------ | ------ | ------ | ------ |
| ECOMMERCE | most_viewed | interactions |  | user_id |  |
| ECOMMERCE | best_sellers | interactions |  | user_id |  |
| ECOMMERCE | frequently_bought_together | interactions |  | item_id |  |
| ECOMMERCE | customers_who_viewed_x_also_viewed | interactions |  | user_id, item_id |  |
| ECOMMERCE | recommended_for_you | interactions | items, users | user_id |  |
| VIDEO_ON_DEMAND | because_you_watched_x | interactions |  | user_id, item_id |  |
| VIDEO_ON_DEMAND | most_popular | interactions |  | user_id |  |
| VIDEO_ON_DEMAND | trending_now | interactions |  |  |  |
| VIDEO_ON_DEMAND | top_picks_for_you | interactions | items, users | user_id |  |
