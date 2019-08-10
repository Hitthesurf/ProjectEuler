class MathFunction:
    def factorial(self, num):
        if num == 1 or num == 0:
            return 1
        else:
            return num * self.factorial(num - 1)

    def add_each_digit(self, num):
        string_num = str(num)
        total = 0
        for i in range(0, len(string_num)):
            total += int(string_num[i])
        return total
