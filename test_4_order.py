import pytest
from locators import *
from data import *


@pytest.mark.positive
# case 4.1
def test_positive_order(browser, standard_auth):
    # pick item and add it to cart:
    browser.find_element('xpath', '(//button[@class="btn_primary btn_inventory"])[1]').click()

    # go to cart:
    browser.find_element(*CartPage.cart_btn).click()

    # go to checkout:
    browser.find_element(*CheckoutPage.checkout_btn).click()

    # fill a form:
    browser.find_element(*CheckoutPage.input_fname).send_keys(PostAuth.fake_user_fname)
    browser.find_element(*CheckoutPage.input_lname).send_keys(PostAuth.fake_user_lname)
    browser.find_element(*CheckoutPage.input_zipcode).send_keys(PostAuth.fake_zip)

    # click 'continue' button:
    browser.find_element(*CheckoutPage.continue_btn).click()

    # click 'finish' button:
    browser.find_element(*CheckoutPage.finish_btn).click()

    # check url and success message:
    curr_url = browser.current_url
    assert curr_url == URLs.checkout_url and CheckoutPage.complete_msg, 'Wrong url'

    # check if cart is empty:
    cart_quantity_tag = '//a[@class="shopping_cart_link fa-layers fa-fw"]/span'
    assert cart_quantity_tag not in browser.page_source, 'Shopping cart is not empty'


@pytest.mark.xfail
@pytest.mark.negative
# case 4.2
def test_negative_empty_order(browser, standard_auth):
    # go to cart:
    browser.find_element(*CartPage.cart_btn).click()

    # go to checkout:
    browser.find_element(*CheckoutPage.checkout_btn).click()

    # fill a form:
    browser.find_element(*CheckoutPage.input_fname).send_keys(PostAuth.fake_user_fname)
    browser.find_element(*CheckoutPage.input_lname).send_keys(PostAuth.fake_user_lname)
    browser.find_element(*CheckoutPage.input_zipcode).send_keys(PostAuth.fake_zip)

    # click 'continue' button:
    browser.find_element(*CheckoutPage.continue_btn).click()

    # click 'finish' button:
    browser.find_element(*CheckoutPage.finish_btn).click()

    # check url and success message:
    curr_url = browser.current_url
    assert not curr_url == URLs.checkout_url and not CheckoutPage.complete_msg, 'Shopping cart is empty, wrong checkout'
