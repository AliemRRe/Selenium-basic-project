import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
# Bu proje'de Locator tercihlerine dikkat edilmemiştir :))
class LcWaikikiTest(unittest.TestCase):
    # Tarayıcı Açma 
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.lcwaikiki.com/tr-TR/TR")
        time.sleep(5)

    def tearDown(self):
        # Tarayıcı Kapatma
        self.driver.quit()

    def test_add_to_cart(self):
        # Erkek Kategori Sayfasına gidiyorum
        category = self.driver.find_element(By.CSS_SELECTOR, "[href='https://www.lcwaikiki.com/tr-TR/TR/lp/32-33-erkek']")
        category.click()
        time.sleep(5)

        # Erkek kategori sayfasında ki ilk ürüne gidiyorum
        category_product = self.driver.find_element(By.XPATH, "(//div[@class='sc5l-content']/a/img)[1]")
        category_product.click()
        time.sleep(5)

        #  ürün sayfasına gidince ürün alt tarafta kaldığı için  Scroll yapıyorum
        self.driver.execute_script("window.scrollBy(0, 200);")

        # Ürüne tıklıyorum
        product = self.driver.find_element(By.XPATH, "//a[@href='/tr-TR/TR/urun/LC-WAIKIKI/erkek/Tisort/6779826/3366924']/div[@class='product-card__product-info']")
        product.click()
        time.sleep(5)

        # Beden seçim kısmında S bedenini seçiyorum kafama göre seçim yaptım
        size = self.driver.find_element(By.CSS_SELECTOR, ".size-pop-up [key='4']")
        size.click()
        time.sleep(5)

        # Sepete ekleme butonuna tıklatıyorum
        add_to_cart = self.driver.find_element(By.CSS_SELECTOR, "#pd_add_to_cart")
        add_to_cart.click()
        time.sleep(5)

        # Sepet sayfasına gidiyorum
        cart_page = self.driver.find_element(By.CSS_SELECTOR, ".header-dropdown-toggle[href='https://www.lcwaikiki.com/tr-TR/TR/sepetim']")
        cart_page.click()
        time.sleep(5)
        
        #Anasayfa ya gidiş
        main_page = self.driver.find_element(By.CSS_SELECTOR, ".header__middle__left")
        main_page.click()

        # Assertion Testleri bu kısmında Chat Gptden birazcık yardım aldım nasıl bir planda ilerliyecepimi bilemediğim için
        # 1. Sepette ürünün olduğunu doğrulama
        self.assertTrue(self.driver.find_element(By.XPATH, "//div[@class='cart-product']/a[@href='/tr-TR/TR/urun/LC-WAIKIKI/erkek/Tisort/6779826/3366924']"))

        # 2. Sepetteki ürünün boyutunu doğrulama
        cart_product_size = self.driver.find_element(By.XPATH, "//div[@class='cart-product-size']")
        self.assertEqual(cart_product_size.text, "Beden: 2XL")

        # 3. Sepetteki toplam ürün sayısını kontrol etme
        total_items = self.driver.find_element(By.CSS_SELECTOR, ".basket-total-info span")
        self.assertIn("1", total_items.text)


if __name__ == "__main__":
    unittest.main()
