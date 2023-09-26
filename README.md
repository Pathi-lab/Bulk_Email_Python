# Bulk_Email_Python
Using this python script you can send bulk email with body template
import requests

# Define your authentication token
auth_token = 'YOUR_AUTH_TOKEN_HERE'

# Define the API endpoint URL
api_url = 'https://api.juniper.com/org/details'

# Get the site name from user input
site_name_to_search = input("Enter the site name you want to search for: ")

# Define headers with authentication token
headers = {
    'Authorization': f'Bearer {auth_token}',
    'Content-Type': 'application/json'
}

# Define the query parameters
params = {
    'site_name': site_name_to_search
}

# Make the API request
response = requests.get(api_url, headers=headers, params=params)

try:
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response into a list of dictionaries
        data_list = response.json()

        # Iterate through the list and find the site ID for the specified site name
        for item in data_list:
            if item['name'] == site_name_to_search:
                site_id = item.get('id')
                if site_id:
                    print(f"Site ID for {site_name_to_search}: {site_id}")
                else:
                    print(f"Site name '{site_name_to_search}' found, but no Site ID.")
                break  # Exit the loop after finding the site
        else:
            print(f"Site name '{site_name_to_search}' not found in the response.")
    else:
        print(f"API request failed with status code {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"An error occurred: {e}")
