# prompt: inheritance with py

class MyChildClass(MyClass):
    def __init__(self, public_attr, protected_attr, private_attr, child_attr):
        super().__init__(public_attr, protected_attr, private_attr)
        self.child_attr = child_attr
    
    def get_attributes(self):
      print(f"Public: {self.public_attr}")
      print(f"Protected: {self._protected_attr}")
      print(f"Private: {self.get_private_attr()}")
      print(f"Child: {self.child_attr}")

# Example usage
child_obj = MyChildClass("ChildPublic", "ChildProtected", "ChildPrivate", "ChildSpecific")

child_obj.get_attributes()
print(child_obj.public_attr)
print(child_obj._protected_attr)
child_obj._MyClass__private_attr