from time import sleep

from progress_checkpoint import dummy_checkpoint, with_progress
from progress_checkpoint.console import ProgressbarCheckpoint


def time_consuming_operation(checkpoint=dummy_checkpoint):
    for _ in with_progress(range(10), checkpoint):
        sleep(0.1)


time_consuming_operation(ProgressbarCheckpoint())
