# Currying practice based on: https://www.clear.rice.edu/comp130/12spring/curry/

def curry(x):
    def a_func(y):
        return x*y # a_func's closure includes curry()'s input param.
    return a_func

f1 = curry(42)
f2 = curry(-10)

print(f1(2))
print(f2(2))
print(f1(-1))
print(f2(-1))

print('-' * 30)

# Looking at curry() func and its returned function together.
# The curring process reduces a func to a func of less params.
print(curry(3)(2))
print(curry(-4)(2))
print(curry(3)(-5))