import webbrowser

# Movie class that creates movie objects with a title, summary,img,and ability to play its movie trailer
class Movie():
    """Class used to store movie information"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # uses webbrowser to open the objects saved youtube url
    def play_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
