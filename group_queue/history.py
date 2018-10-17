

class History:

    def __init__(self, filename: str="history"):

        self.filename = filename
        self.history_file = open(filename, "w", encoding="UTF-8")

    def _re_open_file(self):
        self.history_file = open(self.filename, "a", encoding="UTF-8")

    def write(self, history: any):
        self.history_file.write(str(history))
        self.history_file.write("\n")
        self.history_file.close()

        self._re_open_file()

    def clean(self):
        self.history_file = open(self.filename, "w", encoding="UTF-8")

    def change_file(self, new_filename: str):
        self.filename = new_filename
        self.history_file = open(new_filename, "w")

    def get_history(self) -> list:
        self.history_file.close()
        history = open(self.filename, "r", encoding="UTF-8")
        history = history.read().split("\n")
        self._re_open_file()
        return history
