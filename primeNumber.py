def prime_num():
    min_num = int(raw_input("enter your number"))
    max_num = int(raw_input("enter your number"))
    while min_num<=max_num:
        j = 2
        while j<min_num:
            if min_num%j==0:
                print "not prime",min_num
                break
            j  = j+1
        else:
             print "prime",min_num
        min_num = min_num+1
print prime_num()