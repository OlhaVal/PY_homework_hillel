from assertpy import assert_that

from PY_homework_hillel.lesson_16.task1.testlead import TeamLead


class TestEmployee:
    qa_team_lead: TeamLead = TeamLead("Olga", 5000, "IT_delivery", 10)

    expected_mark_attrs: dict[str, object] = {
        "_Employee__name": "Olga",
        "_Employee__salary": 5000,
        "_Manager__department": "IT_delivery",
        "_TeamLead__team_size": 10
    }

    def test_employee_attrs(self):
        (assert_that(self.qa_team_lead.__dict__,
                     "Desired User's attrs are not equal to desired user attributes.")
         .is_equal_to(self.expected_mark_attrs))


