import media
import html_generator

serenity = media.Movie("Serenity",
                       "https://upload.wikimedia.org/wikipedia/en/9/9e/Serenity_One_Sheet.jpg",
                       "https://www.youtube.com/watch?v=bOpYWl1IwBM")

avatar = media.Movie("Avatar",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

matrix = media.Movie("The Matrix",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

hishtk = media.Movie("Honey, I shrunk the kids",
                     "https://upload.wikimedia.org/wikipedia/en/4/4b/Honey_I_Shrunk_the_kids.jpg",
                     "https://www.youtube.com/watch?v=L9nCNJ3cZSk")

home_alone = media.Movie("Home Alone",
                         "https://upload.wikimedia.org/wikipedia/en/7/76/Home_alone_poster.jpg",
                         "https://www.youtube.com/watch?v=IsOlj-xpK9Q")

police_academy = media.Movie("Police Academy",
                             "https://upload.wikimedia.org/wikipedia/en/4/4d/Police_Academy_film.jpg",
                             "https://www.youtube.com/watch?v=4NT4C1F_HZE")

movies = [serenity, avatar, matrix, hishtk, home_alone, police_academy]
html_generator.open_movies_page(movies)
