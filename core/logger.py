import logging
import os

from datetime import datetime

from settings import BASE_SETTINGS
from root import ROOT_DIR


class Logger:
    def __init__(self):
        level = BASE_SETTINGS['log_level']
        file_path = os.path.join(ROOT_DIR, 'logs', f'{datetime.now().date()}.log')
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        log_level = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'ERROR': logging.ERROR,
            'WARNING': logging.WARNING,
        }
        # Настройка логирования
        logging.basicConfig(
            filename=file_path,
            level=log_level[level],
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger()

    def log_info(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_debug(self, message):
        self.logger.debug(message)


base_logger = Logger()
