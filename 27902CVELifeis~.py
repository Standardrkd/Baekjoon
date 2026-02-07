# CVE Life is ~

import sys
sys.set_int_max_str_digits(100000)

N = int(input())

if len(str(2**N)) <= 4300:
    print(2**N)
