import hashlib

hash_object = hashlib.sha1()
hash_object.update(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)

hash_object = hashlib.sha256()
hash_object.update(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)
