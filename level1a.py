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
tour=[x for x in tour if x!=0]
capacity=0
slots=[]
curslot=[]
orders={0:0,1:70,2:70,3:90,4:50,5:70,6:90,7:110,8:70,9:110,10:70,11:70,12:110,13:110,14:90,15:50,16:90,17:110,18:90,19:70,20:110}
print(tour)
for i in tour:
    if orders[i]+capacity>600:
        slots.append(curslot)
        curslot=[i-1]
        capacity=orders[i]
    else:
        capacity+=orders[i]
        curslot.append(i-1)
slots.append(curslot)
for i in range(len(slots)):
    slots[i]=[0]+slots[i]+[0]
out={}
for i in range(len(slots)):
    for j in range(len(slots[i])):
        if slots[i][j]==0:
            slots[i][j]="r0"
        else:
            slots[i][j]="n"+str(slots[i][j])

