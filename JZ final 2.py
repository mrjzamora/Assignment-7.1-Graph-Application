import networkx as nx
import matplotlib.pyplot as plt

# Function to create a graph of theme parks and routes between them
def create_graph():
    G = nx.Graph()  # Create an empty undirected graph
    # List of theme parks
    theme_parks = [
        "Magic Kingdom, FL", "Disneyland, CA", "Legoland, CA",
        "Sesame Place, PA", "Story Land, NH", "Santa's Village, NH",
        "Universal's Island of Adventure, FL", "Dutch Wonderland, PA",
        "Disney's Animal Kingdom, FL", "SeaWorld Orlando, FL",
        "Carowinds, NC", "Kings Dominion, VA", "Silver Dollar City, MO",
        "Dollywood, TN", "Nickelodeon Universe, NJ", "Six Flags Magic Mountain, CA",
        "Cedar Point, OH", "Kennywood, PA", "Hersheypark, PA", "Busch Gardens Tampa Bay, FL"
    ]
    # Routes between theme parks with distances
    routes = [
        ("Magic Kingdom, FL", "Disneyland, CA", 2500), ("Disneyland, CA", "Legoland, CA", 95),
        ("Legoland, CA", "Sesame Place, PA", 2900), ("Sesame Place, PA", "Story Land, NH", 350),
        ("Story Land, NH", "Santa's Village, NH", 50), ("Santa's Village, NH", "Universal's Island of Adventure, FL", 1400),
        ("Universal's Island of Adventure, FL", "Dutch Wonderland, PA", 950), ("Dutch Wonderland, PA", "Disney's Animal Kingdom, FL", 980),
        ("Disney's Animal Kingdom, FL", "SeaWorld Orlando, FL", 16), ("SeaWorld Orlando, FL", "Carowinds, NC", 550),
        ("Carowinds, NC", "Kings Dominion, VA", 350), ("Kings Dominion, VA", "Silver Dollar City, MO", 920),
        ("Silver Dollar City, MO", "Dollywood, TN", 550), ("Dollywood, TN", "Nickelodeon Universe, NJ", 800),
        ("Nickelodeon Universe, NJ", "Six Flags Magic Mountain, CA", 2800), ("Six Flags Magic Mountain, CA", "Cedar Point, OH", 2300),
        ("Cedar Point, OH", "Kennywood, PA", 150), ("Kennywood, PA", "Hersheypark, PA", 200),
        ("Hersheypark, PA", "Busch Gardens Tampa Bay, FL", 1000), ("Busch Gardens Tampa Bay, FL", "Magic Kingdom, FL", 100)
    ]
    # Add theme parks as nodes and routes as weighted edges to the graph
    G.add_nodes_from(theme_parks)
    G.add_weighted_edges_from(routes)
    return G

# Function to visualize a path on the graph
def visualize_path(G, path, title):
    pos = nx.spring_layout(G)  # Position nodes using Fruchterman-Reingold force-directed algorithm
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)  # Draw the graph with nodes
    # Draw the path on the graph with red edges
    path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
    plt.title(title)  # Set the title of the plot
    plt.show()  # Display the plot

# Heuristic function for A* algorithm
def astar_heuristic(u, v, G, weight='weight'):
    return nx.astar_path_length(G, u, v, weight=weight)

# Function to find paths using different algorithms and visualize them
def find_paths_and_draw(G, start, end):
    # Dijkstra's Algorithm
    path_dijkstra = nx.dijkstra_path(G, source=start, target=end, weight='weight')
    visualize_path(G, path_dijkstra, "Dijkstra's Path from {} to {}".format(start, end))

    # Bellman-Ford Algorithm
    path_bellman = nx.bellman_ford_path(G, source=start, target=end, weight='weight')
    visualize_path(G, path_bellman, "Bellman-Ford Path from {} to {}".format(start, end))

    # Uniform Cost Search Algorithm
    path_ucs = nx.shortest_path(G, source=start, target=end, weight='weight')
    visualize_path(G, path_ucs, "Uniform Cost Search Path from {} to {}".format(start, end))

# Function to display a menu for selecting start and end parks
def menu():
    G = create_graph()  # Create the graph
    parks = list(G.nodes)  # Get the list of theme parks
    print("Available Theme Parks:")
    for i, park in enumerate(parks):
        print(f"{i + 1}. {park}")  # Print the available theme parks with their indices

    start_index = int(input("Select start park (number): ")) - 1  # Prompt user to select start park
    end_index = int(input("Select end park (number): ")) - 1  # Prompt user to select end park

    find_paths_and_draw(G, parks[start_index], parks[end_index])  # Find paths and visualize them

if __name__ == '__main__':
    menu()  # Run the menu function when the script is executed
