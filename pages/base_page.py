from time import sleep
from configs import config
from logs.logger import logger

class BasePage:

    TIMEOUT = config.TIMEOUT

    def __init__(self, driver) -> None:
        self.driver = driver
    

    def text_exists(self, text):
        wait = 0
        while wait < self.TIMEOUT:
            if text.lower() not in self.driver.page_source.lower():
                sleep(1)
                wait += 1
                logger.info(f'Waited for {wait} seconds for [{text}] ...')
            else:
                logger.info(f'Found [{text}] waited {wait} seconds ...')
                return True
        logger.info(f'Text [{text}] was NOT found, waited {wait} seconds ...')
        return False
