class VariableValidator(object):

    def __init__(self, value, var_name, print_validations):
        self._value = value
        self._negation = False
        self._name = var_name
        self._print_validations = print_validations

        if self._print_validations:
            print "Validations for %s" % (self._name or self._value)

    def exists(self):
        error_msg = '%s should exist' % (self._name or self._value)
        dont_error_msg = '%s should not exist' % (self._name or self._value)
        return self._check(self._value != None, error_msg, dont_error_msg)
        
    def is_None(self):
        error_msg = '%s should not have any value' % (self._name or self._value)
        dont_error_msg = '%s should have some value' % (self._name or self._value)
        return self._check(self._value == None, error_msg, dont_error_msg)  

    def is_number(self):
        error_msg = '%s is not a number' % (self._name or self._value)
        return self._fail(error_msg)


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

class NumericValue(VariableValidator):

    def is_number(self):
        error_msg = '%s is a number' % (self._name or self._value)
        return self._success(error_msg)


class CheckError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
