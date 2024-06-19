import requests
import pandas as pd

from getMembers import getMembers
from getMilestones import getMilestones
from getExistingTickets import getExistingIssues

from config import ACCESS_TOKEN, BASE_URL

    

# [{'id': 487, 'name': 'Suman Rimal'}, {'id': 539, 'name': 'Bishesh Tuladhar'}, {'id': 491, 'name': 'Kabi Shakya'}]  getMembers value
# {'Sprint 4': 1000, 'Sprint 3': 999, 'Sprint 2': 998, 'Sprint 1': 997}  getMilestones value

def getIdByName(name, project_id):
    data = getMembers(project_id)
    for item in data:
        if item['name'] == name:
            return item['id']
    return None



def createTicket(project_id):
    # Read the Excel file without headers
  df = pd.read_excel('Tasks.xlsx', header=1)

  api_url = f'{BASE_URL}/v4/projects/{project_id}/issues'


  # Headers for API request
  headers = {
      'Content-Type': 'application/json',
      'Private-Token': ACCESS_TOKEN
  }

  # Fetch existing issues
  existing_issues = getExistingIssues(project_id)
  existing_titles = [issue['title'] for issue in existing_issues]

  # Fetch milestone mapping
  milestone_mapping = getMilestones(project_id)

  # Iterate through rows in the dataframe and create tickets
  for index, row in df.iterrows():
      if row['Ticket Name'] in existing_titles:
        print(f"Ignored duplicate task: {row['Ticket Name']}")
        continue
        
      payload = {'title': row['Ticket Name']}

      # Add assignee_id to payload if available
      assignee_id = getIdByName(row['Assignee'], project_id)
      if assignee_id:
        payload['assignee_ids'] = [assignee_id]

     # Add milestone_id to payload if available
      milestone_id = milestone_mapping.get(row['Milestone'])
      if milestone_id:
        payload['milestone_id'] = milestone_id

      # Add due_date to payload if available
      if not pd.isna(row['Due Date']):
        payload['due_date'] = row['Due Date'].strftime('%Y-%m-%d')

      # Add labels to payload if available
      if not pd.isna(row['Labels']):
        labels = row['Labels'].replace('[', '').replace(']', '').replace('"', '').split(', ')
        payload['labels'] = labels

      response = requests.post(api_url, headers=headers, json=payload)
        
      if response.status_code == 201:
          print(f"Issue created: {row['Ticket Name']}")
      else:
          print(f"Failed to create issue: {row['Ticket Name']} - Status code: {response.status_code}")
          print(response.json())