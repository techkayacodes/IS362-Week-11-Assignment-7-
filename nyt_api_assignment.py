# Import necessary libraries
import requests
import pandas as pd

# Replace 'your_api_key' with your actual New York Times API key
api_key = 'your_api_key'
# Choose an endpoint from the NYT API documentation. Here we use the Top Stories API as an example.
url = f'https://api.nytimes.com/svc/topstories/v2/home.json?api-key={api_key}'

# Fetch the data from the API
response = requests.get(url)
data = response.json()

# Check if the request was successful
if response.status_code == 200:
    print("Data fetched successfully!")
else:
    print("Failed to fetch data")
    exit()

# Transform the JSON data into a pandas DataFrame
articles = data['results']
df = pd.DataFrame(articles)

# Display the first few rows of the DataFrame
print("DataFrame created from NYT API data:")
print(df.head())

# Save the DataFrame to a CSV file
df.to_csv('nyt_top_stories.csv', index=False)
