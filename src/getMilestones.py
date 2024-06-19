
import requests

from config import ACCESS_TOKEN,BASE_URL


def getMilestones(project_id):
        # Headers for API request
    headers = {
        'Content-Type': 'application/json',
        'Private-Token': ACCESS_TOKEN
    }
    
    api_url_milestones = f'{BASE_URL}/v4/projects/{project_id}/milestones'
    response = requests.get(api_url_milestones, headers=headers)
    if response.status_code == 200:
        milestones_data = response.json()
        milestone_mapping = {}
        for milestone in milestones_data:
            milestone_mapping[milestone['title']] = milestone['id']
        return milestone_mapping
    else:
        print(f"Failed to fetch milestones - Status code: {response.status_code}")
        return None

