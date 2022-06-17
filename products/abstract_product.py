"""
# 의사코드

FROM abc IMPORT ABCMeta

CLASS AbstractProduct(추상클래스, 상품):
    id=None
    name=None
    price=None
    discount_rate=None

    @클래스매소드
    FUNC switch_flag(cls,**kargs):

    FUNC 상품객체의 정보를 담은 함수:
"""

from abc import ABCMeta

class AbstractProduct(metaclass=ABCMeta):
    """
    상품 객체의 추상클래스입니다.
    """
    id=None
    name=None
    price=None
    discount_rate=None

    @classmethod
    def switch_flag(cls,**kargs):
        """
        switch_flag의 추상메서드입니다.
        """

    def __str__(self):
        """
        상품객체의 정보를 담은 클래스입니다.
        """
