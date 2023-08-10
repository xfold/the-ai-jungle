import csv
from datetime import timedelta
import random

# Genres to be equally represented
genres = ["Pop", "Rock", "Hip-Hop", "Techno", "Indie", "Jazz", "Blues", "Country", "Electronic", "Folk"]

# Example artists for each genre
artists = {
    "Pop": ["Britney Spears", "Christina Aguilera", "Justin Timberlake", "Madonna", "Katy Perry", "Taylor Swift"],
    "Rock": ["Coldplay", "U2", "Linkin Park", "Foo Fighters", "Green Day", "The Rolling Stones"],
    "Hip-Hop": ["Eminem", "Jay-Z", "OutKast", "Kanye West", "Nas", "Lil Wayne"],
    "Techno": ["The Chemical Brothers", "Moby", "Daft Punk", "Carl Cox", "Jeff Mills", "Richie Hawtin"],
    "Indie": ["Arcade Fire", "Modest Mouse", "Death Cab for Cutie", "The Shins", "Vampire Weekend", "Arctic Monkeys"],
    "Jazz": ["Miles Davis", "John Coltrane", "Herbie Hancock", "Louis Armstrong", "Ella Fitzgerald", "Billie Holiday"],
    "Blues": ["B.B. King", "Eric Clapton", "Stevie Ray Vaughan", "Muddy Waters", "John Lee Hooker", "Robert Johnson"],
    "Country": ["Johnny Cash", "Dolly Parton", "Willie Nelson", "Garth Brooks", "George Strait", "Reba McEntire"],
    "Electronic": ["Kraftwerk", "Aphex Twin", "Deadmau5", "Skrillex", "Calvin Harris", "Zedd"],
    "Folk": ["Bob Dylan", "Joan Baez", "Simon & Garfunkel", "Joni Mitchell", "Leonard Cohen", "Nick Drake"]
}


songs = []

# Create 300 songs
for i in range(300):
    genre = genres[i % len(genres)]
    artist = random.choice(artists.get(genre, ["Unknown Artist"]))
    title = f"Song{i}"  # You can replace this with real song titles if available
    length = timedelta(minutes=random.randint(2, 5), seconds=random.randint(0, 59))
    songs.append((title, artist, genre, length))

# Write to CSV file
with open('../data/songs.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Artist", "Genre", "Length (seconds)"])
    for song in songs:
        writer.writerow([song[0], song[1], song[2], song[3].total_seconds()])
