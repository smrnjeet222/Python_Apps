# pip install passlib

from passlib.hash import pbkdf2_sha512


def hash_password(password):
    return pbkdf2_sha512.using(rounds=5, salt_size=3).hash(password)


def check_hashde_pass(password, hashed_password):
    return pbkdf2_sha512.verify(password, hashed_password)


m_password = 'admin123'  # PS. don't use these dumb passwords

hashed = hash_password(m_password)

print(hashed)

if check_hashde_pass('admin123', hashed):
    print('VALID PASSWORD')
else:
    print("INVALID PASSWORD")
