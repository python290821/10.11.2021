class TvShow():
    def __init__(self, title, genre, seasons, platforms, actors):
        self.title = title
        self.genre = genre
        self.seasons = seasons
        self.platforms = platforms
        self.actors = actors

friends = TvShow('friends', 'comedy', 13, 'NBC', \
                 ['david schwimmer', 'Matt LeBlanc',
                  'Matthew Perry',
                  'Jennifer Aniston', 'Courteney Cox'])

print(vars(friends)) # same as print(friends.__dict__)

