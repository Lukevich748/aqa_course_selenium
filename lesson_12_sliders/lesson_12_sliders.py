from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

driver.get("https://seiyria.com/bootstrap-slider/")

EXAMPLE_6_LOCATOR = ("xpath", "//a[text()='Example 6']")
SLIDER_LOCATOR = ("xpath", "(//div[@id='example-6']//div[@role='slider'])[1]")
CURRENT_SLIDER_VALUE_LOCATOR = ("xpath", "//div[@id='example-6']//span[@id='ex6SliderVal']")

driver.find_element(*EXAMPLE_6_LOCATOR).click()


def move_slider(slider_locator: tuple, current_point: int, target_point: int):
    slider = driver.find_element(*slider_locator)

    if target_point < current_point:
        offset = current_point - target_point
        slider.send_keys(Keys.ARROW_LEFT * offset)
    else:
        offset = target_point - current_point
        slider.send_keys(Keys.ARROW_RIGHT * offset)


def set_slider_example_6(slider_locator: tuple, current_point_attr_name: str, target_point: int):
    min_value = -5
    max_value = 20

    slider = driver.find_element(*slider_locator)

    current_point = int(slider.get_attribute(current_point_attr_name))

    move_slider(slider_locator, current_point, target_point)

    if target_point < min_value or target_point > max_value:
        raise ValueError(
            f"Target point '{target_point}' is out of range. Must be between '{min_value}' and '{max_value}'.")

    current_slider_value = int(driver.find_element(*CURRENT_SLIDER_VALUE_LOCATOR).text)
    assert target_point == current_slider_value, "Target point is not correct"


set_slider_example_6(slider_locator=SLIDER_LOCATOR,
                     current_point_attr_name="aria-valuenow",
                     target_point=20)

driver.quit()