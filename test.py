"""
test log.py
"""

from log import get_logger

logger = get_logger('test')
logger.info('test something')
logger.warning('est warning')