try:
    print('print this line when there is no problem in try block',tty)
except Exception as e:
    print('print this line when its come on exception block else block will be ignored')
    print(e)
else:
    print('it will run when there is no exception')
finally:
    print('it will print every time')
