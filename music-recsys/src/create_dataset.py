import random
from datetime import datetime, timedelta
import pandas as pd
from collections import Counter


# I wanted to use my own history data, but it takes up to 30 days for Spotify to process the request.
# therefore, I just generate some random play_history data for different users, considering 10 different genres, 20 different artists and 500 different songs compiled from the internet
# I randomly assign each user to 1 to 5 favourite genres, and they create their playlists based on the song database I created.
# This data is then going to be used to recommend similar users and songs for each user.

# load song list
df = pd.read_csv('../data/songs.csv')
# Create a list of all genres and songs
genres = df['Genre'].unique().tolist()
songs = df[['Title', 'Artist', 'Genre', 'Length (seconds)']].values.tolist()

# Names of the users
user_names = ["Alice", "Bob", "Charlie", "David", "Emily", "Frank", "Grace", "Hannah", "Ivy", "Jack", "Karen", "Liam", "Monica", "Nancy", "Oliver", "Paul", "Quincy", "Rachel", "Steve", "Tom"]

# define User Preferences
user_preferences = {}
for user in user_names:
    user_preferences[user] = random.sample(genres, random.randint(1, 5))


# generate the Data
for user in user_names:
    user_songs_ratings = {}  # To keep track of user's ratings for specific songs
    with open(f'../data/{user}_music_history.csv', 'w') as file:
        file.write("Song,Artist,Length,Genre,Datetime,Star_Rating\n")
        for i in range(random.randint(20,100)):
            # Selecting songs based on user preference
            song_name, artist, genre, length = random.choice([song for song in songs if song[2] in user_preferences[user]])
            listened_datetime = datetime.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 23), minutes=random.randint(0, 59))
            
            # Assigning star rating
            if (song_name, artist) in user_songs_ratings:
                star_rating = user_songs_ratings[(song_name, artist)]
            else:
                star_rating = random.randint(1, 5)
                user_songs_ratings[(song_name, artist)] = star_rating
            
            # Increase the star rating for repeated songs
            if star_rating < 5:
                star_rating += 1
                user_songs_ratings[(song_name, artist)] = star_rating
            
            file.write(f"{song_name},{artist},{length},{genre},{listened_datetime},{star_rating}\n")
        
