# Private

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # Private

    def rest_pass(self):
        print(self.__acc_pass)


acc1 = Account(12345, "Abcde")
print(acc1.acc_no)
# print(acc1.__acc_pass)  Private h isliye Error aa rha

print(acc1.rest_pass())
