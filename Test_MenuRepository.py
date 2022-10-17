from unittest import mock
from Menu import Menu
from MenuRepository import MenuRepository
from Order import Order
from UserInterface import UserInterface
import unittest


class TestMenuRepository(unittest.TestCase):

    def test_set_menu_item(self):
        # Arrange
        menu_repository = MenuRepository()
        menu_repository.menu_itens = []
        menu1 = Menu(1, "Test 1", 10)
        menu2 = Menu(2, "Test 2", 5)
        menu3 = Menu(3, "Test 3", 2)
        # Act

        menu_repository.set_menu_item(menu1)
        menu_repository.set_menu_item(menu2)

        # Assert
        self.assertEquals(len(menu_repository.menu_itens),2)
        self.assertFalse(menu3 in menu_repository.menu_itens)
        self.assertEquals(type(menu_repository.menu_itens),list)

    def test_check_if_itens_exists(self):
        # Arrange
        menu_repository = MenuRepository()
        menu_repository.menu_itens = []
        menu1 = Menu(1, "Test 1", 10)
        # Act

        menu_repository.set_menu_item(menu1)
        resultOK = menu_repository.check_if_itens_exists(Order(1,1))
        resultNOK = menu_repository.check_if_itens_exists(Order(0,0))

        # Assert
        self.assertEquals(len(menu_repository.menu_itens),1)
        self.assertTrue(resultOK)
        self.assertFalse(resultNOK)

    def test_check_if_total_price_is_right(self):
        menu_repository = MenuRepository()
        menu_repository.menu_itens = []
        menu1 = Menu(1, "Test 1", 10)

        menu_repository.set_menu_item(menu1)

        lanche1 = Order(1,5)

        result = menu_repository.get_total_price(lanche1)
        self.assertEquals(result,50)

    def test_check_if_user_info_is_right(self):
        with mock.patch('builtins.input', return_value="2 4"):
            user = UserInterface(MenuRepository())
            user_input = user.get_user_input()

            ord = Order(2,4)

            self.assertEquals(ord,user_input)
