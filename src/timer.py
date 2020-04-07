## @file timer.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief Helper class for timing methods
#  @date Apr 6, 2020

from timeit import default_timer as timer

## @brief Timer class
class Timer():
    def __init(self):
        self.time = 0;

    def start(self):
        self.time = timer()

    def end(self):
        return (timer() - self.time)