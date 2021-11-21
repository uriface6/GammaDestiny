import pandas
from typing import List, Dict
from abc import ABC, abstractmethod


class UserPreferences(ABC):
    """
    Abstract class for input and output between the program to the user.
    """

    def __init__(self, courses_dataframe: pandas.DataFrame):
        """
        Init function for the class. Init the class parameters.
        :param courses_dataframe: The dataframe that contain all the parameters for every course.
        """
        self._courses_dataframe = courses_dataframe

    @abstractmethod
    def get_user_preferences_list(self) -> List[int]:
        """
        Abstract method that get from the user his preferences about every parameter.
        :return: return the user preferences list.
        """
        pass

    @abstractmethod
    def show_top3(self, top3_dict: Dict[str, float]):
        """
        Abstract method that show to user the top 3 matches course.
        :param top3_dict: dict that contain the top 3 matches courses name and match grade.
        """
        pass
