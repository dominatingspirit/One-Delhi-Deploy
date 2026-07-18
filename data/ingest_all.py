import pandas as pd
from elasticsearch import Elasticsearch, helpers
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Access the variables
ES_CLOUD_ID = os.getenv("ES_CLOUD_ID")
ES_API_KEY = os.getenv("ES_API_KEY")

# Initialize Client
ES_CLIENT = Elasticsearch(
    cloud_id=ES_CLOUD_ID,
    api_key=ES_API_KEY
)
INDEX_NAME = "transit_nodes"

def ingest_all():
    print("--- 🔍 Starting Elasticsearch Ingestion ---")
    
    # Check if variables were loaded correctly
    if not ES_CLOUD_ID or not ES_API_KEY:
        print("❌ Error: Missing credentials in .env file!")
        return

    # Rest of your existing ingestion code...
    df = pd.read_csv('data/all_stops_merged.csv')
    
    documents = []
    for _, row in df.iterrows():
        documents.append({
            "_index": INDEX_NAME,
            "_source": {
                "id": str(row['stop_id']),
                "name": row['stop_name'],
                "type": row['type'],
                "location": {"lat": float(row['stop_lat']), "lon": float(row['stop_lon'])}
            }
        })
    
    helpers.bulk(ES_CLIENT, documents)
    print("✅ Successfully indexed all transit nodes!")

if __name__ == "__main__":
    ingest_all()