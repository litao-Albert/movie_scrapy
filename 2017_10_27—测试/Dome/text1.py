import random
# h=range(5)
# y=random.choice(h)
# print(y)

# seq=list(range(10))
# l=random.shuffle(seq)
# seq.sort()
# print(l)
# s='email=test1%40qq.com&password=123456&repassword=123456&verifyCode=aaaa&tiny_token_reg=l7prz3i38dklm4xdoc7hqq2zm1lnpk9j'
# l=s.split('&')
# print(l)
import unittest
from nose_parameterized import parameterized


class TestAdd(unittest.TestCase):
    @parameterized.expand([
        ("01",1, 1, 2),
        ("02",2, 2, 5),
        ("03",3, 3, 6),
    ])
    def test_add(self, name, a, b, c):
        self.assertEqual(a + b, c)
if __name__ == '__main__':
    unittest.main(verbosity=2)
