# When to use class method and when to use static method?

class Item:
    @staticmethod
    def is_integer(num):
        '''
        This should do with something that a relationship with the class,
        but not something  that must be unique per instance!
        '''
    @classmethod
    def instantiate_from_something(cls):
        '''
        This should also do with something that has relationship with the class,
        but usually, those are used to manipulate different structures of data to
        instantiate objects, like we have done with CSV.
        '''

# However, those could also be called from instances
item1= Item()
item1.is_integer(5)
item1.instantiate_from_something()