x = input('ok')

def swap_every(val, every):
    result = ''
    for i in range(int(len(val)/every/2)):
        i *= 2
        result += val[every*(i+1):every*(i+2)]
        result += val[every*i:every*(i+1)]
        # print(i, result)
    return result

print(swap_every(x, 4))
