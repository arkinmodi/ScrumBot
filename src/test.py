## @file test.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief Testing for ScrumBot
#  @date Mar 29, 2020

import pytest
import task

## @brief Testing of Task Module
class Test_Task:
    ## @brief Testing init and respective getters
    def test_create_task_and_getters(self):
        test_task = task.Task("Name", "2020/01/01 00:00", "Details")
        assert(
            test_task.get_name() == "Name" and
            test_task.get_deadline() == "Jan 01, 2020 at 12:00 AM" and
            test_task.get_details() == "Details"
        )
    
    ## @brief Testing init and respective getters with no details
    def test_create_task_with_no_details(self):
        test_task = task.Task("Name", "2020/01/01 00:00")
        assert(
            test_task.get_name() == "Name" and
            test_task.get_deadline() == "Jan 01, 2020 at 12:00 AM" and
            test_task.get_details() == "No details"
        )

    ## @brief Testing adding and getting feedback
    def test_add_and_get_feedback(self):
        test_task = task.Task("Name", "2020/01/01 00:00", "Details")
        test_task.add_feedback("Feedback")
        assert(test_task.get_feedback() == ["Feedback"])

    ## @brief Testing getting feedback with no feedback
    def test_get_feedback_with_no_feedback(self):
        test_task = task.Task("Name", "2020/01/01 00:00", "Details")
        assert(test_task.get_feedback() == [])

    ## @brief Testing removing feedback
    def test_rm_feedback(self):
        test_task = task.Task("Name", "2020/01/01 00:00", "Details")
        test_task.add_feedback("Feedback")
        assert(test_task.get_feedback() == ["Feedback"])
        test_task.rm_feedback(0)
        assert(test_task.get_feedback() == [])

    ## @brief Testing removing feedback with no feedback
    def test_rm_feedback_with_no_feedback(self):
        with pytest.raises(IndexError):
            test_task = task.Task("Name", "2020/01/01 00:00", "Details")
            test_task.rm_feedback(0)

    ## @brief Testing getting feedback with no feedback
    def test_set_details(self):
        test_task = task.Task("Name", "2020/01/01 00:00", "Details")
        test_task.set_details("New Details")
        assert(test_task.get_details() == "New Details")