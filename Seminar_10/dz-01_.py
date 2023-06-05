# import pandas as pd
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# print(lst)
# random.shuffle(lst)
# data = pd.DataFrame(lst)
# print(data.head())

# dict = {"0": "robot", "1": "human"}
# print(dict)

# # print(dict["robot"][0])
# one_hot = []
# # for i in range (len(data)):
# #     dict.get(key[default])
# #     print(dict.get(key[data[i]]))


# onehot_encoded = list() 
# for value in data:
#     elt = [0 for _ in range(len(lst))] 
#     elt[value] = 1 
#     onehot_encoded.append(elt) 
# print(onehot_encoded) 
# # invert encoding 
# # inverted = int_to_char[argmax(onehot_encoded[0])] 
# # print(inverted) 


# # from numpy import argmax 
# # # Here we are define input string 
# # str_data = 'hello python' 
# # print(str_data) 
# # # Here we are defining possible input values of english alphabate 
# # eng_alphabet = 'abcdefghijklmnopqrstuvwxyz ' 
# # # define a mapping of chars to integers 
# # char_to_int = dict((c, i) for i, c in enumerate(eng_alphabet)) 
# # int_to_char = dict((i, c) for i, c in enumerate(eng_alphabet)) 
# # # input data is encoding in integer 
# # int_encoded = [char_to_int[char] for char in data] 
# # print(int_encoded) 
# # # one hot encode 
# # onehot_encoded = list() 
# # for value in int_encoded: 
# #   letter = [0 for _ in range(len(eng_alphabet))] 
# #   letter[value] = 1 
# #   onehot_encoded.append(letter) 
# # print(onehot_encoded) 
# # # invert encoding 
# # inverted = int_to_char[argmax(onehot_encoded[0])] 
# # print(inverted) 
