from PIL import Image 
import random as random
import json
import os
from IPython.display import display

bg=["bg"]
bg_weights = [100]

head = ["head"]
head_weights = [100]

eyes = ["e1", "e2"]
eyes_weights = [70, 30]

hair = ['h1', 'h2']
hair_weights = [22,78]

mouth = ['m1','m2','m3']
mouth_weights = [20, 30,50]

nose = ['Nose 1', 'Nose 2']
nose_weights = [90, 10]

bg_files = {
    "bg": "bg1"
}

head_files = {
    "head": "head1"
}

eyes_files = {
    "e1": "eyes1",
    "e2": "eyes2"
}

hair_files = {
    "h1": "hair1",
    "h2": "hair2"
}


mouth_files = {
    "m1": "mouth1",
    "m2": "mouth2",
    "m3": "mouth3",
}

nose_files = {
    "Nose 1": "nose1",
    "Nose 2": "nose2"   
}

TOTAL_IMAGES = 10
all_images = [] 

def create_new_image():
    
    new_image = {} #

    new_image ["bg"] = random.choices(bg, bg_weights)[0]
    new_image ["Head"] = random.choices(head, head_weights)[0]
    new_image ["Eyes"] = random.choices(eyes, eyes_weights)[0]
    new_image ["Hair"] = random.choices(hair, hair_weights)[0]
    new_image ["Mouth"] = random.choices(mouth, mouth_weights)[0]
    new_image ["Nose"] = random.choices(nose, nose_weights)[0]
    
    if new_image in all_images:
        return create_new_image()
    else:
        return new_image
    
for i in range(TOTAL_IMAGES): 
    
    new_trait_image = create_new_image()
    
    all_images.append(new_trait_image)


def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1
   
print(all_images)

bg_count = {}
for item in bg:
    bg_count[item] = 0

head_count = {}
for item in head:
    head_count[item] = 0

eyes_count = {}
for item in eyes:
    eyes_count[item] = 0
    
hair_count = {}
for item in hair:
    hair_count[item] = 0
    
mouth_count = {}
for item in mouth:
    mouth_count[item] = 0
    
nose_count = {}
for item in nose:
    nose_count[item] = 0

for image in all_images:
    bg_count[image["bg"]] += 1
    head_count[image["Head"]] += 1
    eyes_count[image["Eyes"]] += 1
    hair_count[image["Hair"]] += 1
    mouth_count[image["Mouth"]] += 1
    nose_count[image["Nose"]] += 1
    
print(bg_count)
print(head_count)
print(eyes_count)
print(hair_count)
print(mouth_count)
print(nose_count)


for item in all_images:

    im1 = Image.open(f'./Images/head/{head_files[item["Head"]]}.png').convert('RGBA')
    im2 = Image.open(f'./Images/eyes/{eyes_files[item["Eyes"]]}.png').convert('RGBA')
    im4 = Image.open(f'./Images/hair/{hair_files[item["Hair"]]}.png').convert('RGBA')
    im5 = Image.open(f'./Images/mouth/{mouth_files[item["Mouth"]]}.png').convert('RGBA')
    im6 = Image.open(f'./Images/nose/{nose_files[item["Nose"]]}.png').convert('RGBA')

    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im4)
    com3 = Image.alpha_composite(com2, im5)
    com4 = Image.alpha_composite(com3, im6)

    rgb_im = com4.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./imagesnft/" + file_name)