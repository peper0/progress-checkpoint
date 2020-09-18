from time import sleep

from progress_checkpoint import dummy_checkpoint, with_progress, with_progress_sub


def time_consuming_operation(num, checkpoint=dummy_checkpoint):
    for _ in with_progress(range(num), checkpoint):
        sleep(0.1)


def compound_time_consuming_operation(checkpoint=dummy_checkpoint):
    counts = [1, 3, 7]
    for cnt, subcheckpoint in with_progress_sub(counts, checkpoint, weights=counts):
        time_consuming_operation(cnt, subcheckpoint)


compound_time_consuming_operation(lambda p, _: print("{:.0f}% ready".format(p * 100)))
