#!/usr/bin/env python3
import unittest
from factorial import fact

class TestFactorial(unittest.TestCase):
    """
    基本测试类
    """

    def test_fact(self):
        """
        实际测试
        任何以‘test_’开头的方法都被视作测试用例
        """
        res = fact(5)
        self.assertEqual(res,121)


if __name__ == '__main__':
    unittest.main()

