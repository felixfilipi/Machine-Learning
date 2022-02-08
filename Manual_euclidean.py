import numpy as np

def euclidean(x2,x1,y2,y1): 
    res = np.sqrt((x2-x1)**2+(y2-y1)**2) 
    return res 

data = [(0.40, 0.53),(0.22, 0.38),(0.35,0.32),
        (0.26,0.19),(0.08,0.41),(0.45,0.30)] 

result = [] 
for first_data in data:
    for second_data in data: 
        distance = euclidean(first_data[0], second_data[0], 
                first_data[1], second_data[1]) 
        result.append(np.round(distance,3)) 

print(result) 
