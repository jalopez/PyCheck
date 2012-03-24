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
		try: 
			self.exists()
		except CheckError:
			return self
		else:
			raise CheckError('%s has value' % (self.value))


class CheckError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)