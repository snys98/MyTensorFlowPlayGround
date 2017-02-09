'''
class represents vector
'''


class Vector(object):
    '''
    class represents vector
    '''

    def __init__(self, values):
        self.set_values(values)

    def get_values(self):
        '''
        get the vector values
        '''
        return self._values_

    def set_values(self, values):
        '''
        get the vector values
        '''
        self._values_ = values

    values = property(get_values, set_values)
