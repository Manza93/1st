def donuts(count):
        comment = 'Number of donuts: '
        if count >= 10:
                i = "many"
        else:
                i = str(count)
        result = "Number of donuts: " + i
        return result
def both_ends(s):
    if len(s) <= 2:
        x = ''
    else:
        i = s[0:2]
        f = s[-2:]
        x = i + f
    return x
def fix_start(s):
    if len(s) > 0:
        firts_car = s[0]
        x = s [1:]
        final = s[0] + x.replace(firts_car,'*')
    return final
def mix_up(a, b):
    f = b[0:2] + a[2:] + ' ' + a[0:2] + b[2:]
    return f
def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)
def main():
    print 'donuts'
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print
    print 'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

  
    print
    print 'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')
    
main()

def verbing(s):
    if len(s) >= 3:
        if s[-3:] == "ing":
            s = s + "ly"
        else:
            s = s + "ing"
    return s
def not_bad(s):
    import re
    if re.search('not (.)*bad', s):
        s = re.sub("not (.)*bad", "good", s)
    return s
def front_back(a, b):
        a_len=len(a)
        b_len=len(b)
        if a_len%2 == 0:
                a_front = a[0:(a_len/2)]
                a_back = a[-(a_len/2):]
        else:
                a_front = a[0:(a_len/2+1)]
                a_back = a[-(a_len/2):]
        if b_len%2 == 0:
                b_front = b[0:(b_len/2)]
                b_back = b[-(b_len/2):]
        else:
                b_front = b[0:(b_len/2+1)]
                b_back = b[-(b_len/2):]
        return a_front + b_front + a_back + b_back
def main():
    print 'verbing'
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')
    
    print
    print 'not_bad'
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print
    print 'front_back'
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')
main()