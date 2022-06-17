"""
# 의사코드

IMPORT unittest

FROM exceptions.index_out_of_range_exception IMPORT IndexOutOfRangeException
FROM exceptions.product_not_found_exception IMPORT ProductNotFoundException
FROM exceptions.product_not_on_sale_exception IMPORT ProductNotOnSaleException
FROM users.person IMPORT Person
FROM products.product IMPORT Product
FROM stores.store IMPORT Store
FROM navigation IMPORT navigation

CLASS Tests(unittest.TestCase){

    park 을 고객명단에 100000원과 추가
    편의점에 kfc추가
    상품에 hot_wings와 가격 3000원, 수량 0추가
    상품에 chicken_tenders와 가격 2000원, 수량 0추가

    FUNC test_generate_person_instance(self){

        park=Person("park",100000)
        받은 고객 이름과 명단에 올라간 이름이 같은지 체크
        고객 보유 자금이 예상과 같은지 체크

        park이 일을 함
        park이 일을 해서 일당이 추가됐는지 확인
        잔액을 확인했을 때 자금과 같은지 확인}

    FUNC test_generate_store_instance(self){

        kfc=Store("kfc")
        kfc라는 이름이 제대로 등록됐는지 확인}

    FUNC test_generate_store_instance(self){

        hot_wings=Product("hot_wings",3000, 0)
        상품이름이 제대로 등록됐는지 확인
        상품가격이 제대로 등록됐는지 확인
        상품할인률 확인

        WITH 예외 발생하는지 확인 (ProductNotOnSaleException){
            chicken_tenders=Product("chicken_tenders",2000, 10)}

        WITH 예외 발생하는지 확인 (ProductNotOnSaleException){
            hot_wings.discount_rate=10}

        chicken_tenders를 상품에 가격과 수량, 이름 추가
        상품명이 제대로 등록됐는지 확인
        상품 가격이 제대로 등록됐는지 확인
        할인 확인
        상품할인
        상품 50%할인
        할인한 가격이 제대로 됐는지 확인}

    FUNC test_buy_not_registered_product(self){

        WITH 예외 발생하는지 확인(ProductNotFoundException):
            고객이 상품을 구입}

    FUNC test_register_product(self){

        kfc에 핫윙등록
        kfc에 핫윙등록
        kfc에 핫윙등록
        핫윙 세 개가 제대로 추가됐는지 확인

        kfc에 치킨텐더 등록

        kfc에서 상품이 제일 적은 순부터 정렬
        WHILE TRUE{
            TRY{
                다음 상품으로 넘어감}
            EXCEPT IndexOutOfRangeException 예외 발생시 {
                BREAK}}}

    FUNC test_buy_registered_product(self){

        hot_wings 구매
        고객이 물건을 제대로 구매했는지 확인
        재고가 맞는지 확인

        출력이 제대로 되는지 확인
        매출이 맞는지 확인
        고객의 잔여금이 맞는지 확인
        고객의 포인트가 맞는지 확인}

    FUNC test_navigation(self){
        navigation()}}
"""

import unittest

from exceptions.index_out_of_range_exception import IndexOutOfRangeException
from exceptions.product_not_found_exception import ProductNotFoundException
from exceptions.product_not_on_sale_exception import ProductNotOnSaleException
from users.person import Person
from products.product import Product
from stores.store import Store
from navigation import navigation

class Tests(unittest.TestCase):
    """
    테스트 클래스입니다.
    """
    park=Person("park",100000)
    kfc=Store("kfc")
    hot_wings=Product("hot_wings",3000, 0)
    chicken_tenders=Product("chicken_tenders",2000, 0)

    def test_generate_person_instance(self):
        """
        사람 인스턴스 테스트 메서드
        """
        park=Person("park",100000)
        self.assertEqual(park.get_customer_name(), "park")
        self.assertEqual(park.get_wallet(), 100000)

        park.work()
        self.assertEqual(park.get_wallet(), 110000)
        self.assertEqual(park.get_wallet(), park.check_balance())

    def test_generate_store_instance(self):
        """
        매장 인스턴스 테스트 메서드
        """
        kfc=Store("kfc")
        self.assertEqual(kfc.get_store_name(), "kfc")

    def test_generate_product_instance(self):
        """
        상품 인스턴스 테스트 메서드
        """

        hot_wings=Product("hot_wings",3000, 0)
        self.assertEqual(hot_wings.get_product_name(), "hot_wings")
        self.assertEqual(hot_wings.get_price(), 3000)
        self.assertEqual(hot_wings.discount_rate, 0)

        with self.assertRaises(ProductNotOnSaleException):
            chicken_tenders=Product("chicken_tenders",2000, 10)

        with self.assertRaises(ProductNotOnSaleException):
            hot_wings.discount_rate=10

        chicken_tenders=Product("chicken_tenders",2000, 0)
        self.assertEqual(chicken_tenders.get_product_name(), "chicken_tenders")
        self.assertEqual(chicken_tenders.get_price(), 2000)
        self.assertEqual(chicken_tenders.discount_rate, 0)
        hot_wings.switch_flag()
        hot_wings.discount_rate=50
        self.assertEqual(hot_wings.get_price(), 1500)

    def test_buy_not_registered_product(self):
        """
        상품 구매 테스트 메서드
        """
        with self.assertRaises(ProductNotFoundException):
            self.park.buy(self.kfc, self.hot_wings)

    def test_register_product(self):
        """
        제품 등록 테스트 메서드
        """
        self.kfc.register(self.hot_wings)
        self.kfc.register(self.hot_wings)
        self.kfc.register(self.hot_wings)
        self.assertEqual(self.kfc.products.get_repository(), {'hot_wings': [3000, 3]})

        self.kfc.register(self.chicken_tenders)

        kfc_sorted_products=self.kfc.products.sorted_by_stock()
        while True:
            try:
                next(kfc_sorted_products)
            except IndexOutOfRangeException:
                break

    def test_buy_registered_product(self):
        """
        상품 구매 테스트 메서드
        """
        self.kfc.register(self.hot_wings)
        self.assertEqual(self.park.buy(self.kfc,self.hot_wings), "hot_wings을 구입했습니다")
        self.assertEqual(self.kfc.products.get_repository(), {'hot_wings': [3000, 0]})

        self.assertEqual(self.kfc.get_customers()[-8:-1], "park고객님")
        self.assertEqual(self.kfc.get_income(), 3000)
        self.assertEqual(self.park.get_wallet(), 97000)
        self.assertEqual(self.park.get_points(), 300)

    @classmethod
    def test_navigation(cls):
        """
        네비게이션 테스트 메서드
        유저와 가게 사이의 적당한 경로를 출력해줍니다.

        가능하면 예시에 있는 좌표를 입력하기를 권장드립니다.
        """
        navigation()
        