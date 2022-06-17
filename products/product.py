"""
# 의사코드

IMPORT uuid

FROM exceptions.product_not_on_sale_exception IMPORT ProductNotOnSaleException
FROM .abstract_product IMPORT AbstractProduct

CLASS Product(AbstractProduct 를 상속받는 상품 객체 클래스):
     on_sale= FALSE (세일기간인지 체크하는 변수)

    FUNC 생성자 함수(상품이름, 상품가격, 할인율):
        id를 uuid.uuid1()로 초기화
        name을 상품이름으로 초기화
        discount_rate를 할인율로 초기화
        IF 할인율 > 0 이고 세일 기간이 아니라면 THEN
            "세일 기간이 아닙니다. 세일 기간에 다시 입력해주세요" 출력
            판매가격 그대로
            할인률 = 0
        ELSE:
            가격 = 정수처리( 가격 * (1-할인율 / 100))

    FUNC 고객의 id 반환해주는 함수
        RETURN 고객 id

    FUNC 이름 반환해주는 함수
        RETURN 상품 이름

    FUNC 상품명을 세팅하는 함수(문자열로 입력된 상품명):
        문자열로 입력된 상품명을 상품 이름으로 설정

    FUNC 가격 반환해주는 함수
        RETURN 상품 가격

    FUNC 상품 가격을 세팅하는 함수(정수열로 입력된 상품가격):
        정수열로 입력된 상품가격을 상품 가격으로 설정

    @property
    FUNC 할인율을 반환하는 함수
        RETURN 할인율 반환

    @discount_rate.setter
    FUNC 할인율을 지정하는 함수(정수의 할인율):
        IF 할인율 > 0 이고 세일 기간이 아니라면 then:
            할인율 = 0
            "세일 기간이 아닙니다. 세일 기간에 다시 입력해주세요" 출력
        ELSE:
            할인율 = 정수
            가격 = 정수( 가격 * ( 1 - 할인율 / 100))


    @classmethod
    FUNC 매장에 세일 여부를 조정하는 함수:
        self.on_sale=not self.on_sale

    FUNC 문자열로 반환시키는 함수:
        RETURN 상품의 가격이 얼마나 할인되었고 얼마인지 알려주는 문구 출력
"""

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
