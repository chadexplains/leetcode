class Movie:
    def __init__(self, title: str, year: int, price: int):
        self.title = title
        self.year = year
        self.price = price
        self.is_rented = False


class RentalSystem:
    def __init__(self):
        self.movies = {}
        self.available_movies = []
        self.rented_movies = []
        self.prices = {}
        self.heap = []

    def add_movie(self, title: str, year: int, price: int) -> None:
        movie = Movie(title, year, price)
        self.movies[(title, year)] = movie
        self.prices[(title, year)] = price
        self.available_movies.append(movie)
        heapq.heappush(self.heap, (-price, title, year))

    def remove_movie(self, title: str, year: int) -> None:
        movie = self.movies[(title, year)]
        if movie.is_rented:
            self.rented_movies.remove(movie)
        else:
            self.available_movies.remove(movie)
            heapq.heappop(self.heap)
        del self.movies[(title, year)]
        del self.prices[(title, year)]

    def rent_movie(self, title: str) -> None:
        movie = self.movies[title]
        movie.is_rented = True
        self.available_movies.remove(movie)
        self.rented_movies.append(movie)

    def return_movie(self, title: str) -> None:
        movie = self.movies[title]
        movie.is_rented = False
        self.rented_movies.remove(movie)
        self.available_movies.append(movie)
        heapq.heappush(self.heap, (-self.prices[title], title, movie.year))

    def display_available_movies(self) -> List[List[str]]:
        res = []
        for movie in self.available_movies:
            res.append([movie.title, str(movie.year), str(movie.price)])
        return res