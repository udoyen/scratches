import re


def validate(code):
    sample_code = """def validate(()):\n    return"""
    if not re.match(r"def", code):
        return "missing def"
    # if not re.match(r"\*:", code):
    #     return "missing :"
    if not re.match(r"(.*)", code):
        return "missing param"
    if not re.match(r"\(\)", code):
        return "missing paren"
    if not re.match("\n\\s{4}return", code):
        return "missing indent"
    if not re.match("validate", code):
        return "wrong name"
    if not re.match("return", code):
        return "missing return"

    return True


data = 'def foo(x):\nprint(123)'

validate(data)
