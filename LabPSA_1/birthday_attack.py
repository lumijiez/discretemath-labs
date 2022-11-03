import hashlib
import os
import binascii

nr_collisions, hashed_dict, strn_table, n = 0, {}, {}, 10
file = open("results.txt", "w")
while n:
    strn = binascii.b2a_hex(os.urandom(16))
    hashed_strn = hashlib.md5(strn).hexdigest()
    sliced_hash = hashed_strn[:10]
    if sliced_hash in hashed_dict:
        nr_collisions += 1
        x = "-----------------------------------------------------------------------------------"
        z = "Collision number: " + str(nr_collisions) + " " * 18 + "Collision: " + str(sliced_hash)
        a = "Hashes: " + " " * 10 + str(hashed_dict[sliced_hash]) + " " + str(hashed_strn)
        b = "Values: " + " " * 10 + strn.decode() + " " + strn_table[sliced_hash].decode()
        file.write(x + "\n" + z + "\n" + a + "\n" + b + "\n")
        n -= 1
    else:
        hashed_dict[sliced_hash] = hashed_strn
        strn_table[sliced_hash] = strn
file.close()
