from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')
FILE_PATH = "record.txt"


class Scorerecord(Turtle):
    def __init__(self):
        super().__init__()
        self.record = 0
        self.ht()
        self.goto(100, 270)
        self.color("Yellow")
        self.read_record()
        self.write(arg=f"Record: {self.record}", align=ALIGNMENT, font=FONT)

    def read_record(self):
        record_file = open(FILE_PATH, "r")
        try:
            saved_record = record_file.read()
            if saved_record:
                self.record = saved_record
        finally:
            record_file.close()


    def write_record(self, score, record):
        record_file = open(FILE_PATH, "w")
        try:
            if score > int(record):
                record_file.write(str(score))
            else:
                record_file.write(record)
        finally:
            record_file.close()