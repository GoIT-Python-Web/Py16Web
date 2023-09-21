class LegacySystem:
    def execute(self, value1, value2, operation):
        if operation == "add":
            return value1 + value2
        elif operation == "sub":
            return value1 - value2
        else:
            raise ValueError("Unknown operation")


if __name__ == '__main__':
    legacy = LegacySystem()
    result = legacy.execute(5, 5, "add")
    print(result)
    result = legacy.execute(5, 5, "sub")
    print(result)
    