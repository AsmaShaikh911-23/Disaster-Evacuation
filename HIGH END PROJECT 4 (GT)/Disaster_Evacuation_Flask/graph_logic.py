import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

def create_india_graph(disaster):
    G = nx.Graph()

    # Roads with distances - Expanded to cover more of India
    edges = [
        # North
        ("Chandigarh", "Delhi", 3),
        # West
        ("Ahmedabad", "Jaipur", 6),
        ("Ahmedabad", "Mumbai", 5),
        ("Ahmedabad", "Bhopal", 5),
        # East
        ("Lucknow", "Kolkata", 8),
        ("Nagpur", "Kolkata", 10),
        # South
        ("Hyderabad", "Bengaluru", 5),
        ("Chennai", "Bengaluru", 3),
        # Existing Core Routes
        ("Delhi", "Jaipur", 4),
        ("Delhi", "Lucknow", 5),
        ("Delhi", "Bhopal", 7),
        ("Jaipur", "Bhopal", 5),
        ("Jaipur", "Mumbai", 8),
        ("Lucknow", "Bhopal", 6),
        ("Bhopal", "Nagpur", 4),
        ("Nagpur", "Hyderabad", 3),
        ("Nagpur", "Mumbai", 7),
        ("Hyderabad", "Chennai", 5)
    ]

    for u, v, d in edges:
        G.add_edge(u, v, weight=d)

    # 🚫 Blocked roads simulation
    if disaster == "flood":
        G.remove_edge("Bhopal", "Nagpur")
    elif disaster == "fire":
        G.remove_edge("Jaipur", "Bhopal")
    elif disaster == "earthquake":
        G.remove_edge("Delhi", "Jaipur")

    return G


def find_evacuation_route(start, destination, disaster):
    G = create_india_graph(disaster)

    try:
        # Check if there's a path to the destination
        if not nx.has_path(G, start, destination):
            return [f"No safe route to {destination}! Stay put or seek local shelter."], float('inf')
        
        path = nx.dijkstra_path(G, start, destination, weight="weight")
        distance = nx.dijkstra_path_length(G, start, destination, weight="weight")
        
        draw_india_map(G, path)
        return path, round(distance, 2)
        
    except nx.NetworkXNoPath:
        return [f"No safe route to {destination}! Stay put or seek local shelter."], float('inf')


def draw_india_map(G, path):
    # Get absolute path to static folder
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Load India map with absolute path
    image_path = os.path.join(base_dir, "static", "india_map.png")
    
    # Check if file exists before loading
    if not os.path.exists(image_path):
        print(f"Warning: India map not found at {image_path}")
        # Create a blank figure instead
        plt.figure(figsize=(6, 8))
        plt.text(0.5, 0.5, "Map image not found", ha='center', va='center', fontsize=12)
    else:
        india_map = mpimg.imread(image_path)
        plt.figure(figsize=(8, 10))  # Increased figure size for more space
        plt.imshow(india_map)
    
    plt.axis("off")
    
    # Approximate map coordinates
    pos = {
        "Delhi": (219, 225),
        "Jaipur": (191, 272),
        "Bhopal": (222, 362),
        "Nagpur": (213, 437),
        "Hyderabad": (249, 519),
        "Mumbai": (140, 450),
        "Lucknow": (280, 280),
        "Chennai": (300, 660), # Adjusted for better separation
        "Chandigarh": (225, 180),
        "Kolkata": (400, 380),
        "Ahmedabad": (120, 350),
        "Bengaluru": (255, 610) # Adjusted for better separation
    }
    
    # Draw all graph edges with a subtle style
    nx.draw_networkx_edges(G, pos, edge_color="#cccccc", width=2)
    
    # --- Enhanced Node and Path Drawing ---
    if len(path) > 1 and path[0] != "No safe route":
        start_node = path[0]
        end_node = path[-1]
        
        # Define colors for different nodes
        node_colors = []
        for node in G.nodes():
            if node == start_node:
                node_colors.append("#ff4757")  # Start node (Red)
            elif node == end_node:
                node_colors.append("#2ed573")  # End node (Green)
            else:
                node_colors.append("#1e90ff")  # Intermediate nodes (Blue)
                
        # Draw the nodes with borders
        nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=600, edgecolors="white", linewidths=2)
        
        # Draw city labels with automatic text adjustment to prevent overlap
        label_pos = {k: (v[0], v[1] - 20) for k, v in pos.items()} # Shift labels slightly above nodes
        nx.draw_networkx_labels(G, label_pos, font_color="black", font_weight="bold", font_size=9,
                                bbox=dict(facecolor='white', alpha=0.7, boxstyle='round,pad=0.3', edgecolor='none'))
        
        # Highlight the evacuation path with a thick red line
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(
            G, pos, edgelist=path_edges, edge_color="#ff4757", width=4, style="solid"
        )
        
        # Set a clear title for the map
        route_str = ' → '.join(path)
        plt.title(f"Evacuation Route: {route_str}", fontsize=14, weight='bold', pad=20)
    else:
        # Fallback for when no route is found
        nx.draw(
            G, pos, with_labels=True, node_color="#cccccc", node_size=500,
            font_color="black", font_weight="bold"
        )
        plt.title("No Safe Evacuation Route Found")
        
    # Save evacuation map with absolute path
    evac_map_path = os.path.join(base_dir, "static", "evacuation_map.png")
    plt.savefig(evac_map_path, bbox_inches='tight', dpi=100)
    plt.close()