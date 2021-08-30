{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "# libraries for making count matrix and similarity matrix\n",
    "from sklearn.feature_extraction.text import CountVectorizer\n",
    "from sklearn.metrics.pairwise import cosine_similarity\n",
    "\n",
    "# reading the data from the preprocessed .csv file\n",
    "data = pd.read_csv('data.csv')\n",
    "\n",
    "# making the new column containing combination of all the features\n",
    "data['combination'] = data['actor_1_name'] + ' ' + data['actor_2_name'] + ' '+ data['actor_3_name'] + ' '+ data['director_name'] +' ' + data['genres']\n",
    "\n",
    "\n",
    "# creating a count matrix\n",
    "cv = CountVectorizer()\n",
    "count_matrix = cv.fit_transform(data['combination'])\n",
    "\n",
    "# creating a similarity score matrix\n",
    "similarity = cosine_similarity(count_matrix)\n",
    "\n",
    "# saving the similarity score matrix in a file for later use\n",
    "np.save('similarity_matrix', similarity)\n",
    "\n",
    "# saving dataframe to csv for later use in main file\n",
    "data.to_csv('data.csv',index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
