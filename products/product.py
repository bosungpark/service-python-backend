import uuid

from exceptions.product_not_on_sale_exception import ProductNotOnSaleException
from .abstract_product import AbstractProduct

class Product(AbstractProduct):
    """
    상품 객체 클래스입니다.
    """
    #현재 세일 기간인지를 체크하는 변수. 만약 아니라면, 세일을 통한 상품가격의 변동이 불가능하다.
    on_sale=False

    def __init__(self, product_name, price, discount_rate):
        self.__id=uuid.uuid1()
        self.__product_name=product_name
        self.__discount_rate=discount_rate
        if discount_rate>0 and not self.on_sale:
            self.__price=price
            self.__discount_rate=0
            raise ProductNotOnSaleException
        else:
            self.__price=int(price*(1-self.__discount_rate/100))

    def get_id(self):
        """
        __id의 게터 함수입나다.
        """
        return self.__id

    def get_product_name(self):
        """
        __product_name의 게터 함수입나다.
        """
        return self.__product_name

    def set_product_name(self, string):
        """
        __product_name의 셋터 함수입나다.
        """
        self.__product_name=string

    def get_price(self):
        """
        _price의 게터 함수입나다.
        """
        return self.__price

    def set_price(self, integer):
        """
        _price의 셋터 함수입나다.
        """
        self.__price=integer

    @property
    def discount_rate(self):
        """
        __discount_rate의 게터 함수입나다.
        """
        return self.__discount_rate

    @discount_rate.setter
    def discount_rate(self,integer):
        """
        할인율을 지정하는 함수입니다.
        입력은 정수값으로 입력합니다.
        예를들어 20%세일이라면 20을 입력합니다.
        """
        if not self.on_sale:
            raise ProductNotOnSaleException
        else:
            self.__discount_rate=integer
            self.__price= int(self.__price*(1-self.__discount_rate/100))


    @classmethod
    def switch_flag(cls):
        """
        현재 매장에 세일 여부를 조정하는 함수입니다.
        on_sale이 True라면 할인룰 적용이 가능합니다.
        하지만 False라면 할인을 통한 가격변동은 불가능합니다.
        단, 직접 가격설정을 통한 가격 변경은 가능합니다.
        """
        cls.on_sale=not cls.on_sale

    def __str__(self):
        return f"{self.__product_name}의 현재 가격은 {self.__discount_rate}% 할인된 {self.__price}원 입니다."
