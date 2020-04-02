## @file test.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief Testing for ScrumBot
#  @date Mar 29, 2020

import pytest
import project
import projectList

## @brief Test Plan Section 3.1.1 Installation
class Test_FR_Installation:
    # All Manual Testing
    pass

## @brief Test Plan Section 3.1.2 Project Creation
class Test_FR_ProjectCreation:
    ## @brief Test_FR_ProjectCreation setup routine for each sub-test
    @pytest.fixture(autouse=True)
    def setup(self):
        self.project_list = projectList.ProjectList()

    ## @brief Test case for project creation
    def test_create_project(self):
        test_project = project.Project("Test Name", "Test Description")
        self.project_list.add(test_project)
        assert (
            self.project_list.to_seq()[0][1].get_name() == "Test Name" and
            self.project_list.to_seq()[0][1].get_desc() == "Test Description"
        )

    ## @brief Test case for project creation without description
    def test_no_description(self):
        test_project = project.Project("Test Name")
        self.project_list.add(test_project)
        assert (
            self.project_list.to_seq()[0][1].get_name() == "Test Name" and
            self.project_list.to_seq()[0][1].get_desc() == "No description"
        )        

## @brief Test Plan Section 3.1.3 Project Removal
class Test_FR_ProjectRemoval:
    ## @brief Test_FR_ProjectRemoval setup routine for each sub-test
    @pytest.fixture(autouse=True)
    def setup(self):
        self.project_list = projectList.ProjectList()
        test_project = project.Project("Test Name", "Test Description")
        self.project_list.add(test_project)

    ## @brief Test case for project removal
    def test_remove_project(self):
        self.project_list.remove(0)
        assert(self.project_list.to_seq() == [])
        
    ## @brief Test case for project removal from empty list
    def test_remove_empty(self):
        with pytest.raises(KeyError):
            projectList.ProjectList().remove(0)

    ## @brief Test case for project removal that is not in list
    def test_remove_item_not_in_list(self):
        with pytest.raises(KeyError):
            self.project_list.remove(1)