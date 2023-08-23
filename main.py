def menu():
    menu_points = ['Open file',
                   'Save file',
                   'Open all contacts',
                   'Add contact',
                   'Find contact',
                   'Edit contact',
                   'Delete contact',
                   'Exit']
    print('Main menu')
    [print(f'\t{i}. {item}') for i, item in enumerate(menu_points, 1)]
    choice = int(input('Choose a menu item: '))
    return choice
    

def open_file(book: dict):
    with open(PATH, 'a', encoding='UTF-8') as file:
        data = file.readlines()
    for i, contact in enumerate(data, 1):
        contact = contact.strip().split(';')
        book[i] = contact


def func_search(book: dict):
    search = input('What are looking for?')
    result = find_contact(phone_book, search)
    show_contacts(result, f'Contact includes {search} not in book!')


def change_contact(book: dict, cid: int):
    name, phone, comment = book.get(cid)
    ch = []
    for item in ['Enter a new name or left empty to skip changes: ',
                 'Enter phone or left empty to skip changes: ',
                 'Enter comment or left empty to skip changes: ']:
        new_contact.append(input(item))
    book[cid] = [ch[0] if ch[0] else name,
                 ch[1] if ch[1] else phone,
                 ch[2] if ch[2] else comment]
    return ch[0] if ch[0] else name


def show_contacts(book: dict, message):
    print('\n' + '=' * 67)
    if book:
        for i, contact in book.items:
            print(f'{i:>3}. {contact[0]:<20} {contact[1]:<20} {contact[2]:<20}')
    else:
        print(message)    
    print('=' * 67)


def add_new_contacts(book: dict, new: list):
    cur_id = max(book.keys()) + 1
    book[cur_id] = new


def save_file(book: dict):
    all_contacts = []
    for contact in book.values():
        all_contacts.append(';'.join(contact))
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(all_contacts))


def find_contact(book: dict, search: str):
    result = {}
    for i, contact in book.items:
        for field in contact:
            if search.lower() in field.lower():
                result[i] = contact
                break
    return result


def delete_contact(book: dict, cid: int):
    name = book.pop(cid)
    return name[0]


phone_book = {}
PATH = 'phones.txt'
while True:
    choice = menu()
    match choice:
        case 1:
            open_file(phone_book)
            print('\nPhone book has open!')
        case 2:
            save_file(phone_book)
            print('\nPhone book has saved!')
        case 3:
            pass
        case 4:
            new_contact = []
            for item in ['Enter name: ', 'Enter phone: ', 'Enter comment: ']:
                new_contact.append(input(item))
            add_new_contacts(phone_book, new_contact)
        case 5:
            func_search(phone_book)
        case 6:
            pass
        case 7:
            pass
        case 8:
            pass