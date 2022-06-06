import uuid
from exceptions.product_not_found_exception import ProductNotFoundException

class Person():
    """
    사람 객체 클래스입니다.
    """
    def __init__(self,customer_name,wallet):
        self.__id=uuid.uuid1()
        self.__customer_name=customer_name
        self.__wallet=wallet
        self.__points=0

    def buy(self, store, product):
        """
        물건을 구매하는 함수입니다.
        """
        try:
            database=store.products.get_repository()
            if product.get_product_name() in database and database[product.get_product_name()][1]>0:
                database[product.get_product_name()][1]-=1
                self.set_wallet(self.get_wallet()-product.get_price())
                self.set_points(self.get_points()+int((product.get_price())*0.1))
                store.add_income(product.get_price())
                store.add_customers((self.get_id(),self.get_customer_name()))
            else:
                raise ProductNotFoundException

            print(f"{product.get_product_name()}을 구입했습니다")
        except ProductNotFoundException:
            # print(f"현재 {store.get_store_name()} 매장에 해당 제품의 재고가 없습니다.")
            raise ProductNotFoundException
            

    def work(self):
        """
        일을 하고 현금을 충전해주는 함수입니다.
        """
        self.__wallet+=10000
        # print("일당 10000원이 입급되었습니다.")

    def check_balance(self):
        """
        잔액을 확인하는 함수입니다.
        본래는 추가적으로 메시지를 반환해 주는 기능을 가지고 있으나, 개발단계에서는 테스트를 위해 주석처리하였습니다.
        """
        # print(f"현재 잔액은 {self.__wallet}원 입니다.")
        return self.__wallet

    def get_id(self):
        """
        __id의 게터 함수입나다.
        """
        return self.__id

    def get_customer_name(self):
        """
        __customer_name의 게터 함수입나다.
        """
        return self.__customer_name

    def set_customer_name(self, string):
        """
        __customer_name의 셋터 함수입나다.
        """
        self.__customer_name=string

    def get_wallet(self):
        """
        __wallet의 게터 함수입나다.
        """
        return self.__wallet

    def set_wallet(self, integer):
        """
        __wallet의 셋터 함수입나다.
        """
        self.__wallet=integer

    def get_points(self):
        """
        __points의 게터 함수입나다.
        """
        return self.__points

    def set_points(self, integer):
        """
        __points의 셋터 함수입나다.
        """
        self.__points=integer

    def __str__(self):
        """
        사람 객체의 정보를 반환하는 클래스입니다.
        """
        return f"{self.__customer_name}씨는 현금{self.__wallet}원과 {self.__points}포인트를 가지고 있습니다."