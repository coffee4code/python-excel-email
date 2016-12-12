def col_to_num(col_str, real_index):
    expn = 0
    col_num = 0
    for char in reversed(col_str):
        col_num += (ord(char) - ord('A') + 1) * (26 ** expn)
        expn += 1

    col_num = col_num-1 if real_index else col_num
    return col_num


def log_separator():
    print("************************************************************************\r\n")


def log_text(text_str):
    print(text_str)


def prompt_question(text_question):
    user_input = input(text_question)
    if user_input.lower() in ['y', 'yes']:
        return True
    return False

