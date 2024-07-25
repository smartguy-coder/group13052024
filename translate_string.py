text1 = 'jkhshgfjdskjvdskgjdshklvdfkjs78789'
# j -> h
# h -> 0
# s -> M

# incorrect
res = text1.replace('j', 'h').replace('h', '0').replace('s', 'M')
print(res)

# not efficient
res2 = ''
for char in text1:
    if char == 'j':
        res2 += 'h'
    elif char == 'h':
        res2 += '0'
    elif char == 's':
        res2 += 'M'
    else:
        res2 += char

print(res2)

# cool approach
translate_map = str.maketrans('jhs', 'h0M')
res3 = text1.translate(translate_map)
print(res3)
