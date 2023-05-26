import threading as th
import time

class Logger:
    """
        Класс предназначен для параллельного вывода сообщений из кода куда-либо
        Посредник вывода представляет собой функцию, принимаю на вход аргументы (как, например, print)
        Логгер позволяет без конфликтов выводить данные из нескольких потоков
    """
    def __init__(self, isPrint=False, LoggerFunc=print, **kwargs):
        "Инизиализация логгера"
        self.kwargs = kwargs
        self.LoggerFunc = LoggerFunc
        self.isPrint = isPrint
        self.OutList = []

        self.__startThread()



    def __startThread(self):
        "Создание потока логгера"
        if self.isPrint:
            t = th.Thread(target=self.__out)
            t.start()



    def output(self):
        "Вывод всех сообщений в логгере"
        while self.OutList:
            self.LoggerFunc(self.OutList.pop(0))



    def log(self):
        "Вывод из логлиста без очистки"
        for event in self.OutList:
            self.LoggerFunc(event, **self.kwargs)



    def clear(self):
        "Очистка логлиста"
        self.OutList = []



    def __call__(self, *message):
        self.append(*message)
    def append(self, *message):
        "Добавление нового сообщения в логгер"
        if type(message) in (tuple, list):
            for nEvent in message:
                self.OutList.append(time.ctime()[11:19] + " >> " + nEvent + "\n")
        else:
            self.OutList.append(time.ctime()[11:19] + " >> " + message + "\n")
        return

    

    def __out(self):
        "Цикл вывода из логгера. Вывод осуществляется при поступлении сообщения"
        while self.isPrint:
            if len(self.OutList):
                self.LoggerFunc(self.OutList.pop(0), **self.kwargs)



    def __str__(self):
        return str(self.OutList)
        


    def start(self):
        "Запуск главного цикла логгера"
        self.isPrint = True
        self.__startThread()



    def close(self, isLogEvents=True):
        "Закрытие логгера с опциональным выводом"
        self.isPrint = False
        if len(self.OutList) and isLogEvents:
            self.output()



    def mute(self):
        "Запрещает печать событий из логлиста"
        self.isPrint = False





if __name__ == "__main__":
    log = Logger(True, print, end="")
    for _ in range(10):
        log(123)