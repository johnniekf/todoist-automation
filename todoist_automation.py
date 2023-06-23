import json
from todoist_api_python.api import TodoistAPI

# TODO: Add subhub to allow instant posting to Todoist
# Allow google sheets integration
# 



with open('secret.json') as f:
		data = json.load(f)
api = data['todoist_api']

# Pull data from Todoist
# try:
#     projects = api.get_projects()
#     print(projects)
# except Exception as error:
#     print(error)

try:
    task = api.add_task(content="Test Task (with label)", labels={"Youtube"})
    print(task)
except Exception as error:
    print(error)
    
    
exit()