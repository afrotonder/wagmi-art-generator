import numpy as np
from PIL import Image
import json

# Opening JSON file
# f = open('colorz.json')
f = open('random.json')

# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list

counter = 0

# works with random.json
for j in data:

    
    im = Image.open('fig1.png')
    
    imgData = np.array(im)

    r1, g1, b1 = 255, 255, 255 # Original value

    rgb = j["rgb"].split(",")

    print(rgb)
    r2, g2, b2 =  int(rgb[0]),int(rgb[1]),int(rgb[2])# Value that we want to replace it with
    
    red, green, blue = imgData[:,:,0], imgData[:,:,1], imgData[:,:,2]

    mask = (red == r1) & (green == g1) & (blue == b1)

    imgData[:,:,:3][mask] = [r2, g2, b2]

    fileName = j["name"]+ "#" + str(counter) + ".png"

    im = Image.fromarray(imgData)

    counter+=1

    im.save(fileName)



# works for colorz.json

# for i in data:
#     for j in data[i]:

        
#         im = Image.open('fig1.png')

#         imgData = np.array(im)

#         r1, g1, b1 = 255, 255, 255 # Original value

#         rgb = j["rgb"].split(",")

#         r2, g2, b2 =  int(rgb[0]),int(rgb[1]),int(rgb[2])# Value that we want to replace it with
     
#         red, green, blue = imgData[:,:,0], imgData[:,:,1], imgData[:,:,2]

#         mask = (red == r1) & (green == g1) & (blue == b1)

#         imgData[:,:,:3][mask] = [r2, g2, b2]

#         fileName = 'wagmiballz#' + str(counter) + ".png"

#         im = Image.fromarray(imgData)

#         counter+=1

#         im.save(fileName)

 

# Closing file
f.close()