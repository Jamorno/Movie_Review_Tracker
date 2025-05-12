import json

class MovieReviewTracker:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie_name, score, comment):
        for movie in self.movies:
            if movie["movie_name"] == movie_name:
                return f"{movie_name} already exits."

        new_movie = {
            "movie_name": movie_name,
            "score": score,
            "comment": comment
        }

        self.movies.append(new_movie)
        return f"Added new movie: {movie_name}"

    def show_all_review(self):
        if not self.movies:
            return "No movie found"

        lines = []
        for movie in self.movies:
            name = movie["movie_name"]
            score = movie["score"]
            comment = movie["comment"]
            lines.append(f"{name}: {score} - {comment}")
        return "\n".join(lines)

    def delete_movie(self, movie_name):
        for movie in self.movies:
            if movie["movie_name"] == movie_name:
                self.movies.remove(movie)
                return f"Deleted - {movie_name}"
        return f"Not found {movie_name}"

    def edit_movie(self, movie_name, new_score, new_comment):
        for movie in self.movies:
            if movie["movie_name"] == movie_name:
                movie["score"] = new_score
                movie["comment"] = new_comment
                return f"Updated {movie_name} score: {new_score} comment: {new_comment}"
        return f"Not found {movie_name}"

    def show_summary(self):
        if not self.movies:
            return "No movie yet."

        total = sum(movie["score"] for movie in self.movies)
        top_movie = max(self.movies, key=lambda x: x["score"])

        return (
            f"Total movie score = {total}\n"
            f"Top movie score is {top_movie["movie_name"]}({top_movie["score"]})"
        )


    def write_movie(self):
        with open("movie_review.json", "w") as file:
            json.dump(self.movies, file)

    def load_movie_review(self):
        try:
            with open("movie_review.json", "r") as file:
                self.movies = json.load(file)
        except FileNotFoundError:
            self.movies = []