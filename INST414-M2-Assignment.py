import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

#League average statistics for 2024

league_obp = 0.312
league_slg = 0.399
constant_oaa = 15
league_speed = 27

#Creating 4-tool index metric

df = pd.read_csv("4_tools.csv")
df = df.dropna(subset=["outs_above_average"])

#Function: Normalizes a player stats to league average, and provides a number where 1 is average

def ftiCalculation(player):

    player_stats = df.loc[df["last_first"]==str(player)]

    normalized_obp =  player_stats["on_base_percent"] / league_obp
    normalized_slg =  player_stats["slg_percent"] / league_slg
    normalized_oaa = 1 + (player_stats["outs_above_average"] / constant_oaa)
    normalized_speed = player_stats["sprint_speed"] / league_speed

    fti = (0.35 * normalized_obp) + (0.30 * normalized_slg) + (0.20 * normalized_oaa) + (0.20 * normalized_speed)
    print(fti)

#Enter Name: Last, First

ftiCalculation(player="Doyle, Brenton")
ftiCalculation(player="Cowser, Colton")
ftiCalculation(player="Judge, Aaron")
ftiCalculation(player="Langford, Wyatt")
ftiCalculation(player="Kwan, Steven")

#Network

g = nx.Graph()

#Connections between the players

g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)

# Node Positionings

pos = {1: (1.321318, 1), 2: (1.251742, 2), 3: (1.372702, 3), 4: (1.124021, 4), 5: (1.17311, 5)}

options = {
    "font_size": 13,
    "node_size": [1500, 800, 1650, 550, 600],
    "node_color": "white",
    "edgecolors": "red",
    "linewidths": 2,
    "width": 2,
}

nx.draw_networkx(g, pos, **options)

plt.axis("on")
plt.grid(True)
plt.show()





