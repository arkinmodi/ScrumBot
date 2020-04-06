## @file test.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief Testing for ScrumBot
#  @date Apr 5, 2020

import pytest
import task, sprint, meeting, project, dict
import projectList
import datetime

## @brief Functional Requirement Tests for BE1 (Test Plan Section 3.1.1)
class Test_FR_BE1:
    # Installation Test Done Manually
    pass

## @brief Functional Requirement Tests for BE2 (Test Plan Section 3.1.2)
class Test_FR_BE2:
    ## @brief Creates a test project and project list for each test
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.test_project = project.Project("Name", "Description")
        self.test_projectList = projectList.ProjectList()

    ## @brief Check if Name and Description is retrieved correctly
    def test_create_project_and_getters(self):
        assert(
            self.test_project.get_name() == "Name" and
            self.test_project.get_desc() == "Description"
        )

    ## @brief Check if Name and Description is retrieved correctly for a project with on description
    def test_create_project_and_getters_with_no_description(self):
        test = project.Project("Name")
        assert(
            test.get_name() == "Name" and
            test.get_desc() == "No description"
        )

    ## @brief Add project to the project list
    def test_add_project_to_list(self):
        self.test_projectList.add(self.test_project)
        assert(self.test_projectList.to_seq()[0][1] == self.test_project)

## @brief Functional Requirement Tests for BE3 (Test Plan Section 3.1.3)
class Test_FR_BE3:
    ## @brief Creates a test project and project list for each test
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.test_project = project.Project("Name", "Description")
        self.test_projectList = projectList.ProjectList()
        self.test_projectList.add(self.test_project)

    ## @brief Checks is it can remove a project from the project list
    def test_remove_project(self):
        assert(self.test_projectList.to_seq()[0][1] == self.test_project)
        self.test_projectList.remove(0)
        assert(self.test_projectList.to_seq() == [])

    ## @brief Tries to remove a project that is not in the project list
    def test_remove_project_not_in_list(self):
        with pytest.raises(KeyError):
            self.test_projectList.remove(1)

## @brief Functional Requirement Tests for BE4 (Test Plan Section 3.1.4)
class Test_FR_BE4:
    ## @brief Creates a test project for each test
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.test_project = project.Project("Name", "Description")
        
    ## @brief Checks if the Task properties are retrieved correctly
    def test_add_and_get_task(self):
        self.test_project.add_sprint()
        self.test_project.add_task("Name", "2020/01/01 00:00", "Details")
        assert(
            self.test_project.get_tasks(0)[0][1][0] == "Name" and
            self.test_project.get_tasks(0)[0][1][1] == "Jan 01, 2020 at 12:00 AM" and
            self.test_project.get_tasks(0)[0][1][2] == "Details"
        )

    ## @brief Checks if the Task properties are retrieved correctly
    def test_add_and_get_task_with_no_details(self):
        self.test_project.add_sprint()
        self.test_project.add_task("Name", "2020/01/01 00:00")
        assert(
            self.test_project.get_tasks(0)[0][1][0] == "Name" and
            self.test_project.get_tasks(0)[0][1][1] == "Jan 01, 2020 at 12:00 AM" and
            self.test_project.get_tasks(0)[0][1][2] == "No details"
        )

    ## @brief Tries to get that Tasks of a Sprint that is not in the list of Sprints
    def test_get_tasks_of_sprint_not_in_list(self):
        with pytest.raises(IndexError):
            self.test_project.get_tasks(0)

    ## @brief Checks if a single Tasks properties are retrieved correctly
    def test_get_single_task(self):
        self.test_project.add_sprint()
        self.test_project.add_task("Name", "2020/01/01 00:00", "Details")
        assert(
            self.test_project.get_task(0, 0)[0] == "Name" and
            self.test_project.get_task(0, 0)[1] == "Jan 01, 2020 at 12:00 AM" and
            self.test_project.get_task(0, 0)[2] == "Details"
        )

    ## @brief Tries to add a Task to a Sprint that does not exist
    def test_add_task_with_no_sprint(self):
        with pytest.raises(IndexError):
            self.test_project.add_task("Name", "2020/01/01 00:00", "Details")

    ## @brief Tries to get a single Task of a Sprint that is not in the list of Sprints
    def test_get_task_with_no_sprint(self):
        with pytest.raises(IndexError):
            self.test_project.get_task(0, 0)

    ## @brief Checks if Feedback is retrieved correctly 
    def test_add_and_get_feedback(self):
        self.test_project.add_sprint()
        self.test_project.add_task("Name", "2020/01/01 00:00", "Details")
        self.test_project.add_feedback(0, "Feedback")
        assert(
            self.test_project.get_feedback(0, 0) == ["Feedback"]
        )

    ## @brief Tries to add Feedback to Sprint not in the list of Sprints
    def test_get_feedback_with_no_sprint(self):
        with pytest.raises(IndexError):
            self.test_project.get_feedback(0, "Feedback")

## @brief Functional Requirement Tests for BE5 (Test Plan Section 3.1.5)
class Test_FR_BE5:
    ## @brief Creates a test project for each test
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.test_project = project.Project("Name", "Description")

    ## @brief Checks if Task is removed
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

    ## @brief Tries to remove a Task of a Sprint that is not in the list of Sprints
    def test_rm_task_with_no_sprint(self):
        with pytest.raises(IndexError):
            self.test_project.rm_task(0)

    ## @brief Tries to remove a Task that is not in the list of Tasks
    def test_rm_task_that_is_not_in_task_list(self):
        with pytest.raises(KeyError):
            self.test_project.add_sprint()
            self.test_project.rm_task(0)

    ## @brief Checks if the Task's details can be updated
    def test_set_task_details(self):
        self.test_project.add_sprint()
        self.test_project.add_task("Name", "2020/01/01 00:00", "Details")
        assert(self.test_project.get_tasks(0)[0][1][2] == "Details")
        self.test_project.set_details(0, "New Details")
        assert(self.test_project.get_tasks(0)[0][1][2] == "New Details")

    ## @brief Tries to update the details of a Task that does not exist
    def test_set_task_details_of_empty_list_of_sprints(self):
        with pytest.raises(IndexError):
            self.test_project.set_details(0, "New Details")

## @brief Functional Requirement Tests for BE6 (Test Plan Section 3.1.6)
class Test_FR_BE6:
    ## @brief Creates a test project for each test
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.test_project = project.Project("Name", "Description")

    ## @brief Tries to add Feedback to a Sprint that is not in the list of Sprints
    def test_add_feedback_with_no_sprint(self):
        with pytest.raises(IndexError):
            self.test_project.add_feedback(0, "Feedback")

    ## @ brief Checks if Feedback is removed
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

    ## @brief Tries to remove Feedback from a Sprint that is not in the list of Sprints
    def test_rm_feedback_with_no_sprint(self):
        with pytest.raises(IndexError):
            self.test_project.rm_feedback(0, 0)

## @brief Functional Requirement Tests for BE7 (Test Plan Section 3.1.7)
class Test_FR_BE7:
    ## @brief Creates a test project for each test
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.test_project = project.Project("Name", "Description")

    ## @brief Checks if Requirement is retrieved correctly
    def test_add_and_get_requirement(self):
        self.test_project.add_rqe("Requirement")
        assert(
            self.test_project.get_rqes() == ["Requirement"]
        )

    ## @brief Checks if Requirement is removed
    def test_rm_requirement(self):
        self.test_project.add_rqe("Requirement")
        assert(self.test_project.get_rqes() == ["Requirement"])
        self.test_project.rm_rqe(0)
        assert(self.test_project.get_rqes() == [])

    ## @brief Tries to remove a Requirement that is not in the list of Requirements
    def test_rm_requirement_not_in_list(self):
        with pytest.raises(IndexError):
            self.test_project.rm_rqe(0)

## @brief Functional Requirement Tests for BE8 (Test Plan Section 3.1.8)
class Test_FR_BE8:
    ## @brief Creates a test project for each test
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.test_project = project.Project("Name", "Description")    
        self.test_project.add_meeting("Name", "2020/01/01 00:00", "grooming", "Description")

    ## @breif Checks if a Meeting's properties are retrieved correctly
    def test_add_and_get_meeting(self):
        assert(
            self.test_project.get_meetings()[0][1][0] == "Name" and
            self.test_project.get_meetings()[0][1][1] == "Jan 01, 2020 at 12:00 AM" and
            self.test_project.get_meetings()[0][1][2] == "GROOMING"
        )

    ## @brief Checks with Meeting name and description getter are correctly functioning
    def test_get_meeting_name_and_description(self):
        assert(
            self.test_project.get_meeting_name(0) == "Name" and
            self.test_project.get_meeting_desc(0) == "Description"
        )

    ## @brief Checks with Meeting name and description getter are correctly functioning
    def test_get_meeting_with_no_description(self):
        self.test_project.add_meeting("Name", "2020/01/01 00:00", "grooming")
        assert(
            self.test_project.get_meeting_desc(1) == "No description"
        )

    ## @brief Tries to get the name of a Meeting that is not in the list of Meetings
    def test_get_meeting_name_of_meeting_not_in_list(self):
        with pytest.raises(KeyError):
            self.test_project.get_meeting_name(2)

    ## @brief Tries to get the description of a Meeting that is not in the list of Meetings
    def test_get_description_of_meeting_not_in_list(self):
        with pytest.raises(KeyError):
            self.test_project.get_meeting_desc(2)

    ## @brief Checks if all valid Meeting Types are correctly registered
    def test_all_meeting_types(self):
        self.test_project.add_meeting("Name", "2020/01/01 00:00", "grooming", "Description")
        self.test_project.add_meeting("Name", "2020/01/01 00:00", "standup", "Description")
        self.test_project.add_meeting("Name", "2020/01/01 00:00", "retrospective", "Description")
        self.test_project.add_meeting("Name", "2020/01/01 00:00", "sprintplanning", "Description")
        assert(
            self.test_project.get_meetings()[1][1][2] == "GROOMING" and
            self.test_project.get_meetings()[2][1][2] == "STANDUP" and
            self.test_project.get_meetings()[3][1][2] == "RETROSPECTIVE" and
            self.test_project.get_meetings()[4][1][2] == "SPRINTPLANNING"
        )

    ## @brief Tries to register and invalid Meeting Type
    def test_invalid_meeting_type(self):
        with pytest.raises(TypeError):
            self.test_project.add_meeting("Name", "2020/01/01 00:00", "dance", "Description")
        
## @brief Functional Requirement Tests for BE9 (Test Plan Section 3.1.9)
class Test_FR_BE9:
    ## @brief Creates a test project for each test
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.test_project = project.Project("Name", "Description")    
        self.test_project.add_meeting("Name", "2020/01/01 00:00", "grooming", "Description")

    ## @brief Checks if Meeting was removed
    def test_rm_meeting(self):
        assert(
            self.test_project.get_meetings()[0][1][0] == "Name" and
            self.test_project.get_meetings()[0][1][1] == "Jan 01, 2020 at 12:00 AM" and
            self.test_project.get_meetings()[0][1][2] == "GROOMING"
        )
        self.test_project.rm_meeting(0)
        assert(
            self.test_project.get_meetings() == []
        )

    ## @brief Tries to remove a Meeting that is not in the list of Meetings
    def test_rm_meeting_with_wrong_key(self):
        with pytest.raises(KeyError):
            self.test_project.rm_meeting(1)

class Test_FR_BE10:
    ## @brief Creates a test project for each test
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.test_project = project.Project("Name", "Description")
        self.test_project.add_meeting("Name", "2020/01/01 00:00", "grooming", "Description")
        self.test_project.add_meeting("Name", "2020/01/01 00:00", "standup", "Description")
        self.test_project.add_meeting("Name", "2020/01/01 00:00", "retrospective", "Description")
        self.test_project.add_meeting("Name", "2020/01/01 00:00", "sprintplanning", "Description")

    ## @brief Checks if all Meeting created are correctly retrieved
    def test_view_all_meeting(self):
        assert(
            len(self.test_project.get_meetings()) == 4 and
            self.test_project.get_meetings()[0][1][2] == "GROOMING" and
            self.test_project.get_meetings()[1][1][2] == "STANDUP" and
            self.test_project.get_meetings()[2][1][2] == "RETROSPECTIVE" and
            self.test_project.get_meetings()[3][1][2] == "SPRINTPLANNING"
        )

class Test_FR_BE11:
    ## @brief Creates a test project for each test
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.test_project = project.Project("Name", "Description")
        self.test_project.add_sprint()

    ## @brief Checks if all Tasks created are correctly retrieved
    def test_view_all_tasks(self):
        self.test_project.add_task("1", "2020/01/01 00:00", "Details")
        self.test_project.add_task("2", "2020/01/01 00:00", "Details")
        self.test_project.add_task("3", "2020/01/01 00:00", "Details")
        assert(
            self.test_project.get_tasks(0)[0][1][0] == "1" and
            self.test_project.get_tasks(0)[1][1][0] == "2" and
            self.test_project.get_tasks(0)[2][1][0] == "3"
        )
