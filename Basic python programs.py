# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VuNwZT1AcagxpDRGX_JKjcsZzB9I3RCk
"""



print('Akshaya')

print("Akshaya")

1-4-1-1-2-0-0-5

1*4*1*1*2*0*0*5

1+4+1+1+2+0+0+5

x=19
y="Akshaya"
print(x)
print(y)

x=str(7)
y=int(3)
z=float(3.25545)
print(x)
print(y)
print(z)

x=8
y="akshaya"
z=6.48
print(type(x))
print(type(y))
print(type(z))

x="akshaya"
x=5
print(x)

x='akshaya'
print(x)
x=9
print(x)

a=8
A='Akshaya'

myvar='John'
my_var='John'
_my_var='John'
myVar='John'
MYVAR='John'
myvar2="John"

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x=y=z='Orange'
print(x)
print(y)
print(z)

value = 42
var1 = value
var2 = value
Var3 = value
var4 = value
var5 = value
var_6 = value
var7 = value
VAr8 = value
VAR9 = value
vAR10 = value
print(var1, var2, var3, var4, var5, var6, var7, var8, var9, var10)

#lists
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#tuple
fruits = ("apple", "banana", "cherry")
x, y, z, = fruits
print(x)
print(y)
print(z)

#set
fruits = {"apple", "banana", "cherry"}
x, y, z = fruits
print(x)
print(y)
print(z)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)



x="Python"
y="is "
z="awesome"
print(x+y+z)

import sys
print(sys.version)

import sys as Akshaya
print(Akshaya.version)

if 5>2:
   print("Five is greater than 2!")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#bfs
from collections import deque
def bfs(g,s):
  q=deque([s])
  v=set()
  v.add(s)
  while q:
    n=q.popleft()
    print(n,end=" ")
    for i in g[n]:
      if i not in v:
        v.add(i)
        q.append(i)
g={'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[]
}
bfs(g,'A')

#encapsulation
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance is ${self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.__balance}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    @property
    def balance(self):
        return self.__balance

    @property
    def account_holder(self):
        return self.__account_holder

account = BankAccount("Alice")
account.deposit(100)
account.withdraw(30)
print(f"Account holder: {account.account_holder}")
print(f"Account balance: ${account.balance}")

#integrating bfs with encapsulation
from collections import deque

class Graph:
    def __init__(self):
        self.__adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.__adjacency_list:
            self.__adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.__adjacency_list and vertex2 in self.__adjacency_list:
            self.__adjacency_list[vertex1].append(vertex2)
            self.__adjacency_list[vertex2].append(vertex1)

    def bfs(self, start_vertex):
        if start_vertex not in self.__adjacency_list:
            print("Start vertex not in graph.")
            return []

        visited = set()
        queue = deque([start_vertex])
        result = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend(neighbor for neighbor in self.__adjacency_list[vertex] if neighbor not in visited)

        return result

    def get_adjacency_list(self):
        return self.__adjacency_list

graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")

print("Graph adjacency list:", graph.get_adjacency_list())
print("BFS starting from vertex 'A':", graph.bfs("A"))

#iterative deepening search
class Graph:
    def __init__(self):
        self.__adjacency_list = {}
    def add_vertex(self, vertex):
        if vertex not in self.__adjacency_list:
            self.__adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.__adjacency_list and vertex2 in self.__adjacency_list:
            self.__adjacency_list[vertex1].append(vertex2)
            self.__adjacency_list[vertex2].append(vertex1)

    def ids(self, start_vertex, goal_vertex):
        def dls(vertex, depth):
            if depth == 0:
                if vertex == goal_vertex:
                    return [vertex]
                else:
                    return None
            elif depth > 0:
                for neighbor in self.__adjacency_list.get(vertex, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        path = dls(neighbor, depth - 1)
                        if path:
                            return [vertex] + path
            return None

        depth = 0
        while True:
            visited = set()
            path = dls(start_vertex, depth)
            if path:
                return path
            depth += 1

    def get_adjacency_list(self):
        return self.__adjacency_list

graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")

print("Graph adjacency list:", graph.get_adjacency_list())
print("IDS path from 'A' to 'D':", graph.ids("A", "D"))

#dfs
class Graph:
    def __init__(self):
        self.__adjacency_list = {}
    def add_vertex(self, vertex):
        if vertex not in self.__adjacency_list:
            self.__adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
      if vertex1 in self.__adjacency_list and vertex2 in self.__adjacency_list:
            self.__adjacency_list[vertex1].append(vertex2)
            self.__adjacency_list[vertex2].append(vertex1)

    def dfs_recursive(self, start_vertex):
        visited = set()
        def dfs(vertex):
            if vertex not in visited:
                visited.add(vertex)
                pri  nt(vertex, end=' ')
                for neighbor in self.__adjacency_list.get(vertex, []):
                    if neighbor not in visited:
                        dfs(neighbor)
        dfs(start_vertex)
        print()
    def get_adjacency_list(self):
        return self.__adjacency_list

graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")

print("Graph adjacency list:", graph.get_adjacency_list())
print("DFS traversal starting from 'A':")
graph.dfs_recursive("A")

#map colouring

class MapColoring:
    def __init__(self, regions, neighbors, colors):
        self.regions = regions
        self.neighbors = neighbors
        self.colors = colors
        self.coloring = {}
    def is_valid(self, region, color):
        for neighbor in self.neighbors.get(region, []):
            if self.coloring.get(neighbor) == color:
                return False
        return True

    def color_map(self, region_index=0):
        if region_index == len(self.regions):
            return True

        region = self.regions[region_index]
        for color in self.colors:
            if self.is_valid(region, color):
                self.coloring[region] = color
                if self.color_map(region_index + 1):
                    return True
                self.coloring.pop(region)
        return False

    def solve(self):
        if self.color_map():
            return self.coloring
        else:
            return None

regions = ['A', 'B', 'C', 'D', 'E']
neighbors = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['A', 'C'],
    'E': ['B', 'C']
}
colors = ['Red', 'Green', 'Blue', 'Yellow']

map_coloring = MapColoring(regions, neighbors, colors)
solution = map_coloring.solve()

if solution:
    print("Solution found:")
    for region, color in solution.items():
        print(f"{region}: {color}")
else:
    print("No solution exists.")

#random variable movement
import random
import matplotlib.pyplot as plt

def random_variable_movement(steps):
    position = [0]  # Start at position 0

    for _ in range(steps):
        move = random.choice([-1, 1])
        position.append(position[-1] + move)

    return position


steps = 100


movement = random_variable_movement(steps)


plt.plot(movement)
plt.title(f"Random Variable Movement over {steps} steps")
plt.xlabel("Step")
plt.ylabel("Position")
plt.show()

"""

---

"""

#line plot
import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y)
plt.title("Line Plot Example")
plt.xlabel("Time")
plt.ylabel("Values")
plt.show()

#bar plot
import matplotlib.pyplot as plt


categories = ['A', 'B', 'C', 'D']
values = [23, 17, 35, 29]


plt.bar(categories, values)
plt.title("Bar Plot Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

#histogram
import matplotlib.pyplot as plt
import numpy as np


data = np.random.randn(1000)


plt.hist(data, bins=30)
plt.title("Histogram Example")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

#scatter plot
import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 8, 10]


plt.scatter(x, y)
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

#box plot
import seaborn as sns
import numpy as np


data = np.random.normal(size=100)


sns.boxplot(data=data)
plt.title("Box Plot Example")
plt.show()

#heat map
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


data = np.random.rand(10, 10)


sns.heatmap(data, annot=True, cmap='coolwarm')
plt.title("Heatmap Example")
plt.show()

#pair plot
import seaborn as sns
import pandas as pd


df = sns.load_dataset("iris")


sns.pairplot(df, hue="species")
plt.show()

#pie chart
import matplotlib.pyplot as plt


labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]


plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Pie Chart Example")
plt.show()

#violin plot
import seaborn as sns
import matplotlib.pyplot as plt


data = sns.load_dataset("tips")


sns.violinplot(x="day", y="total_bill", data=data)
plt.title("Violin Plot Example")
plt.show()

#bubble chart
import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]
sizes = [100, 200, 300, 400, 500]


plt.scatter(x, y, s=sizes, alpha=0.5)
plt.title("Bubble Chart Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

#stacked bar chart

df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Type1': [20, 34, 30, 35],
    'Type2': [25, 32, 34, 20],
})

df.set_index('Category').plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart Example')
plt.show()

#word cloud
from wordcloud import WordCloud


text = "data visualization project dataset python charts seaborn matplotlib plotly"


wordcloud = WordCloud().generate(text)


plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

#3D plot
from mpl_toolkits.mplot3d import Axes3D


x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)
ax.set_title('3D Plot Example')
plt.show()

from heapq import heappop, heappush

def a_star(start, goal, neighbors, h):

    open_set = [(0 + h(start), 0, start, [])]

    while open_set:
        _, g, node, path = heappop(open_set)

        if node in visited:
            continue
        path = path + [node]

        if node == goal:
            return path

        visited.add(node)

        for neighbor, cost in neighbors(node):
            if neighbor not in visited:
                heappush(open_set, (g + cost + h(neighbor), g + cost, neighbor, path))

    return None
def neighbors(node):
    graph = {
        'A': [('B', 1), ('C', 3)],
        'B': [('A', 1), ('D', 1), ('E', 5)],
        'C': [('A', 3), ('F', 1)],
        'D': [('B', 1)],
        'E': [('B', 5), ('F', 1)],
        'F': [('C', 1), ('E', 1)]
    }
    return graph.get(node, [])

def h(node):
    heuristics = {'A': 5, 'B': 4, 'C': 2, 'D': 6, 'E': 1, 'F': 0}
    return heuristics.get(node, float('inf'))


path = a_star('A', 'F', neighbors, h)
print("Path:", path)

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load the dataset from a CSV file
# Replace 'diabetes.csv' with the path to your file
data = pd.read_csv('/content/diabetes (1).csv')

# Display the first few rows of the dataset
print("Dataset preview:")
print(data.head())

# Check for and drop any missing values (optional)
data = data.dropna()

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(data)

# Apply K-Means clustering
n_clusters = 3  # Set the number of clusters you want
kmeans = KMeans(n_clusters=n_clusters, random_state=0)
data['Cluster'] = kmeans.fit_predict(X_scaled)

# Dimensionality reduction for visualization
pca = PCA(n_components=2)  # Reduce to 2 dimensions for visualization
X_pca = pca.fit_transform(X_scaled)

# Plotting the clusters
plt.figure(figsize=(10, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=data['Cluster'], cmap='viridis', marker='o', edgecolor='k', s=50)
plt.title('K-Means Clustering of Diasbetes Dataset')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.colorbar(label='Cluster Label')
plt.show()

# Optional: Print cluster centers
print("Cluster Centers:")
print(kmeans.cluster_centers_)

# Commented out IPython magic to ensure Python compatibility.
# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

# Set up for plotting in Colab
# %matplotlib inline
sns.set(style="whitegrid")

# Upload the diabetes dataset file if not already in Colab
from google.colab import files
import os

if not os.path.isfile('diabetes.csv'):
    print("Please upload the diabetes.csv file.")
    uploaded = files.upload()

# Load the dataset
try:
    df = pd.read_csv("/content/diabetes .csv")
except FileNotFoundError:
    print("The file 'diabetes.csv' could not be found. Please ensure it's uploaded.")

# Preprocess the data
try:
    features = df.drop(columns=['Outcome'])  # Drop any label if present
except KeyError:
    print("Outcome column not found in the dataset. Please check the dataset structure.")

# Standardize the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Determine optimal K using the Elbow Method
inertia = []
K_range = range(1, 11)
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

# Plot the Elbow Curve
plt.figure(figsize=(8, 6))
plt.plot(K_range, inertia, 'bo-')
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()

# Fit the K-means model with the optimal K
optimal_k = 3  # Assume 3 is optimal from elbow/silhouette analysis
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
clusters = kmeans.fit_predict(scaled_features)
df['Cluster'] = clusters

# Evaluate the clustering using silhouette score
score = silhouette_score(scaled_features, clusters)
print(f'Silhouette Score: {score}')

# Analyze cluster characteristics
cluster_centers = kmeans.cluster_centers_
print(f'Cluster Centers:\n {cluster_centers}')

from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Step 1: Define training data
# Features: [fever, body aches, runny nose, itchy eyes]
# Labels: 0 = Cold, 1 = Flu, 2 = Allergies

# Training data (symptoms for each condition)
X = np.array([
    [1, 1, 1, 0],  # Flu
    [1, 0, 1, 0],  # Cold
    [0, 0, 1, 1],  # Allergies
    [1, 1, 0, 0],  # Flu
    [0, 0, 1, 0],  # Cold
    [0, 0, 0, 1],  # Allergies
])

# Labels (0 = Cold, 1 = Flu, 2 = Allergies)
y = np.array([1, 0, 2, 1, 0, 2])

# Step 2: Train the decision tree
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Step 3: Function to classify symptoms
def diagnose_symptoms(fever, body_aches, runny_nose, itchy_eyes):
    symptoms = np.array([[fever, body_aches, runny_nose, itchy_eyes]])
    prediction = clf.predict(symptoms)[0]

    if prediction == 0:
        return "You may have a cold. Please rest and drink plenty of fluids."
    elif prediction == 1:
        return "You may have the flu. Please consult a doctor for a diagnosis."
    elif prediction == 2:
        return "You may have allergies. Consider taking an antihistamine or seeing a doctor."

# Step 4: Example usage
# Here’s how you would call this function with symptoms
# For example, a user with a fever and body aches, no runny nose or itchy eyes
print(diagnose_symptoms(fever=1, body_aches=1, runny_nose=0, itchy_eyes=0))