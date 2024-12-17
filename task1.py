try :
    a=int(input()) # 1
    b=int(input()) # 0
    c=a/b
except (ZeroDivisionError) as e:
    print(a/5)
except (ValueError) as e :
    print("Invalid input",e)
finally :
    print('finally block')
# finally will run compulsary 
# u can use more than 1 excepts and 1 is compalsary
# ur not compalsary to use finally
# indentetion and syntex error will not be handle by error exception and its call compile time error
# all other error will be handle by error exception
# there are two type of errors 1.comiletime error 2.RUN time error

# try:
# except :
# else :
# finally:
    # u have to follow upper sequance order
    # else will run only when there is no error
    # else ke except mathi koi ek ma j jay