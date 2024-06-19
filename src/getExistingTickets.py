import os
import requests

from config import ACCESS_TOKEN,BASE_URL


def getExistingIssues(project_id):
    api_url = f'{BASE_URL}/v4/projects/{project_id}/issues'
    headers = {
        'Content-Type': 'application/json',
        'Private-Token': ACCESS_TOKEN
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch existing issues - Status code: {response.status_code}")
        return []
