# Mock client module for win32com

def Dispatch(com_object_name):
    """Mock for COM object Dispatch"""
    print(f"Mock Dispatch of COM object: {com_object_name}")
    return MockCOMObject(com_object_name)

class MockCOMObject:
    """A mock COM object that can be used for testing"""
    
    def __init__(self, name):
        self.name = name
        print(f"Created mock COM object: {name}")
    
    # Add methods as needed based on what the real COM objects implement
    def __getattr__(self, name):
        # This will handle any method or property access
        def method(*args, **kwargs):
            arg_str = ', '.join([str(a) for a in args] + [f"{k}={v}" for k, v in kwargs.items()])
            print(f"Called {self.name}.{name}({arg_str})")
            # Return a reasonable default value
            return 0
        return method 