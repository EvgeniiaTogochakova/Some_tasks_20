import text


def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)


def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def print_contact(pb: list[dict[str, str]], error: str):
    if pb:
        print('\n' + '=' * 71)
        for i, contact in enumerate(pb, 1):
            print(f'{i:>3}. {contact.get("name"):<20} | {contact.get("phone"): <20} | {contact.get("comment"): <20}')
        print('=' * 71 + '\n')
    else:
        print_message(error)


def input_contact(message: str, cancel: str) -> dict:
    contact = {}
    print(message)
    for key, value in text.input_contact.items():
        data = ' '.join([i.capitalize() for i in input(value).split()])
        # data = input(value)
        if data:
            contact[key] = data
        else:
            print_message(cancel)
    return contact


def input_index(message: str, pb: list, error: str) -> int:
    print_contact(pb, error)
    while True:
        index = input(message)
        if index.isdigit() and 0 < int(index) < len(pb) + 1:
            return int(index)


def ask_what_name_to_find(question: str, message1: str, message2: str, cancel: str) -> str:
    print(question)
    str_1 = input(message1).capitalize().strip()
    str_2 = input(message2).capitalize().strip()
    if len(str_1 + str_2) == 0:
        print(cancel)
    elif len(str_1) != 0 and len(str_2) == 0:
        name_to_find = str_1
        print(name_to_find)
        return name_to_find
    elif len(str_1) == 0 and len(str_2) != 0:
        name_to_find = str_2
        print(name_to_find)
        return name_to_find
    else:
        name_to_find = str_1 + ' ' + str_2
        print(name_to_find)
        return name_to_find


def print_one_contact(message1: str, message2: str, contact: dict[str, str]):
    if contact != None:
        print(message1)
        print(f'{contact.get("name")}: {contact.get("phone")}: {contact.get("comment")}')
    else:
        print(message2)


def confirmation(message: str) -> bool:
    confirmation = input(message)
    return confirmation.isdigit()


def to_get_new_data(a: bool, message1: str, message2: str, message3: str) -> dict[str, str]:
    if a:
        name_changed = input(message1)
        name_changed = ' '.join([i.capitalize() for i in name_changed.split()])
        phone_changed = input(message2)
        phone_changed = ' '.join([i for i in phone_changed.split()])
        comment_changed = input(message3)
        comment_changed = ' '.join([i for i in comment_changed.split()])
        contact_changed = {'name': name_changed, 'phone': phone_changed, 'comment': comment_changed}
        return contact_changed


def after_changing(a: bool, message1: str, message2: str):
    if a:
        print(message1)
    else:
        print(message2)
