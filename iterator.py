class IteratorInterface(object):
    position = 0

    def first(self) -> object:
        pass

    def next(self) -> object:
        pass

    def last(self) -> object:
        pass

    def as_list(self) -> object:
        pass

    def has_next(self) -> bool:
        pass

    def reset_to_first(self) -> None:
        self.position = 0


class ListIterator(IteratorInterface):
    __list = None

    def __init__(self, the_list):
        self.__list = the_list

    def first(self) -> object:
        if len(self.__list) > 0:
            return self.__list[0]
        else:
            return None

    def next(self) -> object:
        if self.position < len(self.__list):
            val = self.__list[self.position]
            self.position += 1
            return val
        else:
            return None

    def last(self) -> object:
        if len(self.__list) > 0:
            return self.__list[len(self.__list)]

    def as_list(self) -> list:
        return self.__list

    def has_next(self) -> bool:
        if self.position < len(self.__list):
            return True
        else:
            return False


class TupleIterator(IteratorInterface):
    __tuple = None

    def __init__(self, the_tuple):
        self.__tuple = the_tuple

    def first(self):
        return self.__tuple[0]

    def next(self) -> object:
        if self.position < len(self.__tuple):
            val = self.__tuple[self.position]
            self.position += 1
            return val
        else:
            return None

    def last(self) -> object:
        if len(self.__tuple) > 0:
            return self.__tuple[len(self.__tuple)]

    def as_list(self) -> list:
        return list(self.__tuple)

    def has_next(self) -> bool:
        if self.position < len(self.__tuple):
            return True
        else:
            return False


class MyList(object):
    __my_list = []

    def add(self, value):
        self.__my_list.append(value)

    def get_iterator(self):
        return ListIterator(self.__my_list)

    def remove(self, position):
        return self.__my_list.pop(position)


def print_iterator(my_iterator):
    while my_iterator.has_next():
        print(my_iterator.next())

    print(my_iterator.as_list())


if __name__ == '__main__':
    my_list = MyList()

    for i in range(1, 10):
        my_list.add(i)

    my_list_iterator = my_list.get_iterator()

    my_tuple_itertor = TupleIterator(('a', 'b', 'c', 'd', 'e', 'f'))

    print_iterator(my_list_iterator)

    print_iterator(my_tuple_itertor)
