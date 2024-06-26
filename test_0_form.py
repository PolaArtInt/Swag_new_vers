import time
import pytest
from data import fake_it
from locators import FormData


# case 0.1
@pytest.mark.positive
def test_register_btn_unblocked(browser, imp_wait, form_conditions):
    browser.find_element(*FormData.form_name).send_keys(fake_it().name())
    browser.find_element(*FormData.form_pass).send_keys(fake_it().password())

    checkbox = browser.find_element(*FormData.form_check)
    checkbox.click()
    assert checkbox.is_selected(), 'Checkbox is not checked'

    register_btn = browser.find_element(*FormData.form_reg_btn)
    assert register_btn.is_enabled(), 'Register button is blocked'


@pytest.mark.positive
# case 0.2
def test_positive_fill_form_fields(browser, imp_wait, form_conditions):
    browser.find_element(*FormData.form_name).send_keys(fake_it().name())
    browser.find_element(*FormData.form_pass).send_keys(fake_it().password())

    browser.find_element(*FormData.form_check).click()
    browser.find_element(*FormData.form_reg_btn).click()

    assert browser.current_url != FormData.form_url, 'Url is not changed'


@pytest.mark.defect
@pytest.mark.xfail
@pytest.mark.negative
# case 0.3
def test_negative_fill_name_with_spaces(browser, imp_wait, form_conditions):
    browser.find_element(*FormData.form_name).send_keys('  ')
    browser.find_element(*FormData.form_pass).send_keys(fake_it().password())
    time.sleep(3)
    browser.find_element(*FormData.form_check).click()

    register_btn = browser.find_element(*FormData.form_reg_btn)
    assert not register_btn.is_enabled(), 'Register button is unblocked'
    assert 'Name is incorrect', 'Login is allowed'


@pytest.mark.negative
# case 0.4
def test_btn_blocked_with_empty_fields(browser, imp_wait, form_conditions):
    browser.find_element(*FormData.form_check).click()

    register_btn = browser.find_element(*FormData.form_reg_btn)
    assert not register_btn.is_enabled(), 'Register button is unblocked'
