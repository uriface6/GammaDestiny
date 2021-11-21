import pandas as pd
from data_mannager import DataManager
from user_preferences import UserPreferences
from cmd_user_preferences import CmdUserPreferences


def main():
    """
    The main function.
    Read the courses data with pandas.
    Get the user preferences with UserPreferences.
    Calculate the top 3 matches course with DataManager.
    And finally show the results for the user with UserPreferences.
    """

    # temp list for checking
    user_preferences_list = [4, 2, 2, 5, 4, 2, 2, 5, 5, 1, 3, 4, 3, 4]

    course_data_df = pd.read_excel("CoursesData.xlsx")

    my_user_preferences: UserPreferences = CmdUserPreferences(course_data_df)
    user_preferences_list = my_user_preferences.get_user_preferences_list()

    my_data_manager = DataManager(user_preferences_list, course_data_df)
    my_user_preferences.show_top3(my_data_manager.get_top3_course())


if __name__ == '__main__':
    main()


