class MyClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def print_info(self):
        print(f"Name: {self.name}, Value: {self.value}")


if __name__ == "__main__":
    obj = MyClass("Test", 42)
    obj.print_info()
