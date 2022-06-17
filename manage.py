"""
IMPORT sys
FROM os IMPORT path

IMPORT unittest

FROM test IMPORT Tests

(((절대경로구하기)파일이 위치한 경로)파일이 위치한 경로)디렉터리 설치

IF __name__ 이 '__main__'과 같다면{
    테스트 실행}
"""

import sys
from os import path

import unittest

from test import Tests

# 절대경로 선언
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

if __name__ == '__main__':
    unittest.main()
    