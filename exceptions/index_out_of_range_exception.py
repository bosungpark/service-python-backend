class IndexOutOfRangeException(Exception):
    """
    인덱스가 순회할 시퀀스 객체의 범위를 넘어갈 시 호출됩니다. 
    """
    def __init__(self):
        super().__init__('이미 모든 상품의 재고를 확인하였습니다.')