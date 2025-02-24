import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from gensim.models import KeyedVectors
from sklearn.decomposition import PCA
import gensim.downloader as api

def plot_word_vectors():
    # Load pre-trained Word2Vec model
    model = api.load('word2vec-google-news-300') # much bigger model
    
    print("Enter words separated by commas e.g. hello, world . Close the generated plot to test a new set of words.")
    
    while True:
        words = input("Enter a words: ")
        words = words.lower().split(', ')

        # Get word vectors
        word_vectors = np.array([model[word] for word in words if word in model])
        valid_words = [word for word in words if word in model]
        
        if len(valid_words) == 0:
            print("No valid words found in the model.")
            continue
        
        # Perform PCA to reduce dimensions to 3
        pca = PCA(n_components=3)
        reduced_vectors = pca.fit_transform(word_vectors)
        
        # Plot in 3D space
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        
        for i, word in enumerate(valid_words):
            ax.scatter(reduced_vectors[i, 0], reduced_vectors[i, 1], reduced_vectors[i, 2])
            ax.text(reduced_vectors[i, 0], reduced_vectors[i, 1], reduced_vectors[i, 2], word)
        
        ax.set_xlabel('PC1')
        ax.set_ylabel('PC2')
        ax.set_zlabel('PC3')
        ax.set_title("Word Embeddings PCA Projection")
        plt.show()


plot_word_vectors()
