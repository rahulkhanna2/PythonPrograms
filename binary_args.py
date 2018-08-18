def bin(*args):
    result = [] #empties the list before the function is carried out
    for arg in args:
        arg = str(arg)
        number = arg[::-1] #reverse the number
        power , total = 0 , 0
        for i in number:
            total += int(i) * (2**power)
            power += 1
        result.append(total)
    return sum(result)
