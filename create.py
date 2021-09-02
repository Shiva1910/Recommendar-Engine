import pandas as pd
import numpy as np
# libraries for making count matrix and similarity matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# reading the data from the preprocessed .csv file
data2 = pd.read_csv('data2.csv')

# making the new column containing combination of all the features
data2['combination'] = data2['actor_1_name'] + ' ' + data2['actor_2_name'] + ' '+ data2['actor_3_name'] + ' '+ data2['director_name'] +' ' + data2['genres']


# creating a count matrix
cv = CountVectorizer()
count_matrix = cv.fit_transform(data2['combination'])

# creating a similarity score matrix
similarity = cosine_similarity(count_matrix)

# saving the similarity score matrix in a file for later use
np.save('similarity_matrix', similarity)

# saving dataframe to csv for later use in main file
data2.to_csv('data2.csv',index=False)
