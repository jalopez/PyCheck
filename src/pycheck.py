def check(value):
	return Variable(value)


class Variable(object):

	def __init__(self, value):
		self._value = value
		self._negation = False

	def exists(self):
		error_msg = '%s does not exist' % (self._value,)
		return self._check(self._value != None, error_msg)
		
	def is_None(self):
		error_msg = '%s has value' % (self._value,)
		return self._check(self._value == None, error_msg)	


	### Private methods

	def _dont(self):
		""" Negates the next validation """
		self._negation = True
		return self


	def _check(self, validation, error_msg):
		""" Check a validation against the value """
		if self._negation:
			self._negation = False
			validation = not validation
			error_msg = 'Dont: ' + error_msg
		if validation:
			return self		
		else:
			raise CheckError(error_msg)

	def __getattribute__(self, name):
		valid_attr_validations = (
			'dont',
		)
		if name in valid_attr_validations:
			object.__getattribute__(self, '_%s' % (name,))()
			return self
		else:
			return object.__getattribute__(self, name)
			

class CheckError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)