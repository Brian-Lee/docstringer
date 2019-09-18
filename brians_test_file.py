def test_func1():
    test_var = "this isn't really much of a variable"

def test_func2():

    a = 1
    b = a + 10

    return b

def test_func3():
    ''' this function was already documented'''
    this_function_doesnt_really_do_much = True

def test_func4(input):
	#this is test_func4
	print(input)
	return True
	
print(test_func1.__doc__)
print(test_func2.__doc__)
print(test_func3.__doc__)
print(test_func4.__doc__)