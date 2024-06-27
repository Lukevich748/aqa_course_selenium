from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TableHandler:

    # Table
    TABLE_LOCATOR = ("xpath", "//table[@id='example']")
    ROWS_LOCATOR = ("xpath", ".//tr[not(@role='row')]")
    CELLS_LOCATOR = ("xpath", "./td")
    SEARCH_INPUT_LOCATOR = ("xpath", "//input[@type='search']")

    # Buttons
    NEW_BUTTON_LOCATOR = ("xpath", "//div[@class='dt-buttons']/button[contains(@class, 'buttons-create')]")
    EDIT_BUTTON_LOCATOR = ("xpath", "//div[@class='dt-buttons']//button[contains(@class, 'buttons-edit')]")
    NEXT_BUTTON_LOCATOR = ("xpath", "//button[@aria-label='Next']")
    CREATE_BUTTON_LOCATOR = ("xpath", "//div[@class='DTE_Footer']//button[text()='Create']")
    UPDATE_BUTTON_LOCATOR = ("xpath", "//div[@class='DTE_Footer']//button[text()='Update']")

    # Fields
    FIRST_NAME_FIELD_LOCATOR = ("xpath", "//div[@class='DTE_Field_Input']//input[@id='DTE_Field_first_name']")
    LAST_NAME_FIELD_LOCATOR = ("xpath", "//div[@class='DTE_Field_Input']//input[@id='DTE_Field_last_name']")
    POSITION_FIELD_LOCATOR = ("xpath", "//div[@class='DTE_Field_Input']//input[@id='DTE_Field_position']")
    SALARY_FIELD_LOCATOR = ("xpath", "//div[@class='DTE_Field_Input']//input[@id='DTE_Field_salary']")

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver=driver, timeout=10, poll_frequency=1)

    @property
    def _table(self) -> WebElement:
        return self.driver.find_element(*self.TABLE_LOCATOR)

    @property
    def _rows(self) -> list[WebElement]:
        table = self._table
        return table.find_elements(*self.ROWS_LOCATOR)

    @property
    def get_rows_count(self) -> int:
        return len(self._rows)

    def get_cell_content(self, row_number: int, column_number: int) -> str:
        row = self._rows[row_number - 1]
        cell = row.find_elements(*self.CELLS_LOCATOR)[column_number - 1]
        return cell.text

    def get_all_cell_content(self) -> list[str]:
        cells_content = []
        for row in self._rows:
            for cell in row.find_elements(*self.CELLS_LOCATOR):
                cells_content.append(cell.text)
        return cells_content

    def get_row_content(self, row_number: int) -> list[str]:
        row = self._rows[row_number - 1]
        cells = row.find_elements(*self.CELLS_LOCATOR)
        row_content = [cell.text for cell in cells]
        return row_content

    def get_all_rows_content(self) -> list[str]:
        row_content = []
        for row in self._rows:
            row_content.append(row.text)
        return row_content

    def get_column_content(self, column_number) -> list[str]:
        column_content = []
        for row in self._rows:
            cells = row.find_elements(*self.CELLS_LOCATOR)[column_number - 1]
            column_content.append(cells.text)
        return column_content

    def get_content_by_name(self, name: str) -> str:
        while True:
            for row in self._rows:
                if name in self.get_row_content(self._rows.index(row) + 1):
                    return row.text
            self.next_page()

    def next_page(self):
        return self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).click()

    def search_content(self, name: str) -> list[str] | str:
        self.driver.find_element(*self.SEARCH_INPUT_LOCATOR).send_keys(name)
        result = []
        while True:
            for row in self._rows:
                if row.text == "No matching records found":
                    return "No matching records found"
                else:
                    result.append(row.text)
            if self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).get_attribute("aria-disabled") is None:
                self.next_page()
            else:
                break
        return result

    def add_content(
            self,
            first_name: str,
            last_name: str,
            position: str = None,
            salary: int = None) -> list[str]:
        self.wait.until(EC.element_to_be_clickable(self.NEW_BUTTON_LOCATOR)).click()
        assert self.driver.find_element(*self.CREATE_BUTTON_LOCATOR).is_displayed(), "Create button is not displayed"

        fields = {
            self.FIRST_NAME_FIELD_LOCATOR: first_name,
            self.LAST_NAME_FIELD_LOCATOR: last_name,
            self.POSITION_FIELD_LOCATOR: position,
            self.SALARY_FIELD_LOCATOR: str(salary)
        }

        for locator, value in fields.items():
            self.driver.find_element(*locator).send_keys(value)

        self.wait.until(EC.element_to_be_clickable(self.CREATE_BUTTON_LOCATOR)).click()

        result = self.search_content(f"{first_name} {last_name}")
        assert "No matching records found" not in result, "Content was not found"
        return result

    def edit_content(
            self,
            search_name: str,
            new_first_name: str,
            new_last_name: str,
            new_position: str = None,
            new_salary: int = None):
        search_field = self.driver.find_element(*self.SEARCH_INPUT_LOCATOR)
        search_field.send_keys(search_name)

        self._rows[0].click()

        self.wait.until(EC.element_to_be_clickable(self.EDIT_BUTTON_LOCATOR)).click()
        assert self.driver.find_element(*self.UPDATE_BUTTON_LOCATOR).is_displayed(), "Update button is not displayed"

        fields = {
            self.FIRST_NAME_FIELD_LOCATOR: new_first_name,
            self.LAST_NAME_FIELD_LOCATOR: new_last_name,
            self.POSITION_FIELD_LOCATOR: new_position,
            self.SALARY_FIELD_LOCATOR: str(new_salary)
        }

        while True:
            for locator, value in fields.items():
                if value is not None:
                    self.driver.find_element(*locator).clear()
                    self.driver.find_element(*locator).send_keys(value)
                    assert value == self.driver.find_element(*locator).get_attribute("value"), \
                        "The actual value does not match the expected value"
                else:
                    continue
            self.driver.find_element(*self.UPDATE_BUTTON_LOCATOR).click()
            break

        self.wait.until(EC.invisibility_of_element(self.UPDATE_BUTTON_LOCATOR), "Update button is displayed")
        search_field.clear()

        search_result = self.search_content(f"{new_first_name} {new_last_name}")

        assert search_result != "No matching records found", "Updated content will not find"
        return search_result