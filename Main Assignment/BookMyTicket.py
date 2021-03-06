import pandas as pd

import BasePage

exit_val = False

while exit_val == False:

    login_status = False
    print("""
    ****** Welcome to BookMyShow ******
    1. Login
    2. Register new account
    3. Exit""")

    num = int(input("Enter : "))

    if num == 1:
        print("******Welcome to BookMyShow*******")
        user = input("User: ")
        password = input("Password: ")
        admin_user = BasePage.login_func(user, password)
        if admin_user != "invalid": login_status = True

    elif num == 2:
        print("****Create new Account***** ")
        name, user_details = BasePage.register_func()
        BasePage.user_detail[name] = user_details
        BasePage.user_detail.to_csv("user.csv", index=False)
        continue

    elif num == 3:
        exit_val = True
        continue

    else:
        print("Enter valid input")
        continue

    if admin_user == "invalid":
        print("Invalid username or password")
        continue

    while login_status:
        if admin_user == "admin":
            print("1. Admin  Login:")
            print("******Welcome Admin*******")
            print("1. Add new Movie Info \n"
                  "2. Edit Movie Info \n"
                  "3. Delete Movies \n"
                  "4. Logout")

            opt = int(input("Enter your choice :"))

            if opt == 1:
                print("******Welcome Admin*******")
                title, movie_details = BasePage.Add_movie()
                BasePage.movie_file[title] = movie_details
                BasePage.movie_file.to_csv("movies.csv", index=False)

            elif opt == 2:
                print("******Welcome Admin*******")
                title = input("Movie name")
                title, movie_details = BasePage.Edit_movie(title)
                BasePage.movie_file[title] = movie_details
                BasePage.movie_file.to_csv("movies.csv", index=False)

            elif opt == 3:
                print("******Welcome Admin*******")
                if len(BasePage.movie_file.columns) > 0:
                    title = input("Title of the movie to be deleted: ")
                    del BasePage.movie_file[title]
                    if len(BasePage.movie_file.columns) > 0:
                        BasePage.movie_file.to_csv("movies.csv", index=False)

                else:
                    print("No movies to delete \n")
                    continue

            elif opt == 4:
                login_status = False

            else:
                print("Enter a valid option \n")

        if admin_user == "user":
            print("2. User Login")
            print("******Welcome User1******* ")
            file = pd.read_csv("movies.csv")
            movies = list(file.columns)
            if len(movies) == 0:
                print("No movies currently")
                login_status = False
                continue

            if len(movies) > 1:
                for i in range(0, len(movies), 1):
                    print(i, ". ", movies[i])

                print((i + 1), ". ", "Logout")

            else:
                print("1 . ", movies[0])
                print("2 . Logout \n")

            movie = int(input("Enter movie: "))
            if movie == 2:
                login_status = False
            print(movies[movie - 1])
            func = BasePage.user_display(movies[movie - 1])

            title = movies[movie - 1]

            if func == 1:
                BasePage.book_ticket(title,user)
                login_status = False

            elif func == 2:
                BasePage.cancel_ticket(title, user)
                login_status = False

            elif func == 3:
                print("******Welcome User1*******")
                BasePage.movie_rating(title)
                login_status = False