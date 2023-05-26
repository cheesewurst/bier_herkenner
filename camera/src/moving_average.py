from typing import List

moving_averages = []
window_size = 20

def moving_average(new_value: float) -> float:
    global moving_averages
    moving_averages.append(new_value)
    if len(moving_averages) > window_size:
        moving_averages.pop(0)

    return sum(moving_averages) / len(moving_averages) if moving_averages else 0