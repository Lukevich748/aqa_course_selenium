from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class TableHandler:
    TABLE_LOCATOR = ("xpath", "//table[@id='example']")
    ROWS_LOCATOR = ("xpath", ".//tr[not(@role='row')]")
    CELLS_LOCATOR = ("xpath", "./td")
    SEARCH_INPUT_LOCATOR = ("xpath", "//input[@type='search']")
    NEXT_BUTTON_LOCATOR = ("xpath", "//button[@aria-label='Next']")

    def __init__(self, driver):
        self.driver: WebDriver = driver

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

    def get_cell_content(self, row_number: int, column_number: int):
        row = self._rows[row_number - 1]
        cell = row.find_elements(*self.CELLS_LOCATOR)[column_number - 1]
        return cell.text

    def get_all_cell_content(self):
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

    def get_all_rows_content(self):
        row_content = []
        for row in self._rows:
            row_content.append(row.text)
        return row_content

    def get_column_content(self, column_number):
        column_content = []
        for row in self._rows:
            cells = row.find_elements(*self.CELLS_LOCATOR)[column_number - 1]
            column_content.append(cells.text)
        return column_content

    def get_content_by_name(self, name: str):
        while name not in self.get_all_rows_content():
            self.next_page()
            for row in self._rows:
                if name in self.get_row_content(self._rows.index(row) + 1):
                    return row.text

    def next_page(self):
        return self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).click()

    def search_content(self, name: str):
        self.driver.find_element(*self.SEARCH_INPUT_LOCATOR).send_keys(name)
        result = []
        for row in self._rows:
            for cell in row.find_elements(*self.CELLS_LOCATOR):
                if name in cell.text:
                    result.append([row.text])
                    break

        if not result:
            return "No matching records found"

        return result
