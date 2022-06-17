"""
# 의사코드

FROM collections IMPORT deque
FROM exceptions.index_out_of_range_exception IMORT IndexOutOfRangeException

CLASS 매장에 등록된 상품을 저장하는 레포지토리:
    FUNC 생성자 함수:
        repository를 상품 이름을 key로 [가격정보, 수량]을 value로 받는 딕셔너리로 초기화

    FUNC 레포지토리에 상품을 등록하는 함수 (상품이름, 가격):
        datebase = 레포지토리에서 꺼내옴

        IF 레포지토리에 상품 존재 THEN
            수량+=1

            IF 할인에 따른 가격 변동으로 상품 가격과 판매 가격이 다르면 THEN
                상품의 가격 = 판매가격
        ELSE:
            레포지토리에 상품의 가격과 수량을 1로 등록

    FUNC 레포지터리를 반환하는 함수(self):
        RETURN 레포지터리

    FUNC 현재 매장 상품의 재고가 적은 순으로 정렬한 값을 제너레이터 형태로 반환하는 함수(self):

        sorted_products = 레포지토리에 있는 상품들을 수량이 적은 순으로 정렬하여 리스트 형태로 반환)

        FUNC 제너레이터 함수(end)
            i = 0
            WHILE (i가 end 값과 sorted_products보다 작을 동안){
                i+=1
                YIELD 품목과 남은 재고의 순위를 안내하는 메시지
            }
            상품 주문이 필요하다는 문구 출력
            RAISE IndexOutOfRangeException
        RETURN generator(sorted_products에 있는 상품 종류 수)
"""

from collections import deque
from exceptions.index_out_of_range_exception import IndexOutOfRangeException

class ItemRepository():
    """
    매장에 등록된 상품을 저장하는 레포지토리입니다.
    """
    def __init__(self):
        #key:상품이름 value:[가격정보, 수량]
        self.__repository={}

    def add_product(self, product_name, price):
        """
        레포지토리에 상품을 등록하는 함수입니다.
        """
        datebase= self.get_repository()

        if product_name in datebase:
            #만약 레포지토리에 이미 상품이 등록되어 있다면 수량+=1
            datebase[product_name][1]+=1
            #만약 할인에 따른 가격변동이 있다면, 가격정보 최신화
            if datebase[product_name][0]!=price:
                datebase[product_name][0]=price
        else:
            datebase[product_name]=[price,1]

    def get_repository(self):
        """
        __repository의 게터 함수입나다.
        """
        return self.__repository


    def sorted_by_stock(self):
        """
        현재 매장상품의 제고가 적은 순으로 정렬한 값을 제너레이터 형태로 반환해줍니다.
        """
        sorted_products=deque(sorted(self.__repository.items(), key=lambda x: x[1][1]))

        def generator(end):
            i=0
            while i<end and sorted_products:
                i+=1
                yield print(f"현재 매장에 재고가 {i}번째로 많이 쌓여있는 품목은 {sorted_products.popleft()[0]}입니다.")
            print("해당 상품들은 빠른 시일 내에 주문이 필요합니다.")
            raise IndexOutOfRangeException
        return generator(len(sorted_products))
        