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

    # Table Buttons
    # button_name = [create, edit, remove]
    table_button_locator = lambda self, button_name: ("xpath", f"//div[@class='dt-buttons']/button[contains(@class, 'buttons-{button_name}')]")

    # Pagination Buttons
    NEXT_BUTTON_LOCATOR = ("xpath", "//button[@aria-label='Next']")

    # Pop-Up Buttons
    # button_name = [Create, Update, Delete]
    pop_up_button_locator = lambda self, button_name: ("xpath", f"//div[@class='DTE_Footer']//button[text()='{button_name}']")
    DELETE_POPUP_INFO_LOCATOR = ("xpath", "//div[@class='DTED_Lightbox_Content']//div[@class='DTE_Form_Info']")

    # Pop-Up Fields
    # field_name = [first_name, last_name, position, office, extn, start_date, salary]
    field_locator = lambda self, field_name: ("xpath", f"//div[@class='DTE_Field_Input']//input[@id='DTE_Field_{field_name}']")

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
            if any(row.text == "No matching records found" for row in self._rows):
                return "No matching records found."

            result.extend(row.text for row in self._rows)

            next_button = self.driver.find_element(*self.NEXT_BUTTON_LOCATOR)
            if next_button.get_attribute("aria-disabled"):
                break

            next_button.click()

        return result

    def add_content(
            self,
            first_name: str,
            last_name: str,
            position: str = None,
            salary: int = None) -> str:
        self.wait.until(EC.element_to_be_clickable(self.table_button_locator("create"))).click()
        assert self.driver.find_element(*self.pop_up_button_locator("Create")).is_displayed(), "Create button is not displayed."

        fields = {
            self.field_locator("first_name"): first_name,
            self.field_locator("last_name"): last_name,
            self.field_locator("position"): position,
            self.field_locator("salary"): str(salary)
        }

        for locator, value in fields.items():
            self.driver.find_element(*locator).send_keys(value)

        self.wait.until(EC.element_to_be_clickable(self.pop_up_button_locator("Create"))).click()
        self.wait.until(EC.invisibility_of_element(self.pop_up_button_locator("Create")))

        result = self.search_content(f"{first_name} {last_name}")
        assert "No matching records found" not in result, "Content was not found."
        return f"Person '{result}' has been added."

    def edit_content(
            self,
            search_name: str,
            new_first_name: str,
            new_last_name: str,
            new_position: str = None,
            new_salary: int = None) -> str:
        search_field = self.driver.find_element(*self.SEARCH_INPUT_LOCATOR)
        search_field.send_keys(search_name)

        self._rows[0].click()

        self.wait.until(EC.element_to_be_clickable(self.table_button_locator("edit"))).click()
        assert self.driver.find_element(*self.pop_up_button_locator("Update")).is_displayed(), "Update button is not displayed."

        fields = {
            self.field_locator("first_name"): new_first_name,
            self.field_locator("last_name"): new_last_name,
            self.field_locator("position"): new_position,
            self.field_locator("salary"): str(new_salary),
        }

        for locator, value in fields.items():
            if value is not None:
                element = self.driver.find_element(*locator)
                element.clear()
                element.send_keys(value)
                assert value == element.get_attribute("value"), "The actual value does not match the expected value."

        self.wait.until(EC.element_to_be_clickable(self.pop_up_button_locator("Update"))).click()
        self.wait.until(EC.invisibility_of_element(self.pop_up_button_locator("Update")), "Update button is displayed.")

        search_field.clear()

        result = self.search_content(f"{new_first_name} {new_last_name}")
        assert result != "No matching records found", "Updated content will not find."

        return f"Person '{result}' has been updated."

    def delete_content(self, search_name: str) -> str:
        search_field = self.driver.find_element(*self.SEARCH_INPUT_LOCATOR)
        search_field.send_keys(search_name)

        self._rows[0].click()

        self.wait.until(EC.element_to_be_clickable(self.table_button_locator("remove"))).click()
        assert self.driver.find_element(*self.DELETE_POPUP_INFO_LOCATOR).text == "Are you sure you wish to delete 1 row?"

        self.wait.until(EC.element_to_be_clickable(self.pop_up_button_locator("Delete"))).click()
        self.wait.until(EC.invisibility_of_element(self.DELETE_POPUP_INFO_LOCATOR))

        for row in self._rows:
            assert row.text == "No matching records found"

        return f"Person '{search_name}' has been deleted."
