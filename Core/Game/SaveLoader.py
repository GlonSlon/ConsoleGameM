from Core.Game.Logger import Logger

import pickle
import os

class SaveLoader:
    """
        Данный класс предназначен для сохранения данных файл, а так же выгрузки данных из файла
        Класс предусматривает вывод через логгер, без логгера вывод будет работать в режиме print`a
    """

    def __init__(self, directory=None, fileFormat="txt", isLog=False, LoggerFunc=print):
        "Конструктор класса"
        self.fileDoesNotExistMsg = "fileDoesNotExistMsg"
        self.succsesfulCreateMsg = "SuccsesfulCreateMsg"
        self.succsecfulSaveMsg = "succsecfulSaveMsg"
        self.succsecfulLoadMsg = "succsecfulLoadMsg"
        self.wrongDirectoryMsg = "wrongDirectoryMsg"
        self.brokenFileMsg = "brokenFileMsg"
        self.noSaveObjMsg = "NoSaveObjMsg"
        
        if isLog:
            try:
                self.LocalLogger = Logger(True, LoggerFunc)
            except:
                self.LocalLogger = print

        if not directory:
            self.LocalLogger(self.wrongDirectoryMsg)
            return None
        self.directory = directory
        
        if fileFormat[0] == ".":
            self.fileFormat = fileFormat
        else:
            self.fileFormat = "." + fileFormat

        self.isLog = isLog
        lastLoadedData = None
        inWorkSave = None



    def Load(self, SaveName):
        "Функция загрузки из файла"
        
        self.inWorkSave = SaveName
        file = self.directory + "\\" + SaveName + self.fileFormat
        try:
            localOpenedFile = open(file, "rb")
        except:
            if self.isLog:
                self.LocalLogger(self.fileDoesNotExistMsg)
                return
        try:
            LoadedData = pickle.load(localOpenedFile)
            localOpenedFile.close()
            if self.isLog:
                self.LocalLogger(self.succsecfulLoadMsg)
        except:
            if self.isLog:
                self.LocalLogger(self.brokenFileMsg)
                return
        return LoadedData



    def Save(self, SaveFile, DataToSave):
        "Функция сохранения данных в файл"
        
        file = self.directory + "\\" + SaveFile + self.fileFormat
        localOpenedFile = open(file, "wb")            
        try:
            pickle.dump(DataToSave, localOpenedFile)
        except:
            if self.isLog:
                self.LocalLogger(self.noSaveObjMsg)
        localOpenedFile.close()
        if self.isLog:
            self.LocalLogger(self.succsecfulSaveMsg)



    # Функция поиска
    def searchingSaves(self):
        "Функция возвращает отсортированный список файлов в папке сейв-лодера"
        
        RawSavesList = os.listdir(self.directory)
        SavesList = []
        for i in RawSavesList:
            if i[(len(i)-len(self.fileFormat)):] == self.fileFormat:
                SavesList.append(i)
        FormatedSavesList = []
        for i in SavesList:
            FormatedSavesList.append(i[:-5])
        return FormatedSavesList


if __name__ == "__main__":
    pass
    










        
