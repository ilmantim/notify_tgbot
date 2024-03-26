import os
import requests
import json
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()
    devman_token = os.environ["DEVMAN_TOKEN"]

    script_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(script_dir, "checklist.json")

    api_url = 'https://dvmn.org/api/user_reviews/'
    headers = {
        'Authorization': devman_token
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        checklist = response.json()

        with open(save_path, "w", encoding="utf-8") as file:
            json.dump(checklist, file, ensure_ascii=False, indent=4)

        print(f"Checklist saved to {save_path}")
    else:
        print(f"Failed to retrieve checklist. Status code: {response.status_code}")
