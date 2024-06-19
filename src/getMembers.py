import requests

from config import ACCESS_TOKEN,BASE_URL



def getMembers(project_id): 
  api_url = f'{BASE_URL}/v4/projects/{project_id}/members'

  # Headers for API request
  headers = {
      'Content-Type': 'application/json',
      'Private-Token': ACCESS_TOKEN
  }

  # List to store user IDs and usernames
  project_members = []

  # API request to get members of the specified project
  response = requests.get(api_url, headers=headers)

  if response.status_code == 200:
      members_data = response.json()
    #   print("Member data", members_data)
      for member in members_data:
          member_id = member['id']
          member_name = member['name']
          project_members.append({'id': member_id, 'name': member_name})
  else:
      print(f"Failed to fetch project members - Status code: {response.status_code}")
      print(response.content)  # Print the response content for debugging

  return project_members

