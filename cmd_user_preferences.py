from user_preferences import UserPreferences
from typing import List, Dict


class CmdUserPreferences(UserPreferences):
    """
    Class that extend from UserPreferences class,
    and manage the input and output with the user in the cmd (input and print)
    """

    def get_user_preferences_list(self) -> List[int]:
        """
        Method that get from the user his preferences about every parameter.
        The method use the cmd for input.
        :return: return the user preferences list.
        """
        first_column_name = self._courses_dataframe.columns[0]
        print("Welcome to GammaDestiny!!!")
        print("The questionnaire that help you to find your destiny in gamma courses!")
        print(f"There is a {len(self._courses_dataframe[first_column_name])} questions")
        print("Every question you need to choose between 5 to 1")
        print("5. Particularly interested. 1. Not interested at all")
        print("If It doesn't matter, Enter 0\n")

        user_preferences_list = []
        for parameter_name in self._courses_dataframe[first_column_name]:
            print(f"{parameter_name} :")
            user_preferences_list.append(self.get_user_int_choice(0, 5))

        return user_preferences_list

    def show_top3(self, top3_dict: Dict[str, float]):
        """
        Method that show to user the top 3 matches course.
        The method use the cmd for print output.
        :param top3_dict: dict that contain the top 3 matches courses name and match grade.
        """
        print("We found your destiny in gamma: ")
        for idx, k_v in enumerate(top3_dict.items()):
            print(f"{idx + 1}. {k_v[0]} with {k_v[1]}% match")

    @staticmethod
    def get_user_int_choice(min: int, max: int) -> int:
        """
        Static method that help to input number in range from the user.
        The function run until the user enter number in the range.
        :param min: the minimum number that user can choose.
        :param max: the maximum number that user can choose.
        :return: user_choice_int: the valid user input.
        """
        user_choice_str = ""
        user_choice_int = min - 1
        while min > user_choice_int or max < user_choice_int:
            user_choice_str = input(f"Enter number between {min} to {max}: ")
            try:
                user_choice_int = int(user_choice_str)
            except ValueError:
                print("Enter valid number!")
        return user_choice_int
