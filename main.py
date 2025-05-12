from MovieReviewTracker import MovieReviewTracker

movie = MovieReviewTracker()
movie.load_movie_review()

while True:
    print("[1]Add movie\n[2]Show all movie\n[3]Delete movie\n"
          "[4]Show summary\n[5]Edit movie score and comment\n[6]Save and exit\n")
    choice = input("Enter number option\n")

    if choice == "1":
        title = input("Enter movie name: ")
        score = int(input(f"Enter {title} score:"))
        comment = input("Write your comment: ")
        msg = movie.add_movie(title, score, comment)
        print(msg)

    elif choice == "2":
        msg = movie.show_all_review()
        print(msg)

    elif choice == "3":
        title = input("Enter movie name to delete: ")
        msg = movie.delete_movie(title)
        print(msg)

    elif choice == "4":
        msg = movie.show_summary()
        print(msg)

    elif choice == "5":
        title = input("Enter movie name to edit: ")
        new_score = int(input("Enter new score: "))
        new_comment = input("Enter your new comment: ")
        msg = movie.edit_movie(title, new_score, new_comment)
        print(msg)

    elif choice == "6":
        movie.write_movie()
        print("Save complete")
        break