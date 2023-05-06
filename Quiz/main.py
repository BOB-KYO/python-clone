class User: # 클래스 네이밍 파스칼 케이스로 입력(주로 파이썬) 캐멜 케이스, 스네이크 케이스
    def __init__(self,user_id, user_name):
        self.id = user_id # id attribute
        self.name = user_name # name attribute
        self.followers = 0 # 값이 초기화 되어있기때문에 제외
        self.following = 0
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001","Kyoseok")
print(user_1.id, user_1.name,user_1.followers)

user_2 = User("002", "Helen")
print(user_2.id,user_2.name,user_2.followers)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


