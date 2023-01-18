msg_template = """Hello {name},
Thank you for joining {website}. We are very
happy to have you on board.
"""


def format_msg(my_name="Samuel", my_website="brainzcode.io"):
    my_msg = msg_template.format(name=my_name, website=my_website)
    return my_msg
