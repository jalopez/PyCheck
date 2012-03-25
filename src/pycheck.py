def check(value, var_name = None):
    return Variable(value, var_name)

### Decorators

def only_warn(fn):
    """
        Substitute check error exceptions by warnings
    """
    def decorator(*args, **kwargs):
        try:
            fn(*args, **kwargs)
        except CheckError, e:
            print 'Warning: ' + str(e)
    return decorator


### Validation classes

class Variable(object):

    def __init__(self, value, var_name):
        self._value = value
        self._negation = False
        self._name = var_name

    def exists(self):
        error_msg = '%s should exist' % (self._name or self._value,)
        dont_error_msg = '%s should not exist' % (self._name or self._value,)
        return self._check(self._value != None, error_msg, dont_error_msg)
        
    def is_None(self):
        error_msg = '%s should not have any value' % (self._name or self._value,)
        dont_error_msg = '%s should have some value' % (self._name or self._value,)
        return self._check(self._value == None, error_msg, dont_error_msg)  


    ### Private methods

    def _dont(self):
        """ Negates the next validation """
        self._negation = True
        return self


    def _check(self, validation, error_msg, dont_error_msg = ''):
        """ Check a validation against the value """
        error = error_msg

        if self._negation:
            self._negation = False
            validation = not validation
            error = dont_error_msg
        
        if validation:
            return self     
        else:
            raise CheckError(error)

    def __getattr__(self, name):
        valid_attr_validations = (
            'dont',
        )
        if name in valid_attr_validations:
            return object.__getattribute__(self, '_%s' % (name,))()
        else:
            raise AttributeError("%r object has no attribute %r" %
                         (type(self).__name__, attr))
            

class CheckError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)