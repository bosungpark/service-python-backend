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
        현재 매장상품의 제고가 적은 순으로 정렬한 값을 리스트 형태로 반환해줍니다.
        """
        sorted_products=deque(sorted(self.__repository.items(), key=lambda x: x[1][1]))

        def generator(end):
            i=1
            while i<end and sorted_products:
                yield print(f"현재 매장에 재고가 {i}번째로 많이 쌓여있는 품목은 {sorted_products.popleft()[0]}입니다.")
            print("해당 상품들은 빠른 시일 내에 주문이 필요합니다.")
            raise IndexOutOfRangeException
        return generator(len(sorted_products))
        