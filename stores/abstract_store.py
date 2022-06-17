"""
# 의사코드

FROM abc IMPORT ABCMeta, abstractmethod

from abc import ABCMeta, abstractmethod

CLASS AbstractStore(추상클래스) 클래스:
    income=None
    customers=None
    products=None

    @추상매소드
    FUNC 등록하기 함수:
        pass

    FUNC 상품정보 기입하기 합수:
"""

from abc import ABCMeta, abstractmethod

class AbstractStore(metaclass=ABCMeta):
    """
    매장 객체 추상클래스입니다.
    """
    income=None
    customers=None
    products=None

    @abstractmethod
    def register(self,**kargs):
        """
        상품 등록 추상 메서드입니다.
        """
        return

    def __str__(self):
        """
        상품정보를 기입할 추상메서드입니다.
        """
        