def indexOfCaps(para):
    ret = []

    idx = 0
    for ch in para:
        if ord('A') <= ord(ch) <= ord('Z'):
            ret.append(idx)

        idx += 1

    return ret


print(indexOfCaps('eDaBiT'))