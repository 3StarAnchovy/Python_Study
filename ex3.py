class Calculator:
    def adder(self,a,b):
        result = a+b
        return result
    def subtracter(self,a,b):
        return a-b
    def divider(self,a,b):
        return a/b
    def multiplicater(self,a,b): #메소드의 첫번째 인자는 항상 self
        return a*b

calc = Calculator();
a = int(input());
b = int(input());

print(calc.adder(a,b))
print(calc.subtracter(a,b))
