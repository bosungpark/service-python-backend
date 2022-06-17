"""
# 의사코드

FROM repositorys.item_repository IMPORT ItemRepository
FROM stores.abstract_store IMPORT AbstractStore

CLASS 매장(AbstractStore 상속받는 매장 객체) 클래스:
    FUNC 생성자 함수(매장 이름):
        name을 매장 이름으로 초기화
        income을 0으로 초기화
        customers을 빈 집합으로 초기화
        products를 레포지터리 클래스로 초기화

    FUNC 매장에 상품을 등록하는 함수(상품):
        상품 이름과 상품 가격 출력

        p_name과 p_price 각각을 문자열화한 상품 이름, 가격으로 설정
        레포지터리에 상품이름과 가격 추가

    FUNC 매장의 이름을 반환하는 함수
        RETURN 매장의 이름

    FUNC 매장의 이름을 세팅하는 함수(문자열로 입력된 매장명)
        문자열로 입력된 매장명을 매장 이름으로 설정

    FUNC 수입 값을 반환하는 함수
        RETURN 수입

    FUNC 수입을 더하는 함수(정수열로 입력된 수입)
        수입에 입력된 수입을 더하여 할당

    FUNC 고객 명단을 반환하는 함수:
        message를 매장에 등록한 고객 목록을 보여주는 문구로 설정

        FOR (고객 명단 순회)
            message에 고객의 아이디와 이름을 알려주는 문구 추가
        RETURN message

    FUNC 명단에 고객을 추가하는 함수(문자열로 입력된 고객명):
        고객 명단에 문자열로 입력된 고객명 추가

    FUNC 문자열로 반환시키는 함수:
        RETURN 매장명과 매장 수입을 알려주는 문구 출력
"""

from repositorys.item_repository import ItemRepository
from stores.abstract_store import AbstractStore

class Store(AbstractStore):
    """
    매장 객체 클래스입니다.
    """
    def __init__(self,store_name):
        self.__store_name=store_name
        self.__income=0
        #튜플의 형태 (uuid,name)->동명이인을 방지하기 위한 조치
        self.__customers=set()
        self.products=ItemRepository()

    def register(self,product):
        """
        매장에 상품을 등록하는 함수입니다.
        """
        # print(product.get_product_name(),product.get_price())

        p_name,p_price=str(product.get_product_name()),product.get_price()
        self.products.add_product(p_name,p_price)

    def get_store_name(self):
        """
        __store_name의 게터 함수입나다.
        """
        return self.__store_name

    def set_store_name(self,string):
        """
        __store_name의 셋터 함수입나다.
        """
        self.__store_name=string

    def get_income(self):
        """
        __income의 게터 함수입나다.
        """
        return self.__income

    def add_income(self,integer):
        """
        __income의 셋터 함수입나다.
        """
        self.__income+=integer

    def get_customers(self):
        """
        customers의 목록을 반환하는 함수입나다.
        """
        message=f'{self.get_store_name()}에 등록한 고객 목록\n'

        for customer in self.__customers:
            message+=f'id: {customer[0]}값을 가지신 {customer[1]}고객님\n'
        return message

    def add_customers(self, string):
        """
        customers의 목록을 추가하는 함수입나다.
        """
        self.__customers.add(string)

    def __str__(self):
        """
        매장객체의 정보를 담은 클래스입니다.
        """
        return f"{self.get_store_name()}의 현재 매출은 {self.get_income()}원 입니다."
    