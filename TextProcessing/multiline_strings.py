use = """ This exact string type
is being use mainly for explaining
the functionality of some function.
"""


# EXAMPLE
def string_concatenation(f_str: str,s_str: str) -> str:
    """
    This function take take two params:
    Both of them - <str><type>

    It concatenate them and returns:
    output - <str>
    """
    final_output = f_str + s_str
    return final_output


print(string_concatenation('Stoqn ', 'Manqka'))