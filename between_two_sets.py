def get_factor(number, a_arr, b_arr):
    for element in a_arr:
        if (number % element != 0):
            return False
    for element in b_arr:
        if (element % number != 0):
            return False
    return True

if __name__ == "__main__":

    m, n = input().split(" ")
    a_arr = list(map(int, input().split(' ')))
    b_arr = list(map(int, input().split(' ')))
    b_min = min(b_arr)
    # b_min_factors = [b_min]
    counter = 0
    for i in range(1, (b_min // 2) + 1):
        if b_min % i == 0:
            # b_min_factors.append(i)
            if (get_factor(i, a_arr, b_arr)):
                counter += 1
    if (get_factor(b_min, a_arr, b_arr)):
        counter += 1

    print(counter)
