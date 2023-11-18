def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(3, 4, 5))
print(max_num(50, 5, 7))

def mult_list(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print (mult_list([1, 2, 3]))
print (mult_list([50, 4, 6]))

def rev_string(my_str):
    return my_str[::-1]
print(rev_string("hello"))
print(rev_string("world"))

def num_within(num1, num2, num3):
    if num3 >= num1 and num3 <= num2:
        return True
    else:
        return False
print(num_within(3, 2, 4))
print(num_within(3, 1, 3))

def pascal(rows):
    triangle = []
    for row_num in range(rows):
        row = []
        for i in range(row_num + 1):
            if i == 0 or i == row_num:
                row.append(1)
            else:
                row.append(triangle[row_num - 1][i] + triangle[row_num - 1][i - 1])
        triangle.append(row)
    return triangle
print(pascal(2))
print(pascal(5))
