from functional_tests.main_page_locators import MainPageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Blog Collection Page action methods are here."""

    def is_title_matches(self):
        """Verifies that the hardcoded text "React App" appears in page title"""

        expected_title = "React App"

        return expected_title == self.driver.title

    def is_url_matches(self):
        """Verifies that the URL is correct on Main Page"""

        page_url = 'http://localhost:3000/main'

        return page_url == self.driver.current_url

    def is_main_header_matches(self):
        """Triggers the navigation and checks main header text"""

        element = self.driver.find_element(*MainPageLocators.MAIN_HEADER)
        expected_header = 'Simple Django and React Blog with Testing Automation'

        return expected_header == element.text

    def click_navigation_button(self):
        """Triggers the navigation button and checks URL"""

        element = self.driver.find_element(*MainPageLocators.NAV_BUTTON_ABOUT)
        element.click()
        page_url = 'http://localhost:3000/about'

        return page_url == self.driver.current_url

    def is_sub_header_matches(self):
        """Triggers the navigation and checks sub header text"""

        element = self.driver.find_element(*MainPageLocators.SUB_HEADER)
        expected_header = 'All Blogs'

        return expected_header == element.text

    def is_no_posts_message_matches(self):
        """Triggers the header element and checks no posts message text"""

        element = self.driver.find_element(*MainPageLocators.NO_POSTS_MESSAGE)
        expected_message = 'There are no posts!'

        return expected_message == element.text

    def is_pages_counter_matches(self):
        """Triggers the span element and checks pages counter text"""

        element = self.driver.find_element(*MainPageLocators.PAGES_COUNTER)
        expected_counter = 'Page 1 of 1'

        return expected_counter == element.text
