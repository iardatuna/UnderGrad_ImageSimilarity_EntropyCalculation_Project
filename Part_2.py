#Ismail Arda Tuna
#240201031
import pandas as pd
import math

pd.set_option("chained_assignment",None)
data_frame = pd.read_csv("heart_summary.csv")

def GiniIndex(selected_column):
    class_levels = list(data_frame[selected_column].unique())
    level_occurences = list(data_frame[selected_column].value_counts())
    target_levels = list(data_frame["target"].unique())
    probability_list=[]
    class_levels_target_counts_list=[]
    gini_summ=0
    for k in range(len(target_levels)):
        for l in range(len(class_levels)): 
            for j in range(len(data_frame)):
                if( data_frame[selected_column][j]== class_levels[l] and data_frame["target"][j] == target_levels[k]): 
                    gini_summ+=1
            class_levels_target_counts_list.append(tuple((class_levels[l],target_levels[k],gini_summ)))
            gini_summ=0       
    for i in range(len(class_levels)):
        probability=level_occurences[i]/len(data_frame)
        probability_list.append(probability)
    gini_indexes_for_levels=[]
    gini_index = 0
    for m in range(len(class_levels)):
        for n in range(len(class_levels_target_counts_list)):
            if(class_levels[m]==class_levels_target_counts_list[n][0]):
                gini_index += float((class_levels_target_counts_list[n][2]/(level_occurences[m]))**2)
        gini_indexes_for_levels.append((1 - (gini_index)))
        gini_index=0
    gini_index_for_attribute = 0
    for gini in range(len(gini_indexes_for_levels)):
        gini_index_for_attribute += gini_indexes_for_levels[gini]*probability_list[gini]
    return gini_index_for_attribute 

def Entropy(selected_column):
    class_levels = list(data_frame[selected_column].unique())
    level_occurences = list(data_frame[selected_column].value_counts())
    target_levels = list(data_frame["target"].unique())
    probability_list=[]
    class_levels_target_counts_list=[]
    entropy_summ=0
    for k in range(len(target_levels)):
        for l in range(len(class_levels)): 
            for j in range(len(data_frame)):
                if( data_frame[selected_column][j]== class_levels[l] and data_frame["target"][j] == target_levels[k]): 
                    entropy_summ+=1
            class_levels_target_counts_list.append(tuple((class_levels[l],target_levels[k],entropy_summ)))
            entropy_summ=0       
    for i in range(len(class_levels)):
        probability=level_occurences[i]/len(data_frame)
        probability_list.append(probability)
    entropy_for_levels=[]
    entropy_value = 0
    for m in range(len(class_levels)):
        for n in range(len(class_levels_target_counts_list)):
            if(class_levels[m]==class_levels_target_counts_list[n][0]):
                entropy_value += -(class_levels_target_counts_list[n][2]/(level_occurences[m])) * math.log((class_levels_target_counts_list[n][2]/(level_occurences[m])),2)
        entropy_for_levels.append(entropy_value)
        entropy_value=0
    entropy_for_attribute = 0
    for entropy in range(len(entropy_for_levels)):
        entropy_for_attribute += entropy_for_levels[entropy]*probability_list[entropy]
    return entropy_for_attribute 
 

def Overall_Collection(target):
    target_list = list(data_frame[target]) 
    zero_counts = target_list.count(0)
    one_counts = target_list.count(1)
    total_count = len(target_list)
    gini_index_value = 1 - ((zero_counts/total_count)**2 +(one_counts/total_count)**2)
    entropy_value = - ((zero_counts/total_count)* math.log(zero_counts/total_count,2)) - ((one_counts/total_count)* math.log(one_counts/total_count,2)) 
    return gini_index_value, entropy_value

#Part a

print("")
print("Gini Index Value for the overall collection --> ",(Overall_Collection("target")[0]))
print("")
print("Entropy Value for the overall collection --> ",(Overall_Collection("target")[1]))
print("-------------------------------------------")

#Part b

print("")
print("Gini Index Value for age attribute --> ",GiniIndex("age"))
print("")
print("Entropy Value for age attribute --> ",Entropy("age"))
print("-------------------------------------------")
#Part c

print("")
print("Gini Index Value for cp attribute --> ",GiniIndex("cp"))
print("")
print("Entropy Value for cp attribute --> ",Entropy("cp"))
print("-------------------------------------------")

#Part d

print("")
print("Gini Index Value for trestbps attribute --> ",GiniIndex("trestbps"))
print("")
print("Entropy Value for trestbps attribute --> ",Entropy("trestbps"))
print("-------------------------------------------")











