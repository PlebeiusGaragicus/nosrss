import os
import logging

# Define the color codes
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

# Function to set the color
def set_color(color):
    return f'\033[1;3{color}m'

# Custom log level colors
LOG_COLORS = {
    logging.DEBUG: set_color(BLUE),
    logging.INFO: set_color(GREEN),
    logging.WARNING: set_color(YELLOW),
    logging.ERROR: set_color(RED),
    logging.CRITICAL: set_color(MAGENTA),
}

class ColoredFormatter(logging.Formatter):
    def format(self, record):
        level_color = LOG_COLORS[record.levelno]
        record.levelname = f"{level_color}{record.levelname}\033[0m"
        return super().format(record)


def setup_logging():
    debug = os.getenv("DEBUG", False)
    if debug:
        # log_format = "%(asctime)s %(levelname)s | (%(filename)s @ %(lineno)d) >> %(message)s"
        # log_format = "%(levelname)s | %(asctime)s | (%(filename)s @ %(lineno)d) | %(message)s"
        log_format = "%(name)s %(levelname)s | (%(filename)s @ %(lineno)d) | %(message)s"
    else:
        # log_format = "%(asctime)s %(levelname)s | %(message)s"
        # log_format = "%(levelname)s | %(asctime)s | %(message)s"
        log_format = "%(levelname)s | %(message)s"

    formatter = ColoredFormatter(log_format, datefmt="%Y/%m/%d %H:%M.%S")

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logging.basicConfig(level=logging.DEBUG if debug != False else logging.INFO, handlers=[console_handler])
