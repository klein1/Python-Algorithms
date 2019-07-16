class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

# 原来的顺序
users = [User(19), User(17), User(18)]
print(users)  # [User(19), User(17), User(18)]

# 根据 user_id 排序
print(sorted(users, key=lambda u: u.user_id))  # [User(17), User(18), User(19)]
# 使用内置函数 operator.attrgetter()
from operator import attrgetter
print(sorted(users, key=attrgetter('user_id')))  # [User(17), User(18), User(19)]