"""
Day 2

Project: Helper functions
Description: Not really a project but helper methods I know I'll need later
Examples:
*Verify inputs for string or int or float or bool
*Convert spelled out words to numbers
"""


def clean_input(input):
    # This function will return the proper data type of input
    # such as [int, float, string]
    # Best used with while loop checking if type(return) == [str, int, float]
    # TODO: determine if string is a boolean
    try:
        val = int(input)
        return val
    except ValueError:
        try:
            val = float(input)
            return val
        except ValueError:
            return val
