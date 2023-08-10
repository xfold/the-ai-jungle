import pandas as pd
import glob
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm

def load_dataset():
    # Define a list to hold data from all files
    all_data = []

    # Iterate through all CSV files matching the pattern
    for filename in glob.glob('data/*_music_history.csv'):
        df = pd.read_csv(filename)
        user_name = filename.split('_')[0].split('\\')[1]
        df['User_Name'] = user_name
        all_data.append(df)

    # Concatenate all DataFrames in the list into a single DataFrame
    return pd.concat(all_data)

def load_songs_data():
    # Define a list to hold data from all files
    df = pd.read_csv('data/songs.csv')
    return df


def summarize_clusters(dataframe, kmeans_clusters, user_song_matrix):
    # Get all unique genres and map them to colors
    unique_genres = dataframe['Genre'].unique()
    colors = cm.get_cmap('tab10', len(unique_genres))
    genre_color_map = {genre: colors(i) for i, genre in enumerate(unique_genres)}

    # Iterate over each unique cluster
    for cluster_num in range(max(kmeans_clusters) + 1):
        print(f"Processing cluster number: {cluster_num}")
        users_in_cluster = user_song_matrix[user_song_matrix['kmeans_cluster_silhouette'] == cluster_num].index.tolist()
        print(f"Users in cluster: {users_in_cluster}")

        if not users_in_cluster:
            print(f"No users found in cluster {cluster_num}. Skipping...")
            continue
        
        # Filter the original dataframe to only include the users in the current cluster
        cluster_data = dataframe[dataframe['User_Name'].isin(users_in_cluster)]
        
        fig, axes = plt.subplots(1, 5, figsize=(20, 4))
        
        # 1- Pie of genres
        genre_counts = cluster_data['Genre'].value_counts()
        genre_colors = [genre_color_map[genre] for genre in genre_counts.index]
        axes[0].pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', colors=genre_colors)
        axes[0].set_title('Genre Distribution')

        # 2- Top 10 most listened songs
        top_songs = cluster_data['Song'].value_counts().nlargest(10).plot(kind='bar', ax=axes[1])
        axes[1].set_title('Top 10 Songs')

        # 3- Histogram of star_rating scores
        cluster_data['Star_Rating'].plot(kind='hist', ax=axes[2])
        axes[2].set_title('Star Rating Distribution')

        # 4- Boxplot of star ratings, song time, and score
        cluster_data[['Star_Rating', 'Length']].plot(kind='box', ax=axes[3])
        axes[3].set_title('Ratings and Length Boxplots')

        # 5- Names of the users
        axes[4].text(0.5, 0.5, '\n'.join(users_in_cluster), ha='center', va='center')
        axes[4].set_title('Users in Cluster')
        axes[4].axis('off')  # Hide axes for this plot
        
        plt.show()