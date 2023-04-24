# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# Используйте декораторы свойств.

a = float(input('Введите длину прямоугольника '))
b = float(input('Введите ширину прямоугольника '))

if a < 0 or b < 0:
    print("Введите положительные значения для стороны прямоугольника")
    a = abs(a)
    b = abs(b)
    print(a, b)




class Rectangle:


    def __init__(self, side_a: float, side_b=None):
        self.side_a = side_a

        if side_b is None:
            self.side_b = side_a
        else:
            self.side_b = side_b

    def chek(self, a, b):
                if a < 0 or b < 0:
                    print("Введите положительные значения для стороны прямоугольника")
    def square_rectangle(self):
        return self.side_a * self.side_b
    def len_rectangle(self):
        return (self.side_a + self.side_b) * 2


rect = Rectangle(a, b)
print(rect.len_rectangle(), rect.square_rectangle())