## @file test.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief Testing for ScrumBot
#  @date Mar 29, 2020

import pytest
import task
import sprint
import datetime

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

class Test_Sprint:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.test_sprint = sprint.Sprint()

    def test_create_sprint_and_getters(self):
        assert(type(self.test_sprint) == sprint.Sprint)

    def test_sprint_date(self):
        today = datetime.date.today()
        assert(today.strftime("%b %d, %Y") == self.test_sprint.get_date())

    def test_add_and_get_tasks(self):
        self.test_sprint.add_task("Name", "2020/01/01 00:00", "Details")
        assert(
            self.test_sprint.get_tasks()[0][1][0] == "Name" and
            self.test_sprint.get_tasks()[0][1][1] == "Jan 01, 2020 at 12:00 AM" and
            self.test_sprint.get_tasks()[0][1][2]== "Details"
        )

    def test_add_and_get_tasks_with_no_details(self):
        self.test_sprint.add_task("Name", "2020/01/01 00:00")
        assert(
            self.test_sprint.get_tasks()[0][1][0] == "Name" and
            self.test_sprint.get_tasks()[0][1][1] == "Jan 01, 2020 at 12:00 AM" and
            self.test_sprint.get_tasks()[0][1][2]== "No details"
        )

    def test_get_single_task(self):
        self.test_sprint.add_task("Name", "2020/01/01 00:00", "Details")
        assert(
            self.test_sprint.get_task(0)[0] == "Name" and
            self.test_sprint.get_task(0)[1] == "Jan 01, 2020 at 12:00 AM" and
            self.test_sprint.get_task(0)[2]== "Details"
        )

    def test_get_single_task_with_no_details(self):
        self.test_sprint.add_task("Name", "2020/01/01 00:00")
        assert(
            self.test_sprint.get_task(0)[0] == "Name" and
            self.test_sprint.get_task(0)[1] == "Jan 01, 2020 at 12:00 AM" and
            self.test_sprint.get_task(0)[2]== "No details"
        )

    def test_rm_task(self):
        self.test_sprint.add_task("Name", "2020/01/01 00:00", "Details")
        assert(self.test_sprint.get_tasks()[0][1][0] == "Name")
        self.test_sprint.rm_task(0)
        assert(len(self.test_sprint.get_tasks()) == 0)

    def test_rm_task_with_no_tasks(self):
        with pytest.raises(KeyError):
            self.test_sprint.rm_task(0)

    def test_add_and_get_feedback(self):
        self.test_sprint.add_task("Name", "2020/01/01 00:00", "Details")
        self.test_sprint.add_feedback(0, "Feedback")
        assert(self.test_sprint.get_feedback(0) == ["Feedback"])

    def test_add_feedback_to_no_task(self):
        with pytest.raises(KeyError):
            self.test_sprint.add_feedback(0, "Feedback")

    def test_rm_feedback(self):
        self.test_sprint.add_task("Name", "2020/01/01 00:00", "Details")
        self.test_sprint.add_feedback(0, "Feedback")
        assert(self.test_sprint.get_feedback(0) == ["Feedback"])
        self.test_sprint.rm_feedback(0, 0)
        assert(self.test_sprint.get_feedback(0) == [])

    def test_rm_feedback_to_no_task(self):
        with pytest.raises(KeyError):
            self.test_sprint.rm_feedback(1, 0)

    def test_set_details(self):
        self.test_sprint.add_task("Name", "2020/01/01 00:00", "Details")
        self.test_sprint.set_details(0, "New Details")
        assert(self.test_sprint.get_task(0)[2]== "New Details")

    def test_set_details_with_no_task(self):
        with pytest.raises(KeyError):
            self.test_sprint.set_details(0, "New Details")