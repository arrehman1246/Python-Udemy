albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1
while True:
    print("Please choose an album (invalid choice exits")
    for index, (title, artist, year, songs) in enumerate(albums):
        print(f"{index + 1}: {title}")

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break

    print("Please choose a song (invalid choice take you back to albums")
    for index, (song_track, song) in enumerate(songs_list):
        print(f"{index + 1}: {song}")

    choice = int(input())
    if 1 <= choice <= len(songs_list):
        title = songs_list[choice - 1][SONG_TITLE_INDEX]
        print(f"Playing {title}")
    print("=" * 40)

