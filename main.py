documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
    }

def docpeople():
    doc_num_input = input('Введите номер документа: ') 
    for doc_info in documents:
        if doc_num_input == doc_info.get('number'):
            print(doc_info.get('name'))
            break
    else:
        print(f'Документа с номером {doc_num_input} нет в каталоге')

def docshelf():
    doc_num_input = input('Введите номер документа: ')
    for key, value in directories.items():
        if doc_num_input in value:
            print(f'Документ с номером {doc_num_input} находится на полке №{key}')
            break
    else:
        print(f'Документа с номером {doc_num_input} нет в картотеке')

def doclist():
    print('В каталоге содержаться следующие документы: ')
    for doc_info in documents:
        value_list = list(doc_info.values())
        print(', '.join(value_list))

def docadd():
    doc_number = input('Введите номер документа: ')
    doc_type = input('Введите тип документа: ')
    doc_owner_name = input('Введите имя владельца документа: ')
    shelf_for_doc = input('Введите номер полки для хранения документа: ')

    new_doc = {}
    new_doc['type'] = doc_type
    new_doc['number'] = doc_number
    new_doc['name'] = doc_owner_name

    for key, value in directories.items():
        if key == shelf_for_doc:
            value.append(doc_number)
            documents.append(new_doc)
            print(f'Документ №{doc_number} добавлен на полку №{shelf_for_doc}')
            break
    else:
        print('Полки, на которую вы хотите поместить документ не существует')

def docdel():

    docdir_list = []
    docshel_list = []

    doc_number_input = input('Введите номер документа: ')

    for value in directories.values():
        for doc_number in value:
            docshel_list.append(doc_number)

    for documents_dict in documents:
        docdir_list.append(documents_dict.get('number'))

    if doc_number_input in docshel_list:
        for value in directories.values():
            for doc_number in value:
                if doc_number == doc_number_input:
                    value.pop(value.index(doc_number_input))
                    print(f'Документ №{doc_number_input} удален из картотеки')

    else:
        print('Такого документа нет в картотеке.')

    if doc_number_input in docdir_list:
        for documents_dict in documents:
            if doc_number_input == documents_dict.get('number'):
                documents.pop(documents.index(documents_dict))
                print(f'Документ №{doc_number_input} удален из каталога')
    else:
        print('Такого документа нет в каталоге. Пожалуйста, ознакомтесь со списком документов в каталоге')

def docmove():
    docnum_move_input = input('Введите номер документа, который вы хотите переместить: ')
    shelfnum_input = input('Введите номер полки, на которую вы хотите переместить документ: ')
    moved_doc = []

    for value in directories.values():
        for doc_number in value:
            moved_doc.append(doc_number)

    if shelfnum_input in directories.keys():
        if docnum_move_input in moved_doc:
            for value in directories.values():
                for doc_number in value:
                    if docnum_move_input == doc_number:
                        remove_doc = value.pop(value.index(docnum_move_input))
                        for key, value in directories.items():
                            if shelfnum_input == key:
                                value.append(remove_doc)
            print(f'Документ №{docnum_move_input} перенесен на полку №{shelfnum_input}')

    if docnum_move_input not in moved_doc and shelfnum_input in directories.keys():
        print('Документа с таким номером нет в картотеке')
    elif docnum_move_input in moved_doc and shelfnum_input not in directories.keys():
        print('Полки с таким номером нет в картотеке')
    elif docnum_move_input not in moved_doc and shelfnum_input not in directories.keys():
        print('Документа с таким номером нет в картотеке')
        print('Полки с таким номером нет в картотеке')

    
def addshelf():

    shelf_add = input('Укажите номер полки для внесения в картотеку: ')
    if shelf_add not in directories.keys():
        for key in directories.keys():
            if shelf_add != key:
                new_shelf = {shelf_add : []}
                directories.update(new_shelf)
                print(f'В картотеку добавлена полка №{shelf_add}')
                break       
    else:
        print('Эта полка уже существует в картотеке. Укажите другой номер для новой полки')

def personfind():
    
    for document in documents:  
        try:
            print(f'{document["name"]}')
        except KeyError:
            print('В document нет name')

def doccheck():
    doccat_set = set()
    docshel_set = set()

    for value in directories.values():
        for doc_number in value:
            docshel_set.add(doc_number)

    for documents_dict in documents:
        doccat_set.add(documents_dict.get('number'))

    set_dif1 = docshel_set.difference(doccat_set)
    set_dif2 = doccat_set.difference(docshel_set)

    if set_dif1 != set():
        for doc in set_dif1:
            print(f'Неизвестна принадлежность документ №{doc}. Документа нет в documents')
            
    if set_dif2 != set():
        for doc in set_dif2:
           print(f'Документа №{doc} нет в directories') 


def docinfoinput():
    while True:
        userinput = input(
        '\nВведите команду:\n\
        p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;\n\
        s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;\n\
        l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";\n\
        a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,\n\
        имя владельца и номер полки, на котором он будет храниться;\n\
        d - delete - команда спросит номер документа и удалит его из списка документов и из полки;\n\
        m - move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;\n\
        as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень\n\
        pf - person find - команда, которая выводит список всех владельцев документов\n\
        dc - document check - команда, которая проверяет есть ли разница по содержанию\n\
        между номерами документов в documents и directories и, если есть выводит информацию о разнице\n'
                          )

        if userinput == 'p':
            docpeople()

        elif userinput == 's':
            docshelf()

        elif userinput == 'l':
            doclist()

        elif userinput == 'a':
            docadd()

        elif userinput == 'd':
            docdel()

        elif userinput == 'm':
            docmove()

        elif userinput == 'as':
            addshelf()

        elif userinput == 'pf':
            personfind()

        elif userinput == 'dc':
            doccheck()


docinfoinput()
