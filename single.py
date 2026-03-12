class Users:
    def __init__(self, name, password, role):
        self.name = name
        self.password = password
        self.role = role

    def userDetail(self):
        print("The name of the user", self.name)
        print("The password of the user", self.password)
        print("The role of the user", self.role)






user1=Users("Akshay","65416516","admin")
user2=Users("Ruby","15151","user")

user1.userDetail()
user2.userDetail()		
