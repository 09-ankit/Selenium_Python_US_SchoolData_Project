from Pages.SearchPage import SearchPage
from Utilities.BasePage import BasePage

class Test:

    def __init__(self):
        self.base = BasePage()  # Initialize the base page (WebDriver instance)
        self.Search = SearchPage(self.base.driver)
        self.Search.enter_School("A")
        self.Search.click_Search_button()
        self.Search.get_Result_Count()
        self.Search.Store_Schools_Data()


test = Test()
