def calculator(txt):
    s=0

    a =0
    for i in txt:
        txt = txt.replace(' ', '')
    x = len(txt)
    for i in txt:
        while i=='.':
            a=a+1
    print(a)
   

print(calculator("..... + ..............."))