class Movie():


    def __init__(self, movie_title, poster_image, trailer_youtube):
        """
        Main constructor of the class Movie, which takes the information from
        entartainment_center.py as an input and defines its behaviour for
        further work with html_generator.py
        """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
