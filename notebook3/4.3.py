import ctypes


def decrypt(v, k):
    y, z = [ctypes.c_uint32(x)
            for x in v]
    sum = ctypes.c_uint32(0xC6EF3720)
    delta = 0x9E3779B9

    for n in range(32, 0, -1):  # 1
        z.value -= (y.value << 4) + k[2] ^ y.value + sum.value ^ (y.value >> 5) + k[3]
        y.value -= (z.value << 4) + k[0] ^ z.value + sum.value ^ (z.value >> 5) + k[1]
        sum.value -= delta

    return [y.value, z.value]  # возврат расшифрованных значений y и z в виде списка


k = [0, 4, 5, 1]
message = "E3238557 6204A1F8 E6537611 174E5747 5D954DA8 8C2DFE97 2911CB4C 2CB7C66B " \
          "E7F185A0 C7E3FA40 42419867 374044DF 2519F07D 5A0C24D4 F4A960C5 31159418 " \
          "F2768EC7 AEAF14CF 071B2C95 C9F22699 FFB06F41 2AC90051 A53F035D 830601A7 " \
          "EB475702 183BAA6F 12626744 9B75A72F 8DBFBFEC 73C1A46E FFB06F41 2AC90051 " \
          "97C5E4E9 B1C26A21 DD4A3463 6B71162F 8C075668 7975D565 6D95A700 7272E637"

'''После того, как все блоки зашифрованных данных были обработаны и расшифрованы, из списка result извлекаются числа, 
которые интерпретируются как коды символов ASCII и склеиваются в единую строку. 
Расшифрованная строка выводится на экран.'''

k = [0, 4, 5, 1]

message = message.split(' ')
result = []
for i in range(1, len(message), 2):
    block1 = ctypes.c_uint32(int(message[i - 1], 16)).value
    block2 = ctypes.c_uint32(int(message[i], 16)).value
    result.extend(decrypt([block1, block2], k))
print("".join(map(chr, result)))