from plugins.utils.logger import setup_logger, get_logger

setup_logger()

logger = get_logger(__name__)
logger.info('test')