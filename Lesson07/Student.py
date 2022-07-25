class Student:
    def __init__(self, student_name="JohnDoe",
                 conf={
                     'exam_max': 0,
                     'lab_max': 0,
                     'lab_num': 0,
                     'k': 0
                 }
                 ):
        self.conf = conf
        self.name = student_name
        self.labs = []
        self.exam = 0.0
        self.balls = 0.0
        self.max_balls = self.conf['lab_num'] * self.conf['lab_max'] + self.conf['exam_max']
        self.result = (0.0, False)
        if self.conf['lab_num']:
            for i in range(0, self.conf['lab_num']):
                self.labs.append(0)

    def make_lab(self, m=0.0, n=None):
        m = m * 1.0
        if m > self.conf['lab_max']:
            m = self.conf['lab_max']

        if n is not None:
            if n < len(self.labs):
                self.labs[n] = m
        else:
            for lab in range(0, len(self.labs) - 1):
                if self.labs[lab] == 0:
                    self.labs[lab] = m
                    break

        return self

    def make_exam(self, m=0.0):
        m = m * 1.0
        if m > self.conf['exam_max']:
            m = self.conf['exam_max']
        self.exam = m

        return self

    def is_certified(self):
        self.balls = 0.0
        for i in self.labs:
            self.balls += i
        # print ("max balls:" + str(self.max_balls) + "\nballs:" + str(self.balls + self.exam) + "\nneeded balls:" + str(self.max_balls * self.conf['k']))
        self.result = (self.balls + self.exam, self.balls + self.exam >= self.max_balls * self.conf['k'])

        return self.result
