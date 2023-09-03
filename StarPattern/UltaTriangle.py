#  range(1,5)h to jo last hota h jaise  5 vo excluded h
for i in range (1,5):
    for j in range (1,5):
        if j<=5-i:
            # we use end kuki vrna vo ek str print krkr agli line m chla jega isliye end se vo usi line m rhega
            print("*" , end ='')
        else:
            print(" " , end='')
    print()