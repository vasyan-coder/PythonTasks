def decode_val(c):
    message = []
    for j in range(len(c)):
        one = 0
        nul = 0
        tmp = '0b'
        item = c[j]
        for i in range(2, len(item), 3):
            slice_item = item[i: i + 3]
            for k in range(0, 3):
                if slice_item[k] == '0':
                    nul += 1
                else:
                    one += 1
            if nul > one:
                tmp += '0'
                nul = 0
                one = 0
            else:
                tmp += '1'
                nul = 0
                one = 0
        message.append(tmp)
    return message


def decode(a):
    message = []
    for i in range(len(a)):
        tmp = bin(a[i])
        str = ""
        if len(tmp[2:]) % 3 == 1:
            str += "0b" + '00' + tmp[2:]
            message.append(str)
        elif len(tmp[2:]) % 3 == 2:
            str += "0b" + '0' + tmp[2:]
            message.append(str)
        else:
            str += tmp
            message.append(str)
            new_message = decode_val(message)
    for i in range(len(new_message)):
        item = new_message[i]
        item_int = int(item[2:], 2)
        new_message[i] = chr(item_int)
    return new_message


values = [815608, 2064837, 2093080, 2063879, 196608, 2067983, 10457031, 1830912, 2067455, 2093116, 1044928, 2064407,
          6262776, 2027968, 4423680, 2068231, 2068474, 1999352, 1019903, 2093113, 2068439, 2064455, 1831360, 1936903,
          2067967, 2068456]

print(''.join(decode(values)))