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
    def switch_flag(cls):
        """
        switch_flag의 추상메서드입니다.
        """

    def __str__(self):
        """
        상품객체의 정보를 담은 클래스입니다.
        """
