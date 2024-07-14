class TheoryMarks:
    def __init__(self, marks):
        self.theory_marks = marks


class PracticalMarks:
    def __init__(self, marks):
        self.practical_marks = marks


class Result(TheoryMarks, PracticalMarks):

    marks = 0

    def __init__(self, tm, pm):
        TheoryMarks.__init__(self, tm)
        PracticalMarks.__init__(self, pm)
        Result.marks = self.theory_marks + self.practical_marks

    def DisplayResult(self):
        total = self.theory_marks + self.practical_marks
        print(f"Theory Marks = {self.theory_marks} Practical Marks = {
              self.practical_marks} Result = {total}")


stud = Result(67, 19)
stud.DisplayResult()
