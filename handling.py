try :
    a=int(input()) # 1
    b=int(input()) # 0
    c=a/b
except (ZeroDivisionError,ValueError) as e:
    print('error',e) #error division by zero
finally :
    print('finally block')
# finally will run compulsary 