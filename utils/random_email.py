import random
import string

class RandomEmail():
    def generate_random_email():
        chars = string.ascii_letters + string.digits  # a-zA-Z0-9
        username = ''.join(random.choices(chars, k=8))
        return f"{username}@vmuat.com"