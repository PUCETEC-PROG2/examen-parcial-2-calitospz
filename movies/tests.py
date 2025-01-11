from django.test import TestCase
from django.test import TestCase
from .models import Movie

class MovieModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a movie object for testing
        cls.movie = Movie.objects.create(
            title='Inception',
            genre='Sci-Fi',
            director_name='Christopher Nolan',
            publication_year=2010,
            synopsis='A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.'
        )

    def test_movie_title(self):
        self.assertEqual(self.movie.title, 'Inception')

    def test_movie_genre(self):
        self.assertEqual(self.movie.genre, 'Sci-Fi')

    def test_movie_director_name(self):
        self.assertEqual(self.movie.director_name, 'Christopher Nolan')

    def test_movie_publication_year(self):
        self.assertEqual(self.movie.publication_year, 2010)

    def test_movie_synopsis(self):
        self.assertEqual(self.movie.synopsis, 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.')

# Create your tests here.

# Create your tests here.
