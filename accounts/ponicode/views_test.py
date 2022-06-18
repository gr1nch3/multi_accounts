from accounts import views

class Test_Views_CreateUser:
    def test_createUser_1(self):
        views.createUser("POST")

    def test_createUser_2(self):
        views.createUser("DELETE")

    def test_createUser_3(self):
        views.createUser("PUT")

    def test_createUser_4(self):
        views.createUser("GET")

    def test_createUser_5(self):
        views.createUser("")

    def test_createUser_6(self):
        views.createUser(None)


class Test_Views_User_detail:
    def test_user_detail_1(self):
        views.user_detail("PUT", "Jean-Philippe")

    def test_user_detail_2(self):
        views.user_detail("POST", "Anas")

    def test_user_detail_3(self):
        views.user_detail("PUT", "Michael")

    def test_user_detail_4(self):
        views.user_detail("POST", "Michael")

    def test_user_detail_5(self):
        views.user_detail("GET", "George")

    def test_user_detail_6(self):
        views.user_detail("", "")


class Test_Views_Home:
    def test_home_1(self):
        views.home("PUT")

    def test_home_2(self):
        views.home("POST")

    def test_home_3(self):
        views.home("GET")

    def test_home_4(self):
        views.home("DELETE")

    def test_home_5(self):
        views.home("")


class Test_Views_CreateStudent:
    def test_createStudent_1(self):
        result = views.createStudent("PUT")

    def test_createStudent_2(self):
        result = views.createStudent("GET")

    def test_createStudent_3(self):
        result = views.createStudent("POST")

    def test_createStudent_4(self):
        result = views.createStudent("DELETE")

    def test_createStudent_5(self):
        result = views.createStudent("")

