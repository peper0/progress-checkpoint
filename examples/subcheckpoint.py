from time import sleep

from progress_checkpoint import dummy_checkpoint, with_progress, with_progress_sub


def time_consuming_operation(checkpoint=dummy_checkpoint):
    for _ in with_progress(range(10), checkpoint):
        sleep(0.1)


def compound_time_consuming_operation(checkpoint=dummy_checkpoint):
    for _, subcheckpoint in with_progress_sub(range(2), checkpoint):
        time_consuming_operation(subcheckpoint)


compound_time_consuming_operation(lambda p, _: print("{:.0f}% ready".format(p * 100)))
