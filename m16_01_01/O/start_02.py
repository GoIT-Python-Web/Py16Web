class Logger:
    def log_to_console(self, message):
        print(message)

    def log_to_file(self, message, filename):
        with open(filename, 'w') as file:
            file.write(message)