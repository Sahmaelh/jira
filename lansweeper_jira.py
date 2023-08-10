import requests

# Informations d'authentification pour Lansweeper
lansweeper_url = "https://votre-serveur-lansweeper/api"
lansweeper_auth = ("votre_nom_utilisateur", "votre_mot_de_passe")

# Informations d'authentification pour Jira
jira_url = "https://votre-instance-jira.atlassian.net"
jira_auth = ("votre_nom_utilisateur", "votre_token_api_jira")

# Appel à l'API Lansweeper pour récupérer les machines non mises à jour
response_lansweeper = requests.get(
    f"{lansweeper_url}/machines-non-mises-a-jour",
    auth=lansweeper_auth
)

if response_lansweeper.status_code == 200:
    machines_non_mises_a_jour = response_lansweeper.json()

    for machine in machines_non_mises_a_jour:
        # Création d'un ticket Jira pour chaque machine non mise à jour
        jira_payload = {
            "fields": {
                "project": {"key": "ITSM"},
                "summary": f"Machine non mise à jour : {machine['nom']}",
                "description": f"La machine {machine['nom']} nécessite une mise à jour.",
                "priority": {"name": "High"},
                # ... autres champs nécessaires
            }
        }

        response_jira = requests.post(
            f"{jira_url}/rest/api/3/issue",
            json=jira_payload,
            auth=jira_auth
        )

        if response_jira.status_code == 201:
            print(f"Ticket créé pour la machine {machine['nom']}")
        else:
            print(f"Échec de la création du ticket pour {machine['nom']}", response_jira.text)
else:
    print("Échec de la récupération des données de Lansweeper", response_lansweeper.text)
