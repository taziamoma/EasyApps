import random
import string


def password_generator(size, chars=string.ascii_letters + string.digits + string.punctuation):
    password = ''.join(random.choice(chars) for _ in range(size))
    return password


# print(password_generator(20))

print(2/2)