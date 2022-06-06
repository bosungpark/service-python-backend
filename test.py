import unittest

from exceptions.index_out_of_range_exception import IndexOutOfRangeException
from exceptions.product_not_found_exception import ProductNotFoundException
from exceptions.product_not_on_sale_exception import ProductNotOnSaleException
from users.person import Person
from products.product import Product
from stores.store import Store

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

    def test_generate_store_instance(self):
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
            except(IndexOutOfRangeException):
                break

    def test_buy_registered_product(self):
        """
        상품 구매 테스트 메서드

        이 메서드의 경우, id 값 등이 랜덤하게 변하므로 라이브러리를 통한 테스트에 한계가 있습니다.
        더욱 섬세하게 테스트 케이스를 작성할 수도 있겠지만, 편의를 위해 print()를 통한 디버깅을 사용하였습니다.
        """
        self.kfc.register(self.hot_wings)
        self.park.buy(self.kfc,self.hot_wings)
        print(self.kfc.products.get_repository())
        print(self.kfc.get_customers())
        print(self.kfc)
        print(self.park)

if __name__ == '__main__':
    unittest.main()