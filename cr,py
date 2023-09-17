import requests
import yaml

# Function to call CR minion API and extract Site_id
def get_site_id_from_api(cr_number):
    # Define the CR minion API URL with the CR number as a parameter
    api_url = f"https://api.example.com/cr_minion?cr_number={cr_number}"

    try:
        # Make the API request
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            api_data = response.json()

            # Extract the Site_id from the response
            description = api_data.get("description", "")
            site_id = None

            if "Site_id:" in description:
                site_id = description.split("Site_id:")[1].strip().split("\r\n")[0].strip()

            return site_id
        else:
            print(f"API request failed with status code {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Input CR number from the user
cr_number = input("Enter the CR number: ")

# Call the function to get the Site_id
site_id = get_site_id_from_api(cr_number)

if site_id is not None:
    # Prepare a dictionary for the YAML configuration file
    config_data = {"Site_id": site_id}

    # Save the configuration to a YAML file named after the CR number
    config_file_name = f"{cr_number}.yml"
    with open(config_file_name, "w") as yaml_file:
        yaml.dump(config_data, yaml_file, default_flow_style=False)

    print(f"Site_id {site_id} stored in {config_file_name}")
else:
    print("Failed to retrieve Site_id from the API")
