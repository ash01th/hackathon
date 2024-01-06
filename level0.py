import numpy as np
import json
file_path = 'level0.json'
with open(file_path, 'r') as json_file:
    data = json.load(json_file)
dist_mat=[]
dist_mat.append(data["restaurants"]["r0"]["neighbourhood_distance"])
dist_mat.append(data["neighbourhoods"]["n0"]["distances"])
dist_mat.append(data["neighbourhoods"]["n1"]["distances"])
dist_mat.append(data["neighbourhoods"]["n2"]["distances"])
dist_mat.append(data["neighbourhoods"]["n3"]["distances"])
dist_mat.append(data["neighbourhoods"]["n4"]["distances"])
dist_mat.append(data["neighbourhoods"]["n5"]["distances"])
dist_mat.append(data["neighbourhoods"]["n6"]["distances"])
dist_mat.append(data["neighbourhoods"]["n7"]["distances"])
dist_mat.append(data["neighbourhoods"]["n8"]["distances"])
dist_mat.append(data["neighbourhoods"]["n9"]["distances"])
dist_mat.append(data["neighbourhoods"]["n10"]["distances"])
dist_mat.append(data["neighbourhoods"]["n11"]["distances"])
dist_mat.append(data["neighbourhoods"]["n12"]["distances"])
dist_mat.append(data["neighbourhoods"]["n13"]["distances"])
dist_mat.append(data["neighbourhoods"]["n14"]["distances"])
dist_mat.append(data["neighbourhoods"]["n15"]["distances"])
dist_mat.append(data["neighbourhoods"]["n16"]["distances"])
dist_mat.append(data["neighbourhoods"]["n17"]["distances"])
dist_mat.append(data["neighbourhoods"]["n18"]["distances"])
dist_mat.append(data["neighbourhoods"]["n19"]["distances"])
dist_mat[0]=[0]+dist_mat[0]
for i in range(1,len(dist_mat)):
    add=[dist_mat[0][i]]
    dist_mat[i]=add+dist_mat[i]    
def tsp_greedy(distances):
    num_cities = len(distances)
    
    # Start from the first city
    current_city = 0
    tour = [current_city]
    
    # Keep track of visited cities
    visited_cities = set([current_city])
    
    while len(visited_cities) < num_cities:
        # Find the nearest unvisited city
        next_city = min(
            range(num_cities),
            key=lambda city: distances[current_city][city] if city not in visited_cities else np.inf
        )
        
        # Move to the next city
        tour.append(next_city)
        visited_cities.add(next_city)
        current_city = next_city

    # Return to the starting city to complete the tour
    tour.append(tour[0])
    
    return tour

# Example usage:
# Replace the 'distances' matrix with the actual distances between cities
distances=np.array(dist_mat)
tour = tsp_greedy(distances)
out={}
num=0
for i in range(len(tour)):
    if tour[i]==0:
        out[i]="r0"
    else:
        out[i]="n"+str(tour[i]-1)
def out_function(dict1):
    output={"v0":{"path":list(dict1.values())}}
    json_output=json.dumps(output)
    with open('level0_output.json', 'w') as json_file:
        json.dump(output, json_file,)
    
out_function(out)
  




