# prompt: coding python encapsulasi private dan protect

class MyClass:
    def __init__(self, public_attr, protected_attr, private_attr):
        self.public_attr = public_attr
        self._protected_attr = protected_attr  # Protected attribute (convention)
        self.__private_attr = private_attr  # Private attribute (name mangling)

    def get_private_attr(self):
        return self.__private_attr

    def set_private_attr(self, new_value):
        self.__private_attr = new_value

# Example usage
obj = MyClass("Public", "Protected", "Private")

# Accessing attributes
print(obj.public_attr)       # Accessing public attribute directly
print(obj._protected_attr)   # Accessing protected attribute (convention, still accessible)
# print(obj.__private_attr) # Direct access will cause an AttributeError

# Accessing private attribute using methods
print(obj.get_private_attr())
obj.set_private_attr("New Private Value")
print(obj.get_private_attr())

# Name mangling demonstration (accessing the private attribute directly, but with modified name)
obj._MyClass__private_attr