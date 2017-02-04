
# Think Python: Chapters 11, 13, 14

# Chapter 11: Dictionaries


def histogram(s):
    """Return histogram from string."""
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

h = histogram('brontosaurus')
print(h)


def print_hist(h):
    """Print histogram."""
    for c in h:
        print(c, h[c])

print('\n')
print_hist(h)
print('\n')
for key in sorted(h):
    print(key, h[key])


def reverse_lookup(d, v):
    """Perform a reverse lookup."""
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('value does not appear in the dictionarys')

h = histogram('parrot')
key = reverse_lookup(h, 2)
print('\n')
print(key)

#key = reverse_lookup(h, 3) # uncussessful reverse lookup


def invert_dict(d):
    """Invert a dictionary."""
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

hist = histogram('parrot')
print('\n')
print(hist)
inverse = invert_dict(hist)
print('\n')
print(inverse)

t = [1, 2, 3]
d = dict()
# d[t] = 'ooops' # causes error
# print(d[t]) # causes error

known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

print('\n')
print(fibonacci(10))

