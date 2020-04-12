import Encryption as ec

msg_to_encrypt = "THE Romans are Coming"


print("ENCRYPTING....")

encrypted = ec.encrypt(msg_to_encrypt, 12)

print(encrypted)

print("DECRYPTING....")

ec.brute_force(encrypted)
