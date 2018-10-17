import random
import os

class GetQuestion:

    answers_file = None
    questions_file = None

    # Проблемы с кодировками на разных системах
    if os.name == "nt":
        files_path = "questions/java/QaA_javaWindows"
    else:
        files_path = "questions/java/QaA_java"
    wasted_questions = []
    last_question = None

    def __init__(self):
        self.q_a_a = self.get_questions_from_file()

    def update_file_open(self):
        self.answers_file = open(self.files_path + "/java_oop_answers", "r")
        self.questions_file = open(self.files_path + "/java_oop_questions", "r")

        self.answers_file = self.answers_file.read().split("$$")
        self.questions_file = self.questions_file.read().split("\n")

    def get_questions_from_file(self) -> list:

        self.update_file_open()
        i = 0
        q_a_a = []

        for que in self.questions_file:
            q_a_a.append([que, self.answers_file[i]])
            i += 1
        return q_a_a

    def get_question(self, quest_id: int = -1) -> list:
        if quest_id == -1:
            quest_id = random.randint(0, 61)
        else:
            quest_id += 1

        if quest_id not in self.wasted_questions:
            self.wasted_questions.append(quest_id)

        self.last_question = quest_id - 1

        return [quest_id,                   # question id
                self.q_a_a[quest_id][0],    # question
                self.q_a_a[quest_id][1]]    # answer

    def get_wasted_questions(self): return self.wasted_questions

    def get_last_question(self): return self.last_question

    def reset_wasted_questions(self): self.wasted_questions = []

