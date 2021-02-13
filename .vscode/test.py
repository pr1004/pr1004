import bcrypt
password = '1234'
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
print(bcrypt.gensalt())
decode_password = hashed_password
a = hashed_password.decode('utf-8')
print(a)
c = '1234'
print(bcrypt.checkpw(c.encode('utf-8'), a.encode('utf-8')))