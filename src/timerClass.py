## @file timer.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief Helper class for timing methods
#  @date Apr 6, 2020

from timeit import default_timer as timer

## @brief Timer class
class timerClass():
    start_time = 0

    @staticmethod
    def start():
        timerClass.start_time = timer()

    @staticmethod
    def end():
        return (timer() - timerClass.start_time)