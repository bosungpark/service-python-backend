import sys
from os import path

import unittest

from test import Tests

# 절대경로 선언
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


# *, **
# 함수 일급 객체
# 재귀함수

if __name__ == '__main__':
    unittest.main()