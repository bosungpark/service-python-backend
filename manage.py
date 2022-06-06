import sys
from os import path

import unittest

from test import Tests

# 절대경로 선언
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

if __name__ == '__main__':
    unittest.main()