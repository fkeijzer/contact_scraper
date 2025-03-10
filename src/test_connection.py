from dotenv import load_dotenv
import os
from hubspot import HubSpot

# Laad de environment variables
load_dotenv()

def test_hubspot_connection():
    try:
        # Initialiseer de HubSpot client
        api_client = HubSpot(access_token=os.getenv('HUBSPOT_API_KEY'))
        
        # Probeer een simpele API call te maken
        contacts_page = api_client.crm.contacts.basic_api.get_page()
        
        print("✅ Verbinding met HubSpot succesvol!")
        print(f"Aantal contacten in je account: {len(contacts_page.results)}")
        
    except Exception as e:
        print("❌ Er ging iets mis met de HubSpot verbinding:")
        print(str(e))

if __name__ == "__main__":
    test_hubspot_connection()

