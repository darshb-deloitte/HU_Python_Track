import pandas as pd

try:
    movie_file = pd.read_csv("movies.csv")
except Exception:
    movie_file = pd.DataFrame()

try:
    admin_detail = pd.read_csv("admin.csv")
except Exception:
    admin_detail = pd.DataFrame()

try:
    user_detail = pd.read_csv("user.csv")
except Exception:
    user_detail = pd.DataFrame()


def register_func():
    name = input("Name :")
    email = input("Email :")
    phone = input("Phone :")
    age = input("Age :")
    password = input("Password :")

    lis = [email, phone, age, password]
    return name, lis


def Edit_movie(title):
    # title = input("Title [{}] :".format(title))
    print("Title :", title)
    genre = input("Genre [{}] :".format(movie_file[title][0]))
    duration = input("Length [{}] :".format(movie_file[title][1]))
    cast = input("Cast [{}] :".format(movie_file[title][2]))
    director = input("Director [{}] :".format(movie_file[title][3]))
    admin_rating = input("Admin Rating [{}] :".format(movie_file[title][4]))
    lang = input("Language [{}] :".format(movie_file[title][5]))
    timing_string = input("Timing [{}] :".format(movie_file[title][6]))
    timing = list(timing_string.split(","))
    # no_of_shows = input("Number of shows :")
    no_of_shows = len(timing)
    print("Number of shows in a day :", no_of_shows)
    first_show = input("First Show [{}] :".format(movie_file[title][8]))
    interval_time = input("Interval Time [{}] :".format(movie_file[title][9]))
    gap_btw_show = input("Gap Between Shows [{}] :".format(movie_file[title][10]))
    capacity = input("Capacity [{}] :".format(movie_file[title][11]))

    lis = [genre, duration, cast, director, admin_rating, lang, timing, no_of_shows, first_show, interval_time,
           gap_btw_show, capacity]

    return title, lis


def Add_movie():
    title = input("Title :")
    genre = input("Genre :")
    duration = input("Length :")
    cast = input("Cast :")
    director = input("Director :")
    admin_rating = input("Admin Rating :")
    lang = input("Language :")
    timing_string = input("Timing :")
    timing = list(timing_string.split(","))
    # no_of_shows = input("Number of shows :")
    no_of_shows = len(timing)
    print("Number of shows in a day:", no_of_shows)
    first_show = input("First Show :")
    interval_time = input("Interval Time :")
    gap_btw_show = input("Gap Between Shows :")
    capacity = input("Capacity :")

    lis = [genre, duration, cast, director, admin_rating, lang, timing, no_of_shows, first_show, interval_time,
           gap_btw_show, capacity]

    return title, lis


def login_func(user, password):
    admins = list(admin_detail.columns)
    users = list(user_detail.columns)

    if (user in users) and (user_detail[user][3] == password):
        return "user"

    elif (user in admins) and (admin_detail[user][0] == password):
        return "admin"

    else:
        return "invalid"


def user_display(title):
    lis = list(movie_file[title])

    print("Title :", title, "\n"
                            "Genre :", lis[0], "\n"
                                               "Length", lis[1], "\n"
                                                                 "Cast :", lis[2], "\n"
                                                                                   "Director :", lis[3], "\n"
                                                                                                         "Admin :",
          lis[4], "\n"
                  "Timings :", lis[5], "\n"
                                       "User Rating :", lis[6])

    func = int(input("1. Book Tickets \n"
                     "2. Cancel Tickets \n"
                     "3. Give User Rating"))

    return func


def ratings():
    movies = ("RRR", "83", "RX100")
    for movie in movies:
        print("Rating For Movie:", movie)
        for i in range(len(movies)):
            rating = int(input("Enter Movie rating: "))
            if rating < 1 or rating > 10:
                print("That's not a Valid number")
                continue
            break


def book_ticket(title):
    lis = list(movie_file[title])
