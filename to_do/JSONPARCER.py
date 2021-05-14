
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
from services.ordinary_types import *
from services import SerBase


class Json(SerBase):
    def dump(self, obj, fp):
        """сериализует Python объект в файл"""
        prep_obj = prepare_data(obj)
        return json.dump(prep_obj,fp)

    def dumps(self, obj):
        """сериализует Python объект в строку"""
        prep_obj = prepare_data(obj)
        return json.dumps(prep_obj)

    def load(self, fp):
        """десериализует Python объект из файла"""
        prep_obj = prepare_data(fp)
        return json.load(prep_obj)

    def loads(self, s):
        """десериализует Python объект из строки"""
        prep_obj = prepare_data(s)
        return json.load(prep_obj)