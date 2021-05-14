
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


class JsonClassMy(SerBase.SerBaseClass):
    def dump(self, obj, fp):
        """сериализует Python объект в файл"""
        prep_obj = prepare_data(obj)
        with open(fp, 'w') as fp_prep:
            return json.dump(prep_obj,fp_prep)

    def dumps(self, obj):
        """сериализует Python объект в строку"""
        prep_obj = prepare_data(obj)
        return json.dumps(prep_obj)

    def load(self, fp):
        """десериализует Python объект из файла"""
        # fp_prep = open(fp, 'w')
        with open(fp, 'r') as fp_prep:
            prep_obj = de_prepare_data(json.load(fp_prep))
            return prep_obj

    def loads(self, s):
        """десериализует Python объект из строки"""
        prep_obj = de_prepare_data(json.loads(s))
        return prep_obj