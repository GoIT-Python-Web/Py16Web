class Report:
    def __init__(self, content):
        self.content = content

    def generate_report(self):
        pass  # logic to generate a report

    def save_to_file(self, file_path):
        with open(file_path, 'w') as file:
            file.write(self.content)

            