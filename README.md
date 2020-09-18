# Progress-checkpoint

Helpers for reporting a progress from functions by the means of callbacks.
## Examples

### Trivial

```python
def time_consuming_operation(checkpoint=dummy_checkpoint):
    for i in with_progress(range(10), checkpoint):
        time.sleep(0.2)

time_consuming_operation(lambda p, _: print("{:.0f}% ready".format(p*100)))
```

### Subcheckpoints

```python
def time_consuming_operation(checkpoint=dummy_checkpoint):
    for _ in with_progress(range(10), checkpoint):
        sleep(0.1)


def compound_time_consuming_operation(checkpoint=dummy_checkpoint):
    for _, subcheckpoint in with_progress_sub(range(2), checkpoint):
        time_consuming_operation(subcheckpoint)


compound_time_consuming_operation(lambda p, _: print("{:.0f}% ready".format(p * 100)))
```

### Subcheckpoints with different weights

```python
def time_consuming_operation(num, checkpoint=dummy_checkpoint):
    for _ in with_progress(range(num), checkpoint):
        sleep(0.1)


def compound_time_consuming_operation(checkpoint=dummy_checkpoint):
    counts = [1, 3, 7]
    for cnt, subcheckpoint in with_progress_sub(counts, checkpoint, weights=counts):
        time_consuming_operation(cnt, subcheckpoint)


compound_time_consuming_operation(lambda p, _: print("{:.0f}% ready".format(p * 100)))

```