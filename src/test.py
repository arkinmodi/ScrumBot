## @file test.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief Testing for ScrumBot
#  @date Mar 29, 2020

import pytest
import project

# Test Plan Section 3.1.1 Installation
class Test_FR_Installation:
    # All Manual Testing
    pass

# Test Plan Section 3.1.2 Project Creation
class Test_FR_ProjectCreation:
    def test_create_project(self):
        test_project = project.Project("Test Name", "Test Description")
        assert( test_project.get_name() == "Test Name" and 
                test_project.get_desc() == "Test Description")

    def test_no_description(self):
        test_project = project.Project("Test Name")
        assert( test_project.get_name() == "Test Name" and 
                test_project.get_desc() == "No description")

# Test Plan Section 3.1.3 Project Removal
class Test_FR_ProjectRemoval:
    pass
