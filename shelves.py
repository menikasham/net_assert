class Shelves:
    def __init__(self):
        self.documents = []
        self.directories = {}

    def get_name(self, doc_number):
        for document in self.documents:
            if document['number'] == doc_number:
                return document['name']
        return "Документ не найден"

    def make_dir(self, number, *args):
        self.directories[number] = [*args]

    def get_directory(self, doc_number):
        for number, docs in self.directories.items():
            if doc_number in docs:
                return number
        return "Полки с таким документом не найдено"

    def add(self, document_type, number, name, shelf_number):
        new_doc = {"type": document_type, "number": number, "name": name}
        self.documents.append(new_doc)
        if shelf_number in self.directories:
            self.directories[shelf_number].append(number)
        else:
            self.directories[shelf_number] = [number]

    def get_all_notes(self):
        return self.documents



if __name__ == '__main__':
    shelves = Shelves()
    shelves.make_dir('1', '2207 876234', '11-2', '5455 028765')
    shelves.make_dir('2', '10006')
    shelves.make_dir('3', '')
    print(shelves.get_name("10006"))
    print(shelves.get_directory("11-2"))
    print(shelves.get_name("101"))
    shelves.add('international passport', '311 020203', 'Александр Пушкин', 4)
    print(shelves.get_directory("311 020203"))
    print(shelves.get_name("311 020203"))
    print(shelves.get_directory("311 020204"))
    print(shelves.get_all_notes())
