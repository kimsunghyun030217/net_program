# MyComplex 클래스 정의 및 곱셈 결과 출력 프로그램

class MyComplex:
    def __init__(self, real_1, imaginary_1, real_2, imaginary_2):
        self.real_1 = real_1           # 첫 번째 복소수의 실수 부분
        self.imaginary_1 = imaginary_1 # 첫 번째 복소수의 허수 부분
        self.real_2 = real_2           # 두 번째 복소수의 실수 부분
        self.imaginary_2 = imaginary_2 # 두 번째 복소수의 허수 부분

    def multiply(self):
        # 곱셈 공식: (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        a = self.real_1
        b = self.imaginary_1
        c = self.real_2
        d = self.imaginary_2

        real_part = a * c - b * d
        imaginary_part = a * d + b * c

        print(f"{real_part}+{imaginary_part}i")

# a = 3 - 4i, b = -5 + 2i 를 클래스에 저장하여 곱셈 수행
# a = (3, -4), b = (-5, 2)

complex_calc = MyComplex(3, -4, -5, 2)
complex_calc.multiply()  # 출력 결과: -7+26i