class VariableValidator(object):

    def __init__(self, value, var_name, print_validations):
        self._value = value
        self._print_name = var_name or value
        self._negation = False

        self._print_validations = print_validations

        if self._print_validations:
            print "Validations for %s" % (self._print_name)


    def exists(self):
        error_msg = '%s should exist' % (self._print_name)
        dont_error_msg = '%s should not exist' % (self._print_name)
        return self._check(self._value != None, error_msg, dont_error_msg)


    def is_None(self):
        error_msg = '%s should not have any value' % (self._print_name)
        dont_error_msg = '%s should have some value' % (self._print_name)
        return self._check(self._value == None, error_msg, dont_error_msg)  


    def equals(self, other):
        error_msg = '%s should be equal to %s' % (self._print_name, other)
        dont_error_msg = '%s should be distinct to %s' % (self._print_name, other)
        # To be overriden in complex classes
        return self._check(self._value == other, error_msg, dont_error_msg)


    def distinct(self, other):
        error_msg = '%s should be distinct to %s' % (self._print_name, other)
        dont_error_msg = '%s should be equal to %s' % (self._print_name, other)
        # To be overriden in complex classes
        return self._check(self._value != other, error_msg, dont_error_msg)


    def gt(self, other):
        error_msg = '%s should be greater than %s' % (self._print_name, other)
        dont_error_msg = '%s should not be greater than %s' % (self._print_name, other)
        return self._check(self._value > other, error_msg, dont_error_msg)

    ## TODO: Think a better way of handling these kind of methods
    def is_number(self):
        error_msg = '%s should be a number' % (self._print_name)
        dont_error_msg = '%s should not be a number' % (self._print_name)
        return self._check(isinstance(self._value, (int, long, float, complex)), 
                        error_msg, dont_error_msg)


    def is_int(self):
        error_msg = '%s should be an integer' % (self._print_name)
        dont_error_msg = '%s should not be an integer' % (self._print_name)
        return self._check(isinstance(self._value, (int)), error_msg, dont_error_msg)


    ### Private methods

    def _dont(self):
        """ Negates the next validation """
        self._negation = True
        return self


    def _check(self, validation, error_msg, dont_error_msg = None):
        """ Check a validation against the value """
        error = error_msg

        if self._negation:
            self._negation = False
            validation = not validation
            error = dont_error_msg or 'Dont: ' + error_msg

        if self._print_validations:
            print ' - ' + error
                
        if validation:
            return self     
        else:
            raise CheckError(error)


    def _fail(self, error_msg):
        """ Fail unless dont is modifying the validation """
        if self._negation:
            self._negation = False
            return self
        else:
            raise CheckError(error_msg)

    
    def _success(self, error_msg):
        """ Success unless dont is modifying the validation """
        if self._negation:
            raise CheckError(error_msg)
        else:
            return self


    def __getattr__(self, name):
        valid_attr_validations = (
            'dont',
        )

        if name in valid_attr_validations:
            return object.__getattribute__(self, '_%s' % (name,))()
        else:
            raise AttributeError("%r object has no attribute %r" %
                         (type(self).__name__, name))



class CheckError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
