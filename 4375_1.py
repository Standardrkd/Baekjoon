import sys
sys.set_int_max_str_digits(9999)
while True:
    try:
        n = int(input())
        i = 10
        one = 1
        while True:
            if one % n == 0:
                print(len(str(one)))
                break
            one += i
            i *= 10
    except:
        exit(0)