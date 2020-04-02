## @file test.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief Testing for ScrumBot
#  @date Mar 29, 2020

import pytest
import task

## @brief Testing of Task Module
class Test_Task:
    def test_create_task_and_getters(self):
        test_task = task.Task("Name", "2020/01/01 00:00", "Details")
        assert(
            test_task.get_name() == "Name" and
            test_task.get_deadline() == "Jan 01, 2020 at 12:00 AM" and
            test_task.get_details() == "Details"
        )

    def test_create_task_with_no_details(self):
        test_task = task.Task("Name", "2020/01/01 00:00")
        assert(
            test_task.get_name() == "Name" and
            test_task.get_deadline() == "Jan 01, 2020 at 12:00 AM" and
            test_task.get_details() == "No details"
        )

    def test_add_and_get_feedback(self):
        test_task = task.Task("Name", "2020/01/01 00:00", "Details")
        test_task.add_feedback("Feedback")
        assert(test_task.get_feedback() == ["Feedback"])

    def test_get_feedback_with_no_feedback(self):
        test_task = task.Task("Name", "2020/01/01 00:00", "Details")
        assert(test_task.get_feedback() == [])

    def test_rm_feedback(self):
        test_task = task.Task("Name", "2020/01/01 00:00", "Details")
        test_task.add_feedback("Feedback")
        assert(test_task.get_feedback() == ["Feedback"])
        test_task.rm_feedback(0)
        assert(test_task.get_feedback() == [])

    def test_rm_feedback_with_no_feedback(self):
        with pytest.raises(IndexError):
            test_task = task.Task("Name", "2020/01/01 00:00", "Details")
            test_task.rm_feedback(0)

    def test_set_details(self):
        test_task = task.Task("Name", "2020/01/01 00:00", "Details")
        test_task.set_details("New Details")
        assert(test_task.get_details() == "New Details")