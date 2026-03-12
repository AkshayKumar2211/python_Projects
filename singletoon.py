class Single:
	instance=None
	def __new__(cls):
		if cls.instance is None:
			cls.instance=super().__new__(cls)
		return cls.instance
	
a=Single()
b=Single()

print(a is b)

