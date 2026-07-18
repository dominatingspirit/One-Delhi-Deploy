import pandas as pd
import networkx as nx
from scipy import spatial
import os
import pickle

def process_transit():
    print("--- 🛠️ Starting Multimodal Stitching Pipeline ---")
    
    # 1. Load Metro and Bus Data
    # Note: Ensure these paths exist exactly as written
    metro_stops = pd.read_csv('data/DMRC_GTFS/stops.txt')
    bus_stops = pd.read_csv('data/GTFS/stops.txt')
    metro_times = pd.read_csv('data/DMRC_GTFS/stop_times.txt')
    bus_times = pd.read_csv('data/GTFS/stop_times.txt')
    
    metro_stops['type'] = 'metro'
    bus_stops['type'] = 'bus'
    
    all_stops = pd.concat([metro_stops, bus_stops])
    
    # 2. Build the Graph
    G = nx.Graph()
    for _, row in all_stops.iterrows():
        G.add_node(str(row['stop_id']), name=row['stop_name'], type=row['type'], 
                   lat=row['stop_lat'], lon=row['stop_lon'])

    # 3. Add Edges (Trip Connectivity)
    print("--- 🔗 Stitching Trip Sequences ---")
    for df in [metro_times, bus_times]:
        for _, group in df.sort_values(['trip_id', 'stop_sequence']).groupby('trip_id'):
            s_ids = group['stop_id'].astype(str).tolist()
            for i in range(len(s_ids) - 1):
                G.add_edge(s_ids[i], s_ids[i+1], weight=2)

    # 4. Spatial Stitching (Metro <-> Bus Transfers)
    print("--- 🔗 Stitching Multimodal Transfers ---")
    tree = spatial.cKDTree(bus_stops[['stop_lat', 'stop_lon']].values)
    distances, indices = tree.query(metro_stops[['stop_lat', 'stop_lon']].values, k=1, distance_upper_bound=0.003)
    
    for i, metro_row in metro_stops.iterrows():
        if indices[i] < len(bus_stops):
            bus_row = bus_stops.iloc[indices[i]]
            G.add_edge(str(metro_row['stop_id']), str(bus_row['stop_id']), weight=5, type='transfer')

    # 5. Export using Python's standard pickle module (avoids NetworkX version issues)
    with open('data/combined_network.gpickle', 'wb') as f:
        pickle.dump(G, f)
        
    all_stops.to_csv('data/all_stops_merged.csv', index=False)
    print(f"✅ Pipeline Success: {G.number_of_nodes()} total nodes integrated.")

if __name__ == "__main__":
    process_transit()