import hashlib

target_password = 'Hello World'
password_hash = 'b10a8db164e0754105b7a99be72e3fe5'

entry_password = input('Password: ')

encoded = entry_password.encode('utf-8')
print(encoded)
digest = hashlib.md5(encoded).hexdigest() # get md5 hash of string (string must be encoded first)
print(digest)

if digest == password_hash:
    print('y')
