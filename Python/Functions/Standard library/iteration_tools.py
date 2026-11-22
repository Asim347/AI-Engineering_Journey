from itertools import chain

dataset1 = ['python','Machine learninig']
dataset2 = ['Java','C sharp','C++','C']
combined = chain(dataset1,dataset2)
print(list(combined))


from itertools import combinations

algorithms = ['SVM','Decision Tree','Random Forest']

groups = combinations(algorithms,2)
print(list(groups))

techniques = ['Normalization','Tokenization','Stemming','Lemmatization']
grouping = combinations(techniques,2)
for pair in grouping:
    print(pair)