from playwright.sync_api import Page

class LoginPage:
  def __init__(self, page: Page):
    self.page = page
    self.user_name_field = page.get_by_test_id("username")
    self.password_field = page.get_by_test_id("password")
    self.login_button = page.get_by_test_id("login-button")
    self.error_message = page.get_by_test_id("error")
  
  def goto(self, page: Page):
      page.goto()
      
  def login(self, username: str, password: str):
    self.user_name_field.fill(username)
    self.password_field.fill(password)
    self.login_button.click()