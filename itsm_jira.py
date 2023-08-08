import requests

# Configuration de l'API Jira
JIRA_BASE_URL = 'https://your-jira-instance.atlassian.net/rest/api/2'
USERNAME = 'your_username'
API_TOKEN = 'your_api_token'  # Pour les anciennes versions de Jira, vous pouvez utiliser votre mot de passe à la place du token.

# Endpoint pour créer un ticket dans Jira
CREATE_ISSUE_ENDPOINT = '/issue'

# Fonction pour effectuer une requête POST pour créer un ticket dans Jira
def create_jira_issue(issue_data):
    headers = {
        'Authorization': f'Basic {USERNAME}:{API_TOKEN}',
        'Content-Type': 'application/json',
    }
    response = requests.post(JIRA_BASE_URL + CREATE_ISSUE_ENDPOINT, json=issue_data, headers=headers)
    return response

if __name__ == '__main__':
    # Exemple de création d'un nouveau ticket dans Jira
    new_issue_data = {
        'fields': {
            'project': {
                'key': 'YOUR_PROJECT_KEY',  # Remplacez YOUR_PROJECT_KEY par la clé du projet réel
            },
            'summary': 'Nouveau ticket créé depuis Python',
            'description': 'Description du ticket créé depuis Python',
            'issuetype': {
                'name': 'Bug',  # Remplacez 'Bug' par le type de ticket que vous souhaitez créer
            },
        },
    }

    create_response = create_jira_issue(new_issue_data)
    print(create_response.status_code)
    print(create_response.json())
