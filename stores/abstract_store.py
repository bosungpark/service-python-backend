from abc import ABCMeta, abstractmethod

class AbstractStore(metaclass=ABCMeta):
    """
    매장 객체 추상클래스입니다.
    """
    income=None
    customers=None
    products=None

    @abstractmethod
    def register(self, product):
        """
        상품 등록 추상 메서드입니다.
        """
        return

    def __str__(self):
        """
        상품정보를 기입할 추상메서드입니다.
        """