import pandas
import itertools
from typing import List, Dict


class DataManager:
    """
    Class that manage all the data.
    The class use to calculate the match between the user preferences to every course,
    and then to get the top 3 matches course.
    """

    def __init__(self, user_preferences_list: List[int], courses_dataframe: pandas.DataFrame):
        """
        Init function for the class.
        Init the class parameters and create dict for course match.
        :param user_preferences_list: The list with the preferences for all parameters from the user.
        :param courses_dataframe: The dataframe that contain all the parameters for every course.
        """
        self._user_preferences_list = user_preferences_list
        self._course_match_dict: Dict[str, float] = {}
        self._courses_dataframe = courses_dataframe

    def _calculate_course_match(self):
        """
        This function calculate the match for every course,
        and then update the dict that contain this data.
        The function run on every course, and with Weighted arithmetic mean
        calculate the match between the course parameters to user preferences.
        """
        course_match_list = []
        weight_column_name = self._courses_dataframe.columns[1]

        for curr_course in self._courses_dataframe.columns[2:]:
            course_match_list.clear()
            weight_sum = 0
            for course_grade, user_grade, parameter_weight in \
                    zip(self._courses_dataframe[curr_course],
                        self._user_preferences_list,
                        self._courses_dataframe[weight_column_name]):
                if user_grade != 0:
                    # We take the distance between user grade to the course grade,
                    # then sub him from 5 and multiply in 20 to get result in percents.
                    # finally multiply in parameter weight
                    course_match_list.append((5 - abs(user_grade - course_grade)) * 20 * parameter_weight)
                    weight_sum += parameter_weight

            self._course_match_dict[curr_course] = round(sum(course_match_list) / weight_sum, 2)

    def get_top3_course(self) -> Dict[str, float]:
        """
        This function called for _calculate_course_match function
        for fill the course match dict.
        Then, sorted the dict.
        And finally return the top 3 matches course.
        :return: top3_dict: dict that contain the top 3 matches courses name and match grade.
        """
        self._calculate_course_match()
        sorted_dict = {k: v for k, v in sorted(self._course_match_dict.items(), key=lambda item: item[1], reverse=True)}
        self._course_match_dict = sorted_dict
        top3_dict = dict(itertools.islice(self._course_match_dict.items(), 3))
        return top3_dict
