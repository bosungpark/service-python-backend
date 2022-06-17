"""
# 의사코드

IMPORT uuid
FROM exceptions.product_not_found_exception IMPORT ProductNotFoundException

CLASS Person():
    FUNC 생성자 함수(고객이름, 고객이 보유한 금액)
        id를 uuid.uuid1()로 초기화
        name을 고객 이름으로 초기화
        wallet을 고객이 보유한 금액으로 초기화
        point를 0으로 초기화

    FUNC 물건을 구매하는 함수(상품을 구매한 매장, 상품):
        TRY
            물건 = 상점의 레포지토리에서 꺼내온 물건
            IF 상품의 이름이 상점의 레포지토리에 있고 상품의 수량이 0보다 크다면 THEN
                상품의 개수가 하나 줄어듬
                고객이 보유한 금액에서 상품의 가격만큼 돈을 뺌
                고객이 보유한 포인트에 (구매한 상품의 가격 * 0.1)의 값을 더함
                상점의 수입에 고객이 구매한 물건의 가격이 더해짐
                상점의 고객 명단에 고객의 아이디와 이름 추가
            ELSE:
                RAISE ProductNotFoundException
            RETURN 구매한 상품명과 함께 구매 문구 출력
        TRY블록에서 오류가 발생한다면 THEN
            RAISE ProductNotFoundException

    FUNC 고객이 일을 하고 고객이 보유한 금액을 충전해주는 함수:
        고객보유 금액에 10000원을 추가
        일당이 입금되었음을 알리는 문구 출력

    FUNC 고객이 보유한 잔액을 확인해주는 함수:
        고객이 보유한 잔액을 알려주는 문구 출력

    FUNC 고객의 아이디를 반환하는 함수:
        RETURN 고객의 아이디

    FUNC 고객의 이름을 반환하는 함수:
        RETURN 고객의 이름

    FUNC 고객의 이름을 세팅하는 함수(문자열로 입력된 고객명)
        문자열로 입력된 고객명을 고객 이름으로 설정

    FUNC 고객이 보유한 금액을 반환하는 함수
        RETURN 고객이 보유한 금액

    FUNC 고객이 보유한 금액을 세팅하는 함수(정수열로 입력된 금액)
        정수열로 입력된 보유액을 고객이 보유한 금액으로 설정

    FUNC 고객이 보유한 포인트를 반환하는 함수
        RETURN 포인트

    FUNC 고객이 보유한 포인트를 세팅하는 함수(정수열로 입력된 포인트)
        정수열로 입력된 포인트를 고객이 보유한 포인트로 설정

    FUNC 문자열로 반환시키는 함수:
        RETURN 고객명과 보유액, 보유 포인트를 알려주는 문구 출력
"""

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

            return f"{product.get_product_name()}을 구입했습니다"
        except ProductNotFoundException as not_found_exception:
            # print(f"현재 {store.get_store_name()} 매장에 해당 제품의 재고가 없습니다.")
            raise ProductNotFoundException from not_found_exception


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
    