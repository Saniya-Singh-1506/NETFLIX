import matplotlib.pyplot as plt
import networkx as nx

# Create a binary tree
G = nx.DiGraph()

# Add edges
edges = [
    ("1", "2"), ("1", "3"),
    ("2", "4"), ("2", "5"),
    ("3", "6"), ("3", "7")
]
G.add_edges_from(edges)

# Perfect tree positions
pos = {
    "1": (0, 0),
    "2": (-1, -1), "3": (1, -1),
    "4": (-1.5, -2), "5": (-0.5, -2),
    "6": (0.5, -2), "7": (1.5, -2)
}

# Draw
plt.figure(figsize=(7, 5))
nx.draw(G, pos, with_labels=True,
        node_size=3000, node_color=["gold", "skyblue", "skyblue", "lightgreen", "lightgreen", "pink", "pink"],
        font_size=14, font_weight="bold", edge_color="gray", arrows=False)

plt.title("🌳 Cute Colorful Binary Tree 🌳", fontsize=18, fontweight="bold")
plt.show()
