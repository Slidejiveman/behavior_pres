class Drive(object):
    CHECK_STATUS = 'check status'
    INSERT = 'insert'
    EJECT = 'eject'

    __status = 'ejected'

    def command(self, command):
        if command == self.CHECK_STATUS:
            return self.__status
        elif command == self.INSERT:
            self.__status = 'inserted'
            return self.__status
        elif command == self.EJECT:
            self.__status = 'ejected'
            return self.__status
        else:
            return 'Unrecognized Command'


if __name__ == '__main__':
    drive = Drive()
    while True:
        print(drive.command(input('Enter command: ')))
