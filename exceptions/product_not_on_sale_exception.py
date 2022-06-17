"""
# 의사코드

CLASS 세일 기간이 아닌 상품에 대해 세일 기능을 조작할 때 생기는 예외 클래스
    FUNC 생성자 함수:
        예외 메시지 설정
"""

class ProductNotOnSaleException(Exception):
    """
    세일기간이 아닌 상품에 대해 세일관련한 기능을 조작할 때 생기는 예외 클래스입니다.
    """
    def __init__(self):
        super().__init__("세일 기간이 아닙니다.\n따라서 할인률은 적용되지 않을 것입니다.")
        