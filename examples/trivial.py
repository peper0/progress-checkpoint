from time import sleep

from progress_checkpoint import dummy_checkpoint, with_progress


def time_consuming_operation(checkpoint=dummy_checkpoint):
    for _ in with_progress(range(10), checkpoint):
        sleep(0.1)


time_consuming_operation(lambda p, _: print("{:.0f}% ready".format(p * 100)))
