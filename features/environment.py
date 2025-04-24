from utility.web_driver import WebDriverFactory

def before_scenario(context, scenario):
    context.driver = WebDriverFactory.get_driver()

def after_scenario(context, scenario):
    context.driver.quit()
