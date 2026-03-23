import logging
import os

class LogGen:
    @staticmethod
    def loggen():

        # Project root directory
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        log_dir = os.path.join(base_dir, "logs")

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_file = os.path.join(log_dir, "automation.log")

        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        # Remove old handlers (important for pytest)
        if logger.hasHandlers():
            logger.handlers.clear()

        file_handler = logging.FileHandler(log_file)

        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger

# import logging
# import os
#
# class LogGen():
#     @staticmethod
#     def loggen():
#         path = os.path.abspath(os.curdir) + '\\logs\\automation.log'
#         logging.basicConfig(filename=path,
#                             format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#         logger = logging.getLogger()
#         logger.setLevel(logging.DEBUG)
#         return logger