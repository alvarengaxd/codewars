def is_triangle(a, b, c):
    if abs(b - c) < a < b + c or abs(a - c) < b < a + c or abs(a - b) < c < a + b: #absolute valor
        return True
    else:
        return False


'''
most voted solution

def is_triangle(a, b, c):
    return (a + b) > c and (a + c) > b and (b + c) > a

'''