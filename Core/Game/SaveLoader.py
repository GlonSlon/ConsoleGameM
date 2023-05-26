import pickle
import os

class SaveLoader:
    """
        Данный класс предназначен для сохранения данных файл, а так же выгрузки данных из файла
        Класс предусматривает вывод через логгер, без логгера вывод будет работать в режиме print`a
    """

    def __init__(self, directory=None, fileFormat="txt", LocalLogger = None):
        "Конструктор класса"
        self.file_does_not_exist_msg = "file_does_not_exist_msg"
        self.creating_saveloader_msg = "Starting SaveLoader"
        self.succsesful_create_msg = "succsesful_create_msg"
        self.succsecful_save_msg = "succsecful_save_msg"
        self.succsecful_load_msg = "succsecful_load_msg"
        self.wrong_directory_msg = "wrong_directory_msg"
        self.broken_file_msg = "broken_file_msg"
        self.no_save_obj_msg = "no_save_obj_msg"
        
        if LocalLogger:
            self.LocalLogger = LocalLogger
            try:
                self.LocalLogger(self.creating_saveloader_msg)
            except:
                while True:
                    print("Create a logger, fucking bastard!")


        if not directory:
            self.LocalLogger(self.wrong_directory_msg)
            return None
        self.directory = directory
        
        if fileFormat[0] == ".":
            self.fileFormat = fileFormat
        else:
            self.fileFormat = "." + fileFormat

        lastLoadedData = None
        inWorkSave = None



    def Load(self, SaveName):
        "Функция загрузки из файла"
        
        self.inWorkSave = SaveName
        file = self.directory + "\\" + SaveName + self.fileFormat
        try:
            localOpenedFile = open(file, "rb")
        except:
            self.LocalLogger(self.file_does_not_exist_msg)
            return
        try:
            LoadedData = pickle.load(localOpenedFile)
            localOpenedFile.close()
            self.LocalLogger(self.succsecful_load_msg)
        except:
            self.LocalLogger(self.broken_file_msg)
            return
        return LoadedData



    def Save(self, SaveFile, DataToSave):
        "Функция сохранения данных в файл"
        
        file = self.directory + "\\" + SaveFile + self.fileFormat
        localOpenedFile = open(file, "wb")            
        try:
            pickle.dump(DataToSave, localOpenedFile)
        except:
            self.LocalLogger(self.no_save_obj_msg)
            return
        localOpenedFile.close()
        self.LocalLogger(self.succsecful_save_msg)



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
    










        
