class InputManager:
    def __init__(self):
        self._default_method = "default_method"
        self._methods_dict = {}
        self._next_method = self._default_method

    def set_default_method(self, method):
        self.set_methods(method)
        self._default_method = method.__name__

    def set_methods(self, *args):
        """Set a new methods to dictionary of methods"""
        for func in args:
            self._methods_dict[func.__name__] = func

    def get_methods_keys(self):
        """Returns a methods name"""
        return self._methods_dict.keys()

    def get_method(self, method_name):
        """Returns a method or None. Have a KeyError exception"""
        try:
            return self._methods_dict[method_name]
        except KeyError:
            print("(KeyError): InputManager->get_method(self,method_name)"
                  " --Method with this name not found. Method name: "+method_name)
            return self.default_method

    def call_method(self, method_name):
        """Calls a method or None. Have a KeyError exception"""
        try:
            return self._methods_dict[method_name]()
        except KeyError:
            print("(KeyError): InputManager->call_method(self,method_name"
                  " --Method with this name not found. Method name: "+method_name)
            return self.default_method()

    def set_class(self, *args):
        pass

    def set_next_method(self, next_method):
        """It is needed to determine the method that will be called by the following"""
        if next_method in self.get_methods_keys():
            self._next_method = next_method
        else:
            print("InputManager->set_next_method(self,method_name)"
                  " --Not found next_method in methods dictionary keys")
            self._next_method = "default_method"

    def update(self, user_input):
        """Main call method, implementing the management methods."""
        for method in self.get_methods_keys():
            if method == self._next_method:
                return self.get_method(method)(user_input)

    @staticmethod
    def default_method():
        print("Called default method")
        return None
