def ratings():
    movies = ("RRR", "83", "RX100")
    for movie in movies:
        print("Rating For Movie:", movie)
        rating = 0

        # while rating > 1 or rating < 10:
        for i in range(len(movies)):
            rating = int(input("Enter Movie rating"))
            if rating < 1 or rating > 5:
                print("That's not a Valid number")
                continue

            break

        print("*" * rating)

ratings()
