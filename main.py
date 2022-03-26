from matplotlib import pyplot as plt
import numpy as np

documents = ["Text_{}".format(i + 1) for i in range(10)]
counts = [0 for i  in range(10)]
words = {}
data = list()
top1 = list()
top2 = list()

for i in range(10):
    with open("text_{}.txt".format(i + 1), "r") as file:
        lines = file.readlines()
        for line in lines:
            row = list(line.split())
            counts[i] += len(row)
            for word in row:
                words[word] = words.get(word, 0) + 1
for key, value in words.items():
    data.append([key, value]) 
for i in range(len(data) - 1):
    for j in range(len(data) - 1 - i):
        if (data[j][1] < data[j + 1][1]):
            temp = data[j]
            data[j] = data[j + 1]
            data[j + 1] = temp
for i in range(10):
    top1.append(data[i][0])
    top2.append(data[i][1])
		
print("The number of words:", sum(counts))

fig = plt.figure(figsize =(10, 7))
plt.pie(top2, labels = documents)
plt.show()

fig = plt.figure(figsize = (10, 5))
plt.bar(top1, top2, color ='green', width = 0.4)
plt.xlabel("10 most popular words")
plt.ylabel("Times repeated")
plt.title("Texts' analysis")
plt.show()