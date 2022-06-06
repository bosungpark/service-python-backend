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
        print(product.get_product_name(),product.get_price())

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