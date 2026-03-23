import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import Optional
import logging

logger = logging.getLogger(__name__)

# Single ThreadPoolExecutor for CPU-bound ML inference (Avoid GIM issues)
# Default max_workers: Num CPUs + 4
ml_executor = ThreadPoolExecutor(thread_name_prefix="inference_worker")

def get_ml_executor():
    """ Returns the global thread pool for CPU-heavy inference. """
    return ml_executor
