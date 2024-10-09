import logging
import re


class HideApiKeyHandler(logging.Formatter):
    def format(self, record):
        formatted = super().format(record)
        return re.sub(r"apikey=[^&]*", "apikey=******", formatted)
