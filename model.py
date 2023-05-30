class PhoneBook:

    def __init__(self, path: str = 'phone.txt'):

        self.phone_book: list[dict[str, str]] = []
        self.path = path

    def open(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for contact in data:
            contact = [i.strip() for i in contact.split(':')]
            if len(contact) == 3:
                self.phone_book.append({'name': contact[0], 'phone': contact[1], 'comment': contact[2]})

    def save(self):
        data = []
        for contact in self.phone_book:
            contact = ':'.join([value for value in contact.values()])
            data.append(contact)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write('\n'.join(data))

    def load(self) -> list[dict[str, str]]:
        return self.phone_book

    def add(self, contact: dict[str, str]):
        self.phone_book.append(contact)
        return contact.get('name')

    def delete(self, index: int):
        return self.phone_book.pop(index - 1).get('name')

    def find(self, to_find: str) -> dict:
        if to_find:
            for contact in self.phone_book:
                if to_find in contact.get("name"):
                    return contact

    def change(self, a: bool, contact1: dict[str, str], contact2: dict[str, str]):
        if a:
            new_list = []
            for contact in self.phone_book:
                if contact != contact1:
                    new_list.append(":".join((contact['name'], contact['phone'], contact['comment'])))
                else:
                    new_list.append(":".join((contact2['name'], contact2['phone'], contact2['comment'])))
            with open(self.path, 'w', encoding='utf-8') as file:
                for i in new_list:
                    file.write(i + '\n')
