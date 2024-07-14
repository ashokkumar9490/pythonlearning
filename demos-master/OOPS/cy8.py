class Height:
    def __init__(self, inches):
        self.feet = 0
        self.inches = 0
        self.cal_height_parts(inches)

    def __str__(self):
        return f"{self.feet}'{self.inches}\""  # \" to escape "

    def cal_height_parts(self, inches):
        self.feet = inches // 12        # floor or int division
        self.inches = inches % 12       # mod to get remainder


h1 = Height(50)
print(f"Height1 = {h1}")
h2 = Height(70)
print(f"Height2 = {h2}")
