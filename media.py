import webbrowser

class Movie():
    def __init__(self, title_movie, director_movie, trailer_movie, image_movie):
        self.title = title_movie
        self.director = director_movie
        self.trailer_url = trailer_movie
        self.img_movie_url = image_movie

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
