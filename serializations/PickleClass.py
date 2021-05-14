
a ="""{
  "AllData": {"ArchiveAndDearchieveConfiguration": {
      "Archieve": true,
      "DeArchieve": true
    },
    "FinderInfo": {
      "Coding": "utf8",
      "SourceDirectory": "/Users/victoriasviridchik/Desktop/lab2/SourceDir",
      "TargetDirectory": "/Users/victoriasviridchik/Desktop/lab2/TargetDir/",
      "LogPath": "/Users/victoriasviridchik/Desktop/zoo/templog.txt",
      "NeedToLog": true
    },
    "CompressingOptions": {
      "Compressing": false
    },
    "EncryptingAndDecriptingOptions": {
      "RandomKey": true,
      "Encrypt": false,
      "DEncrypt": false
    },

    "DataOptions": {
      "Server": "localhost\\SQLEXPRESS",
      "Database": "master",
      "Trusted_Connection": true
    }
  }
}"""
# import re as r
# pattern = '""(\w*[^""{}])"": {([^}]*)} ?'
# res = r.match(pattern,a)
# for r in res:
#     print(rim
import pickle
from services import SerBase

from services.ordinary_types import *


class PickleClassMy(SerBase.SerBaseClass):
    def dump(self, obj, fp):
        """сериализует Python объект в файл"""
        prep_obj = prepare_data(obj)
        with open(fp, 'wb') as fp_prep:
            return pickle.dump(prep_obj, fp_prep)


    def dumps(self, obj):
        """сериализует Python объект в строку"""
        prep_obj = prepare_data(obj)
        return pickle.dumps(prep_obj)

    def load(self, fp):
        """десериализует Python объект из файла"""
        with open(fp, 'rb') as fp_prep:
            prep_obj = de_prepare_data(pickle.load(fp_prep))
            return prep_obj


    def loads(self, s):
        """десериализует Python объект из строки"""
        prep_obj = de_prepare_data(pickle.loads(s))
        return prep_obj