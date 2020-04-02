## @file test.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief Testing for ScrumBot
#  @date Apr 2, 2020

import pytest
import task, sprint, meeting, project, dict
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

    def test_sprint_custom_date(self):
        test = sprint.Sprint("2020/01/01")
        assert(test.get_date() == "Jan 01, 2020")

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

    def test_get_task_not_in_list(self):
        assert(self.test_sprint.get_task(0) == None)

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

    def test_get_feedback_from_not_existing_task(self):
        with pytest.raises(KeyError):
            self.test_sprint.get_feedback(0)

    def test_add_feedback_with_no_task(self):
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

    def test_add_task_from_file(self):
        self.test_sprint.add_task_from_file(0, "Name", "2020/01/01 00:00", "Details")
        assert(
            self.test_sprint.get_tasks()[0][1][0] == "Name" and
            self.test_sprint.get_tasks()[0][1][1] == "Jan 01, 2020 at 12:00 AM" and
            self.test_sprint.get_tasks()[0][1][2]== "Details"
        )

    def test_add_task_from_file_with_no_details(self):
        self.test_sprint.add_task_from_file(0, "Name", "2020/01/01 00:00")
        assert(
            self.test_sprint.get_tasks()[0][1][0] == "Name" and
            self.test_sprint.get_tasks()[0][1][1] == "Jan 01, 2020 at 12:00 AM"
        )

    def test_get_last_task_id(self):
        self.test_sprint.add_task_from_file(0, "Name", "2020/01/01 00:00")
        self.test_sprint.add_task_from_file(1, "Name", "2020/01/01 00:00")
        assert(self.test_sprint.get_last_task_id() == 1)

    def test_get_last_task_id_with_no_tasks(self):
        assert(self.test_sprint.get_last_task_id() == -1)

class Test_Meetings:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.test_meeting = meeting.Meeting("Name", "2020/01/01 00:00", "grooming", "Description")

    def test_create_meeting_and_getters(self):
        assert(
            self.test_meeting.get_name() == "Name" and
            self.test_meeting.get_datetime() == "Jan 01, 2020 at 12:00 AM" and
            self.test_meeting.get_type() == "GROOMING" and
            self.test_meeting.get_desc() == "Description"
        )

    def test_create_meeting_and_getters_with_no_description(self):
        test = meeting.Meeting("Name", "2020/01/01 00:00", "grooming")
        assert(
            test.get_name() == "Name" and
            test.get_datetime() == "Jan 01, 2020 at 12:00 AM" and
            test.get_type() == "GROOMING" and
            test.get_desc() == "No description"
        )

    def test_set_description(self):
        self.test_meeting.set_desc("New Description")
        assert(self.test_meeting.get_desc() == "New Description")

    def test_diff_meeting_types(self):
        grooming = meeting.Meeting("Name", "2020/01/01 00:00", "grooming", "Description")
        standup = meeting.Meeting("Name", "2020/01/01 00:00", "standup", "Description")
        retrospective = meeting.Meeting("Name", "2020/01/01 00:00", "retrospective", "Description")
        sprintplanning = meeting.Meeting("Name", "2020/01/01 00:00", "sprintplanning", "Description")
        assert(
            grooming.get_type() == "GROOMING" and
            standup.get_type() == "STANDUP" and
            retrospective.get_type() == "RETROSPECTIVE" and
            sprintplanning.get_type() == "SPRINTPLANNING"
        )

    def test_invalid_meeting_type(self):
        with pytest.raises(TypeError):
            meeting.Meeting("Name", "2020/01/01 00:00", "dance", "Description")

class Test_Project:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.test_project = project.Project("Name", "Description")

    def test_create_meeting_and_getters(self):
        assert(
            self.test_project.get_name() == "Name" and
            self.test_project.get_desc() == "Description"
        )

    def test_create_meeting_and_getters_with_no_description(self):
        test = project.Project("Name")
        assert(
            test.get_name() == "Name" and
            test.get_desc() == "No description"
        )

    def test_add_and_get_meeting(self):
        self.test_project.add_meeting("Name", "2020/01/01 00:00", "grooming", "Description")
        assert(
            self.test_project.get_meetings()[0][1][0] == "Name" and
            self.test_project.get_meetings()[0][1][1] == "Jan 01, 2020 at 12:00 AM" and
            self.test_project.get_meetings()[0][1][2] == "GROOMING"
        )

    def test_get_meeting_name_and_description(self):
        self.test_project.add_meeting("Name", "2020/01/01 00:00", "grooming", "Description")
        assert(
            self.test_project.get_meeting_name(0) == "Name" and
            self.test_project.get_meeting_desc(0) == "Description"
        )

    def test_get_meeting_name_of_meeting_not_in_list(self):
        with pytest.raises(KeyError):
            self.test_project.get_meeting_name(0)

    def test_get_description_of_meeting_not_in_list(self):
        with pytest.raises(KeyError):
            self.test_project.get_meeting_desc(0)

    def test_rm_meeting(self):
        self.test_project.add_meeting("Name", "2020/01/01 00:00", "grooming", "Description")
        assert(
            self.test_project.get_meetings()[0][1][0] == "Name" and
            self.test_project.get_meetings()[0][1][1] == "Jan 01, 2020 at 12:00 AM" and
            self.test_project.get_meetings()[0][1][2] == "GROOMING"
        )
        self.test_project.rm_meeting(0)
        assert(
            self.test_project.get_meetings() == []
        )

    def test_rm_meeting_with_wrong_key(self):
        with pytest.raises(KeyError):
            self.test_project.rm_meeting(0)

    def test_meeting_last_id(self):
        self.test_project.add_meeting("Name", "2020/01/01 00:00", "grooming", "Description")
        assert(self.test_project.get_last_meeting_id() == 0)

    def test_set_meeting_desc(self):
        self.test_project.add_meeting("Name", "2020/01/01 00:00", "grooming", "Description")
        assert(self.test_project.get_meeting_desc(0) == "Description")
        self.test_project.set_meeting_desc(0, "New Description")
        assert(self.test_project.get_meeting_desc(0) == "New Description")

    def test_set_meeting_desc_of_meeting_not_in_list(self):
        with pytest.raises(KeyError):
            self.test_project.set_meeting_desc(0, "New Description")

    def test_add_and_get_requirement(self):
        self.test_project.add_rqe("Requirement")
        assert(
            self.test_project.get_rqes() == ["Requirement"]
        )

    def test_rm_requirement(self):
        self.test_project.add_rqe("Requirement")
        assert(self.test_project.get_rqes() == ["Requirement"])
        self.test_project.rm_rqe(0)
        assert(self.test_project.get_rqes() == [])

    def test_rm_requirement_not_in_list(self):
        with pytest.raises(IndexError):
            self.test_project.rm_rqe(0)

    def test_add_and_get_sprints(self):
        self.test_project.add_sprint()
        assert(
            len(self.test_project.get_sprints()) == 1
        )

    def test_rm_sprint(self):
        self.test_project.add_sprint()
        assert(len(self.test_project.get_sprints()) == 1)
        self.test_project.rm_sprint()
        assert(len(self.test_project.get_sprints()) == 0)

    def test_rm_sprint_not_in_list(self):
        with pytest.raises(IndexError):
            self.test_project.rm_sprint()

    def test_set_description(self):
        self.test_project.set_desc("New Description")
        assert(
            self.test_project.get_desc() == "New Description"
        )

    def test_add_and_get_task(self):
        self.test_project.add_sprint()
        self.test_project.add_task("Name", "2020/01/01 00:00", "Details")
        assert(
            self.test_project.get_tasks(0)[0][1][0] == "Name" and
            self.test_project.get_tasks(0)[0][1][1] == "Jan 01, 2020 at 12:00 AM" and
            self.test_project.get_tasks(0)[0][1][2] == "Details"
        )

    def test_get_tasks_of_sprint_not_in_list(self):
        with pytest.raises(IndexError):
            self.test_project.get_tasks(0)

    def test_get_single_task(self):
        self.test_project.add_sprint()
        self.test_project.add_task("Name", "2020/01/01 00:00", "Details")
        assert(
            self.test_project.get_task(0, 0)[0] == "Name" and
            self.test_project.get_task(0, 0)[1] == "Jan 01, 2020 at 12:00 AM" and
            self.test_project.get_task(0, 0)[2] == "Details"
        )

    def test_add_task_with_no_sprint(self):
        with pytest.raises(IndexError):
            self.test_project.add_task("Name", "2020/01/01 00:00", "Details")

    def test_get_task_with_no_sprint(self):
        with pytest.raises(IndexError):
            self.test_project.get_task(0, 0)

    def test_rm_task(self):
        self.test_project.add_sprint()
        self.test_project.add_task("Name", "2020/01/01 00:00", "Details")
        assert(
            self.test_project.get_tasks(0)[0][1][0] == "Name" and
            self.test_project.get_tasks(0)[0][1][1] == "Jan 01, 2020 at 12:00 AM" and
            self.test_project.get_tasks(0)[0][1][2] == "Details"
        )
        self.test_project.rm_task(0)
        assert(
            self.test_project.get_tasks(0) == []
        )

    def test_rm_task_with_no_sprint(self):
        with pytest.raises(IndexError):
            self.test_project.rm_task(0)

    def test_set_task_details(self):
        self.test_project.add_sprint()
        self.test_project.add_task("Name", "2020/01/01 00:00", "Details")
        assert(self.test_project.get_tasks(0)[0][1][2] == "Details")
        self.test_project.set_details(0, "New Details")
        assert(self.test_project.get_tasks(0)[0][1][2] == "New Details")

    def test_set_task_details_of_empty_list_of_sprints(self):
        with pytest.raises(IndexError):
            self.test_project.set_details(0, "New Details")

    def test_add_and_get_feedback(self):
        self.test_project.add_sprint()
        self.test_project.add_task("Name", "2020/01/01 00:00", "Details")
        self.test_project.add_feedback(0, "Feedback")
        assert(
            self.test_project.get_feedback(0, 0) == ["Feedback"]
        )

    def test_add_feedback_with_no_sprint(self):
        with pytest.raises(IndexError):
            self.test_project.add_feedback(0, "Feedback")

    def test_get_feedback_with_no_sprint(self):
        with pytest.raises(IndexError):
            self.test_project.get_feedback(0, "Feedback")

    def test_rm_feedback(self):
        self.test_project.add_sprint()
        self.test_project.add_task("Name", "2020/01/01 00:00", "Details")
        self.test_project.add_feedback(0, "Feedback")
        assert(
            self.test_project.get_feedback(0, 0) == ["Feedback"]
        )
        self.test_project.rm_feedback(0, 0)
        assert(
            self.test_project.get_feedback(0, 0) == []
        )

    def test_rm_feedback_with_no_sprint(self):
        with pytest.raises(IndexError):
            self.test_project.rm_feedback(0, 0)

    def test_update_meeting(self):
        self.test_project.add_meeting("Name", "2020/01/01 00:00", "grooming", "Description")
        assert(
            self.test_project.get_meetings()[0][1][0] == "Name" and
            self.test_project.get_meetings()[0][1][1] == "Jan 01, 2020 at 12:00 AM" and
            self.test_project.get_meetings()[0][1][2] == "GROOMING" and
            self.test_project.get_meeting_desc(0) == "Description"
        )
        self.test_project.update_meeting(0, "New Name", "2020/01/01 00:01", "standup", "New Description")
        assert(
            self.test_project.get_meetings()[0][1][0] == "New Name" and
            self.test_project.get_meetings()[0][1][1] == "Jan 01, 2020 at 12:01 AM" and
            self.test_project.get_meetings()[0][1][2] == "STANDUP" and
            self.test_project.get_meeting_desc(0) == "New Description"
        )

    def test_update_meeting_with_no_description(self):
        self.test_project.add_meeting("Name", "2020/01/01 00:00", "grooming", "Description")
        assert(
            self.test_project.get_meetings()[0][1][0] == "Name" and
            self.test_project.get_meetings()[0][1][1] == "Jan 01, 2020 at 12:00 AM" and
            self.test_project.get_meetings()[0][1][2] == "GROOMING" and
            self.test_project.get_meeting_desc(0) == "Description"
        )
        self.test_project.update_meeting(0, "New Name", "2020/01/01 00:01", "standup")
        assert(
            self.test_project.get_meetings()[0][1][0] == "New Name" and
            self.test_project.get_meetings()[0][1][1] == "Jan 01, 2020 at 12:01 AM" and
            self.test_project.get_meetings()[0][1][2] == "STANDUP" and
            self.test_project.get_meeting_desc(0) == "No description"
        )

    def test_add_sprint_from_file(self):
        self.test_project.add_sprint_from_file("2020/01/01")
        assert(len(self.test_project.get_sprints()) == 1)

    def test_add_task_from_file(self):
        self.test_project.add_sprint()
        self.test_project.add_task_from_file(0, "Name", "2020/01/01 00:00", "Details")
        assert(
            self.test_project.get_tasks(0)[0][1][0] == "Name" and
            self.test_project.get_tasks(0)[0][1][1] == "Jan 01, 2020 at 12:00 AM" and
            self.test_project.get_tasks(0)[0][1][2] == "Details"
        )

    def test_add_task_from_file_no_details(self):
        self.test_project.add_sprint()
        self.test_project.add_task_from_file(0, "Name", "2020/01/01 00:00")
        assert(
            self.test_project.get_tasks(0)[0][1][0] == "Name" and
            self.test_project.get_tasks(0)[0][1][1] == "Jan 01, 2020 at 12:00 AM"
        )

    def test_add_task_from_file_with_no_sprints(self):
        with pytest.raises(IndexError):
            self.test_project.add_task_from_file(0, "Name", "2020/01/01 00:00")

    def test_get_last_task_id(self):
        self.test_project.add_sprint()
        self.test_project.add_task_from_file(0, "Name", "2020/01/01 00:00", "Details")
        self.test_project.add_task_from_file(1, "Name", "2020/01/01 00:00", "Details")
        assert(
            self.test_project.get_last_task_id() == 1
        )

    def test_get_last_task_id_with_no_tasks(self):
        self.test_project.add_sprint()
        assert(self.test_project.get_last_task_id() == -1)

class Test_Dictionary:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.test_dict = dict.Dict()

    def test_create_dict_and_to_sequence(self):
        assert(self.test_dict.to_seq() == [])

    def test_add_to_dict(self):
        self.test_dict.add(0)
        assert(self.test_dict.to_seq() == [[0, 0]])
        self.test_dict.add(0)
        assert(self.test_dict.to_seq() == [[0, 0], [1, 0]])

    def test_update_dict(self):
        self.test_dict.add(0)
        assert(self.test_dict.to_seq() == [[0, 0]])
        self.test_dict.update(0, 1)
        assert(self.test_dict.to_seq() == [[0, 1]])

    def test_remove_dict(self):
        self.test_dict.add(0)
        assert(self.test_dict.to_seq() == [[0, 0]])
        self.test_dict.remove(0)
        assert(self.test_dict.to_seq() == [])

    def test_remove_dict_not_in_dict(self):
        with pytest.raises(KeyError):
            self.test_dict.remove(0)

    def test_get_last_id(self):
        self.test_dict.add(0)
        self.test_dict.add(0)
        assert(self.test_dict.get_last_id() == 1)