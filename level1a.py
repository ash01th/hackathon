import json
file_path = 'level1a.json'
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
orders={0:0,1:70,2:70,3:90,4:50,5:70,6:90,7:110,8:70,9:110,10:70,11:70,12:110,13:110,14:90,15:50,16:90,17:110,18:90,19:70,20:110}
n_dist={}
for i in range(1,len(dist_mat[0])):
    n_dist[i]=dist_mat[0][i]
slots=[]
capacity=0
n_dist=dict(sorted(n_dist.items(), key=lambda item: item[1]))
print(n_dist)
 
