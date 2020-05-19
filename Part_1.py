#Ismail Arda Tuna
#240201031
import numpy as np
from PIL import Image
import os
import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

current_directory = os.getcwd()
current_directory = current_directory.replace("\\","/")
#print(current_directory+"/Car_Data")
os.chdir(current_directory+"/Car_Data")
images_in_file=glob.glob("*.png")

def Image_To_Vector(image_name):
    image = Image.open(image_name,"r")
    image_pixels = np.asarray( image, dtype="float32" )
    image_vector = image_pixels.flatten()
    return image_vector

def Similarity(vector1,vector2):
    dot_product = np.dot(vector1,vector2)
    vector1_norm = np.linalg.norm(vector1)
    vector2_norm = np.linalg.norm(vector2)
    similarity = dot_product/(vector1_norm*vector2_norm)
    return similarity
while(True):
    input_name=str(input("Please Enter input image name with .png extension: "))
    print("")
    if(images_in_file.count(input_name)==1):
        image = mpimg.imread(input_name)
        imgplot = plt.imshow(image)
        plt.show()
        print(" Input image -> ",input_name)
        input_vector = Image_To_Vector(input_name)
        similarity_array = []
        png_names_and_similarity_values= []
        top_3_name_values = []
        for i in range(len(images_in_file)):
            if(images_in_file[i]==input_name):
                continue
            compared_image_vector = Image_To_Vector(images_in_file[i])
            similarity = Similarity(input_vector, compared_image_vector)
            similarity_array.append(similarity)
            similarity_value_and_name=(images_in_file[i],similarity)
            png_names_and_similarity_values.append(similarity_value_and_name)
        similarity_array.sort(reverse=True)
        for j in range(3):
            for k in range(len(png_names_and_similarity_values)):
                if(similarity_array[j]== png_names_and_similarity_values[k][1]):
                    top_3_name_values.append(png_names_and_similarity_values[k])
        for l in range(3):
            image = mpimg.imread(top_3_name_values[l][0])
            imgplot = plt.imshow(image)
            plt.show()
            print("Image Name and Similarity Value -> ", top_3_name_values[l])
        #print("Similarity Values -> ", top_3_name_values[0],",",top_3_name_values[1],",",top_3_name_values[2])
        break
    if(images_in_file.count(input_name)==0):
        print("Image is not found, please try again.")      
