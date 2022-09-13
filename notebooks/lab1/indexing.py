from doctest import master
import os
import regex as re
import pickle
from typing import DefaultDict

ray = [1,1,2,3]

for i in range(len(ray)-1):
    print(i)


# master_dict = dict()
# master_dict["hek"] =  {"file.txt": [1,2,3], "file2.txt" : [3,76] }
# master_dict["tja"] =  {"file.txt": [1,2,3], "file3.txt" : [3,76] }

# files = ["hej.txt", "sad.txt", "bok.txt"]
# words = ["hej", "tjena", "hej"]

# print(len(master_dict["hek"]["file.txt"]))

# print(len(master_dict["hek"].values()))

# print("okokok", "file.txt" in master_dict["hek"])

# ray = [1,1,2,3]
# print(len(set(ray)))

# * läs in hela filen och regex till array -> len
# * iterera hela dict och räkna arrayen av occurences till f



# w = "Tjena längesedan, ska vi ta en öl elr va säger du?"

# print(w[6:16])


# ["word1": [pos1, pos2], ]

# x = {'en': [1, 2], 'tva': [2, 3]}

# print(x)

# for w in x:
#     print(w, " ", x.get(w))


# if(master_dict["hek"]["1"])


# for f in files:
#     for w in words:
#         if w not in master_dict:
#             master_dict[w] = {f : [1,2,3]}
#         else:  master_dict[w].update({f : [1,2,3]})

# # master_dict["hej"]["hello.txt"] = [1,2,3]

# # master_dict.update({"sad":[1,2,3]})
# print(master_dict)


# wordDict = dict()
# path = os.path.join("Selma", "bannlyst.txt")
# try:
#     f = open(path, "r", encoding='utf-8')
# except:
#     pass

# 1. extract words
# content = f.read()
# str =  re.sub("\W\s"," ", content).lower()
# allWords = set(str.split(" "))

# for word in allWords:
#     wordDict[word] = []
#     for match in re.finditer(rf'\b{word}\b', str):
#         wordDict[word].append(match.start())

# pickle.dump(wordDict, open("save.p", "wb"))

# reading the content of a folder
