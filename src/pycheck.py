def check(value):
	return Variable(value)


class Variable:
	def __init__(self, value):
		self.value = value

	def exists(self):
		if self.value is None:
			raise CheckError('%s does not exist' % (self.value))
		else:
			return self

	def is_None(self):
		self.__opposite(self.exists, '%s has value')


	def __opposite(self, method, error_msg, *args):
		"""
			Executes the opposite method validation of the one passed 
			as parameter.
			The method can have a variable number of arguments
		"""
		try: 
			method(*args)
		except CheckError:
			return self
		else:
			raise CheckError(error_msg % (self.value))


class CheckError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)