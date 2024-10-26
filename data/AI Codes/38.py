class Movie:
    def __init__(self, title, year, watched=False):
        self.title = title
        self.year = year
        self.watched = watched

    def __str__(self):
        status = "Watched" if self.watched else "Not Watched"
        return f"{self.title} ({self.year}) - {status}"

class MovieTracker:
    def __init__(self):
        self.movies = []

    def add_movie(self, title, year):
        self.movies.append(Movie(title, year))

    def mark_as_watched(self, title):
        for movie in self.movies:
            if movie.title == title:
                movie.watched = True
                print(f"Marked '{title}' as watched.")
                return
        print("Movie not found.")

    def list_movies(self):
        for movie in self.movies:
            print(movie)

def main():
    tracker = MovieTracker()
    while True:
        print("\n1. Add Movie")
        print("2. Mark Movie as Watched")
        print("3. List Movies")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '4':
            break
        elif choice == '1':
            title = input("Enter movie title: ")
            year = int(input("Enter movie year: "))
            tracker.add_movie(title, year)
        elif choice == '2':
            title = input("Enter movie title to mark as watched: ")
            tracker.mark_as_watched(title)
        elif choice == '3':
            tracker.list_movies()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
