import ctypes


def decrypt(v, k):
    v0 = v[0]
    v1 = v[1]
    sum = 0xc6ef3720
    delta = 0x9e3779b9
    k0 = k[0]
    k1 = k[1]
    k2 = k[2]
    k3 = k[3]
    for i in range(32):
        v1 -= ((v0 << 4) + k2) ^ (v0 + sum) ^ ((v0 >> 5) + k3)
        v0 -= ((v1 << 4) + k0) ^ (v1 + sum) ^ ((v1 >> 5) + k1)
        sum -= delta
    return [v0, v1]


key = [0, 4, 5, 1]
encrypted_message = [
    ctypes.c_uint(0xe3238557), ctypes.c_uint(0x6204a1f8,
    ctypes.c_uint(0xe6537611), ctypes.c_uint(0x174e5747),
    ctypes.c_uint(0x5d954da8), ctypes.c_uint(0x8c2dfe97),
    ctypes.c_uint(0x2911cb4c), ctypes.c_uint(0x2cb7c66b),
    ctypes.c_uint(0xe7f185a0), ctypes.c_uint(0xc7e3fa40),
    ctypes.c_uint(0x42419867), ctypes.c_uint(0x374044df),
    ctypes.c_uint(0x2519f07d), ctypes.c_uint(0x5a0c24d4),
    ctypes.c_uint(0xf4a960c5), ctypes.c_uint(0x31159418),
    ctypes.c_uint(0xf2768ec7), ctypes.c_uint(0xaeaf14cf),
    ctypes.c_uint(0x071b2c95), ctypes.c_uint(0xc9f22699),
    ctypes.c_uint(0xffb06f41), ctypes.c_uint(0x2ac90051),
    ctypes.c_uint(0xa53f035d), ctypes.c_uint(0x830601a7),
    ctypes.c_uint(0xeb475702), ctypes.c_uint(0x183baa6f),
    ctypes.c_uint(0x12626744), ctypes.c_uint(0x9b75a72f),
    ctypes.c_uint(0x8dbfbfec), ctypes.c_uint(0x73c1a46e),
    ctypes.c_uint(0xffb06f41), ctypes.c_uint(0x2ac90051),
    ctypes.c_uint(0x97c5e4e9), ctypes.c_uint(0xb1c26a21),
    ctypes.c_uint(0xdd4a3463), ctypes.c_uint(0x6b71162f),
    ctypes.c_uint(0x8c075668), ctypes.c_uint(0x7975d565),
    ctypes.c_uint(0x6d95a700), ctypes.c_uint(0x7272e637)
]

decrypted_message = ""

for pair in encrypted_message:
    decrypted_pair = decrypt(pair, key)
    decrypted_message += chr(decrypted_pair[0]) + chr(decrypted_pair[1])

print(decrypted_message)
