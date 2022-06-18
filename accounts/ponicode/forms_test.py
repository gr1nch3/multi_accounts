from accounts import forms
import pytest

class Test_Teacherform_Save:
    
    @pytest.fixture()
    def teacherform(self):
        return forms.TeacherForm()
    

    def test_save_1(self, teacherform):
        teacherform.save("commit 03ccef2ffa982df061ae86ca8730cd9ad0af05b3\r\nAuthor: Ladarius Zboncak <Ricky.Schultz37@hotmail.com>\r\nDate: Wed Jul 28 2021 16:52:11 GMT+0200 (Central European Summer Time)\r\n\r\n    program wireless program\r\n")

    def test_save_2(self, teacherform):
        teacherform.save("commit 380428b6b61b64631d941b27db3e91df27bfff8e\r\nAuthor: Lera Swift <Lela.Lubowitz@yahoo.com>\r\nDate: Wed Jul 28 2021 23:21:29 GMT+0200 (Central European Summer Time)\r\n\r\n    reboot digital application\r\n")

    def test_save_3(self, teacherform):
        teacherform.save("commit e6d1117d97e7cc250166120d2eee1c2662c58150\r\nAuthor: Keagan Cole <Crystal69@gmail.com>\r\nDate: Thu Jul 29 2021 05:36:16 GMT+0200 (Central European Summer Time)\r\n\r\n    override wireless alarm\r\n")

    def test_save_4(self, teacherform):
        teacherform.save("commit d3f6bf9bcee016096098e88aced2d5afdc68c424\r\nAuthor: Edna Rice <Shanie.Pagac@yahoo.com>\r\nDate: Wed Jul 28 2021 22:05:49 GMT+0200 (Central European Summer Time)\r\n\r\n    bypass cross-platform hard drive\r\n")

    def test_save_5(self, teacherform):
        teacherform.save("commit f20ba84baadcbd1f3a45d95e9bb5aef588f4e902\r\nAuthor: Marty Douglas <Rubie_Boehm29@yahoo.com>\r\nDate: Thu Jul 29 2021 09:06:18 GMT+0200 (Central European Summer Time)\r\n\r\n    override solid state microchip\r\n")

    def test_save_6(self, teacherform):
        teacherform.save("")


class Test_Userform_Save:
    
    @pytest.fixture()
    def userform(self):
        return forms.UserForm()
    

    def test_save_1(self, userform):
        result = userform.save("commit e6d1117d97e7cc250166120d2eee1c2662c58150\r\nAuthor: Keagan Cole <Crystal69@gmail.com>\r\nDate: Thu Jul 29 2021 05:36:16 GMT+0200 (Central European Summer Time)\r\n\r\n    override wireless alarm\r\n")

    def test_save_2(self, userform):
        result = userform.save("commit 380428b6b61b64631d941b27db3e91df27bfff8e\r\nAuthor: Lera Swift <Lela.Lubowitz@yahoo.com>\r\nDate: Wed Jul 28 2021 23:21:29 GMT+0200 (Central European Summer Time)\r\n\r\n    reboot digital application\r\n")

    def test_save_3(self, userform):
        result = userform.save("commit 03ccef2ffa982df061ae86ca8730cd9ad0af05b3\r\nAuthor: Ladarius Zboncak <Ricky.Schultz37@hotmail.com>\r\nDate: Wed Jul 28 2021 16:52:11 GMT+0200 (Central European Summer Time)\r\n\r\n    program wireless program\r\n")

    def test_save_4(self, userform):
        result = userform.save("commit f20ba84baadcbd1f3a45d95e9bb5aef588f4e902\r\nAuthor: Marty Douglas <Rubie_Boehm29@yahoo.com>\r\nDate: Thu Jul 29 2021 09:06:18 GMT+0200 (Central European Summer Time)\r\n\r\n    override solid state microchip\r\n")

    def test_save_5(self, userform):
        result = userform.save("commit d3f6bf9bcee016096098e88aced2d5afdc68c424\r\nAuthor: Edna Rice <Shanie.Pagac@yahoo.com>\r\nDate: Wed Jul 28 2021 22:05:49 GMT+0200 (Central European Summer Time)\r\n\r\n    bypass cross-platform hard drive\r\n")

    def test_save_6(self, userform):
        result = userform.save("")

