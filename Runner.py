from WebUI_task import Scenario


login = 'Sergey'
password = '12345678'
name = 'Serg'
country = 'Ukraine'
city = 'Kyiv'
card = '1234 5678 9012 3456'
month = 'May'
year = '2024'


if __name__ == "__main__":
    s = Scenario()
    s.log_in(login, password)
    s.laptops_click()
    s.dell_click()
    s.add_to_cart_click()
    s.go_to_cart_click()
    s.place_order_click()
    s.filling_in_the_card_data(name, country, city, card, month, year)
    s.purchase_click()
    s.check_for_pop_up_window()
