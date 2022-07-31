n = int(input())
a = int(input())
b = int(input())
c = int(input())
c1 = c * 3
b1 = b * 2
cont = 0
if (a + b1 + c1) <= n:
    if c1 <= (b + a):
        if c1 > b:
            if c1//b >= a:
                if b1 > a:
                    cont = c1//b*b1 + a
                else:
                    cont = a + b1
            else:
                if b1 > a:
                    cont = b1 + (c1 - b)
                else:
                    cont = a + b1
        else:
            cont = b1
    else:
        if a < c1 and b1 < c1:
            cont = c1 + b
else:
    cont = n
print(cont)
#else:
#if c1 // b == c1 // a:
    #cont = c1 // b * b1 + c1 // a
#else:
    #if c1 // b >= a:
        #if b1 > a:
            #cont = c1 // b * b1
        #else:
            #if c1 // b == c1 // a:
                #cont = c1 // b * b1 + c1 // a
    #else:
    #if c1 > b:
        #if c1 // b >= a:
            #if b1 > a:
                #cont = c1 // b * b1 + a + 1

#if c1 // b == c1 // a:
    #cont = c1 // b * b1 + c1 // a
