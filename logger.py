from loguru import logger


logger.add(
    'newspublisher.log', 
    format="{time} {level} {message}", 
    level="INFO",
    rotation='500MB',
    compression='zip')