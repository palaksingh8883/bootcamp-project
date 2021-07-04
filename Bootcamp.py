import hashlib
mystring = input('Enter string to hash: ')
obj = hashlib.md5(mystring.encode())
print(obj.hexdigest())