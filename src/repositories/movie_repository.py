from src.models import Movie, db


class MovieRepository:

    def get_all_movies(self):
        all_movies: list[Movie] = Movie.query.all()
        return all_movies

    def get_movie_by_id(self, movie_id: int):
        found_movie: Movie = Movie.query.get_or_404(movie_id)
        return found_movie

    def create_movie(self, title: str, director: str, rating: int):
        new_movie = Movie(title=title, director=director, rating=rating)
        db.session.add(new_movie)
        db.session.commit()
        return new_movie

    def search_movies(self, title):
        found_movies: list[Movie] = Movie.query.filter(Movie.title.ilike(f'%{title}%')).all()
        return found_movies


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
