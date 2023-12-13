# %% Function and Variable
msg = "hello world"
print(msg)

# %%
2**2
2**3
3**2
# %%
2 >> 2
2 << 1
# %%
a = -1
a if a > 0 else 0
if a > 0:
    a = a
else:
    a = 0
print(a)

# %%


def apply_mul(a):
    print("apply_mul", a)
    return mul(*a)


def mul(a, b):
    # print("mul",)
    return a * b
    # return a


print(mul(2, 2))

# %%

a = [
    (1, 2),
    (3, 4),
    (4, 6),
]
len(a)
a[0]

# %%
list(map(apply_mul, a))

# %%
list(map(lambda x: mul(*x), a))

# %%
b = []
for aa in a:
    print(aa)
    r = mul(*aa)
    b.append(r)
print(b)


# %%
def n2(a):
    return a * 2


b = [1, 3, 4]
list(map(n2, b))

# %%
a = 32
# a = a a > 0 && a < 100
# other, a = 0
b = {}
b[True] = {
    True: a,
    False: 0,
}
b[False] = {
    True: 0,
    False: 0,
}
print(b[a > 0][a < 100])

# %%
