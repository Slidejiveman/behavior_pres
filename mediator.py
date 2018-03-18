import asyncio
import time


class ProcessProcessor(object):
    __queue = []

    def process(self):
        if len(self.__queue) == 0:
            return
        else:
            process: ProcessInterface = self.__queue.pop(0)
            process.run()

    def print(self, text):
        self.__queue.append(PrintProcess(text))

    def empty_queue(self):
        return len(self.__queue) == 0


class ProcessInterface(object):
    def run(self):
        pass


class PrintProcess(ProcessInterface):
    value = None

    def __init__(self, val):
        self.value = val

    def run(self):
        print(self.value)


if __name__ == '__main__':
    processor = ProcessProcessor()
    await_array = []

    for i in range(1, 15):
        processor.print('I am print process {}'.format(i))
        if i % 3 == 0:
            processor.process()

    while not processor.empty_queue():
        processor.process()
