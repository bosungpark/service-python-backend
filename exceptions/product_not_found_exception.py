class ProductNotFoundException(Exception):
    """
    재고가 없는 상품을 주문할 때 생기는 예외 클래스입니다.
    """
    def __init__(self):
        super().__init__('현재 매장에 해당 제품의 재고가 없습니다.')