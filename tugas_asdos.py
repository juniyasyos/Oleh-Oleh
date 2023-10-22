# |>>>>>>>>>>>>>>>>>>>> INI SOAL YA MASSS <<<<<<<<<<<<<<<<<<<<<<<|
from icecream import ic

# Kode 1
def sequenceGenerator(start,stop):
    x = []
    for i in range(start,stop):
        x.append(i)
    return x
# print(sequenceGenerator(1,10))

# Kode 2
def fizzBuzz(a,b):
    x = []
    for num in range(a,b):
        if num % 3 == 0 and num % 5 == 0:
            x.append("FizzBuzz")
        elif num % 3 == 0:
            x.append("Fizz")
        elif num % 5 == 0:
            x.append("Buzz")
        else:
            x.append(num)
    return x

# Kode 3
def twoNumbers(l):
    res = []
    for i in l:
        if l.index(i) == len(l) - 2:
            break
        z = i + l[i+1]
        res.append(z)
    return res


# |>>>>>>>>>>>>>>>>>>>> INI JAWABANNYA YA MASSS <<<<<<<<<<<<<<<<<<<<<<<|
# Kode 1
sequenceGenerator_FP = lambda start, stop: list(map(int, range(start, stop)))
ic(sequenceGenerator_FP(1, 10))

#Kode 2
from functools import reduce
fizzBuzz_FP = lambda a, b: \
    reduce(
        lambda x,y : x+y, 
        map(
            lambda num: \
                ["FizzBuzz" if num % 3 == 0 and num % 5 == 0 else "Fizz" if num % 3 == 0 else "Buzz" if num % 5 == 0 else num], 
                range(a, b)
            )
        )
ic(fizzBuzz_FP(1, 30))

# Kode 3
twoNumbers_FP = lambda l: [] if len(l) < 2 else [l[0] + l[1]] + twoNumbers_FP(l[1:])
ic(twoNumbers_FP([1, 2]))

