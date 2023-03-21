class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a_real, a_imag = map(int, a[:-1].split('+'))
        b_real, b_imag = map(int, b[:-1].split('+'))
        real = a_real * b_real - a_imag * b_imag
        imag = a_real * b_imag + a_imag * b_real
        return f'{real}+{imag}i'