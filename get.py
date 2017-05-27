def get_something(something,something_else,gap=' '):
	if type(something)==str and type(something_else)==str:
		return something.upper()+gap+something_else.upper()
	elif type(something)==str or type(something_else)==str:
		return str(something)+str(something_else)
	elif type(something)==int and type(something_else)==int:
		return int(something)+int(something_else)
print(get_something('Hello','world'))
print(get_something(2,3))
print(get_something('Hi',3))