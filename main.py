{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "from flask import Flask, render_template, request\n",
    "# libraries for making count matrix and similarity matrix\n",
    "from sklearn.feature_extraction.text import CountVectorizer\n",
    "from sklearn.metrics.pairwise import cosine_similarity\n",
    "\n",
    "# define a function that creates similarity matrix\n",
    "# if it doesn't exist\n",
    "def create_similarity():\n",
    "    data = pd.read_csv('data.csv')\n",
    "    # creating a count matrix\n",
    "    cv = CountVectorizer()\n",
    "    count_matrix = cv.fit_transform(data['combination'])\n",
    "    # creating a similarity score matrix\n",
    "    similarity = cosine_similarity(count_matrix)\n",
    "    return data,similarity\n",
    "\n",
    "\n",
    "# defining a function that recommends 10 most similar movies\n",
    "def rec(m):\n",
    "    m = m.lower()\n",
    "    # check if data and sim are already assigned\n",
    "    try:\n",
    "        data.head()\n",
    "        similarity.shape\n",
    "    except:\n",
    "        data, similarity = create_similarity()\n",
    "    # check if the movie is in our database or not\n",
    "    if m not in data['movie_title'].unique():\n",
    "        return('This movie is not found in database.\\nPlease check if you spelled it correct.')\n",
    "    else:\n",
    "        # getting the index of the movie in the dataframe\n",
    "        i = data.loc[data['movie_title']==m].index[0]\n",
    "\n",
    "        # fetching the row containing similarity scores of the movie\n",
    "        # from similarity matrix and enumerate it\n",
    "        lst = list(enumerate(similarity[i]))\n",
    "\n",
    "        # sorting this list in decreasing order based on the similarity score\n",
    "        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)\n",
    "\n",
    "        # taking top 1- movie scores\n",
    "        # not taking the first index since it is the same movie\n",
    "        lst = lst[1:11]\n",
    "\n",
    "        # making an empty list that will containg all 10 movie recommendations\n",
    "        l = []\n",
    "        for i in range(len(lst)):\n",
    "            a = lst[i][0]\n",
    "            l.append(data['movie_title'][a])\n",
    "        return l\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route(\"/\")\n",
    "def home():\n",
    "    return render_template('home.html')\n",
    "\n",
    "@app.route(\"/recommend\")\n",
    "def recommend():\n",
    "    movie = request.args.get('movie')\n",
    "    r = rec(movie)\n",
    "    movie = movie.upper()\n",
    "    if type(r)==type('string'):\n",
    "        return render_template('Final.html',movie=movie,r=r,t='s')\n",
    "    else:\n",
    "        return render_template('Final.html',movie=movie,r=r,t='l')\n",
    "\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run()"
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
   "name": ""
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
