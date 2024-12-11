import logging


class ProjectLog:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ProjectLog, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler("my_log_file.log")
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger

    def example(self):
        # Log some messages
        self.logger.debug("This is a debug message")
        self.logger.info("This is an info message")
        self.logger.warning("This is a warning message")
        self.logger.error("This is an error message")
        self.logger.critical("This is a critical message")
