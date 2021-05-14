import os
import unittest
from serializations.JsonClass import *
from services.fabric import *
def p(c):
    return "the res is {}".format(c)

def summ(a=9,b=1):
    return p(a+b)

data_etalon = {'__closure__': None,
 '__code__': {'co_argcount': 2,
              'co_cellvars': [],
              'co_code': [116, 0, 124, 0, 124, 1, 23, 0, 131, 1, 83, 0],
              'co_consts': [None],
              'co_filename': '/Users/victoriasviridchik/PycharmProjects/isp_4sem_2/tests.py',
              'co_firstlineno': 7,
              'co_flags': 67,
              'co_freevars': [],
              'co_kwonlyargcount': 0,
              'co_lnotab': [0, 1],
              'co_name': 'summ',
              'co_names': ['p'],
              'co_nlocals': 2,
              'co_posonlyargcount': 0,
              'co_stacksize': 3,
              'co_varnames': ['a', 'b']},
 '__defaults__': (9, 1),
 '__globals__': {'p': {'__closure__': None,
                       '__code__': {'co_argcount': 1,
                                    'co_cellvars': [],
                                    'co_code': [100,
                                                1,
                                                160,
                                                0,
                                                124,
                                                0,
                                                161,
                                                1,
                                                83,
                                                0],
                                    'co_consts': [None, 'the res is {}'],
                                    'co_filename': '/Users/victoriasviridchik/PycharmProjects/isp_4sem_2/tests.py',
                                    'co_firstlineno': 4,
                                    'co_flags': 67,
                                    'co_freevars': [],
                                    'co_kwonlyargcount': 0,
                                    'co_lnotab': [0, 1],
                                    'co_name': 'p',
                                    'co_names': ['format'],
                                    'co_nlocals': 1,
                                    'co_posonlyargcount': 0,
                                    'co_stacksize': 3,
                                    'co_varnames': ['c']},
                       '__defaults__': None,
                       '__globals__': {},
                       '__name__': 'p'}},
 '__name__': 'summ'}

class TestSer(unittest.TestCase):
    def test_atom(self):
        a_int = prepare_data(9)
        a_float = prepare_data(3.14)
        self.assertEqual(a_int,9)
        self.assertEqual(a_float,3.14)

    def test_simplices(self):
        list_data = [1,2,3]
        a_list = prepare_data(list_data)
        dict_data =  {'data': [{'vbh': bytes([6, 9, 123]), 'y':('x', 5),'o': {8, 'z'}}]}
        a_dict = prepare_data(dict_data)
        a_exp = {'data': [{'o': [8, 'z'], 'vbh': [6, 9, 123], 'y': ['x', 5]}]}
        self.assertEqual(a_list,list_data)
        self.assertEqual(a_dict,a_exp)

    def test_func(self):
        a_func = prepare_data(summ)
        self.assertEqual(de_prepare_data(a_func)(2), "the res is 3")
        # self.assertEqual(a_dict, a_exp)

    def test_dumps_loads(self):
        data = { "I am tired HELP":["very"]}
        a_dict = prepare_data(data)
        a_expp_json = { "I am tired HELP":["very"]}
        # a_expp_pickle =bytes("I am tired HELP")
        # print(a_expp)
        res = fabrica('json').dumps(a_dict)
        res_pickle = fabrica('pickle').dumps(a_dict)
        res_toml = fabrica('toml').dumps(a_dict)
        res_yaml = fabrica('yaml').dumps(a_dict)
        # print(a_expp)
        # print(res)
        # self.assertEqual(res,a_expp_json)

        self.assertEqual(fabrica('json').loads(res), data)
        self.assertEqual(fabrica('pickle').loads(res_pickle),data )
        self.assertEqual(fabrica('toml').loads(res_toml), data)
        self.assertEqual(fabrica('yaml').loads(res_yaml), data)

    def test_dump_load(self):
        data = { "I am tired HELP":["very"]}
        a_dict = prepare_data(data)
        with open('data_json', 'w'):
            fabrica('json').dump(a_dict, 'data_json')
            self.assertEqual(fabrica('json').load('data_json'), data)
        with open('data_toml', 'w'):
            fabrica('toml').dump(a_dict, 'data_toml')
            self.assertEqual(fabrica('toml').load('data_toml'), data)
        with open('data_yaml', 'w'):
            fabrica('yaml').dump(a_dict, 'data_yaml')
            self.assertEqual(fabrica('yaml').load('data_yaml'), data)
        with open('pickle_data', 'wb'):
            fabrica('pickle').dump(a_dict, 'pickle_data')
            self.assertEqual(fabrica('pickle').load('pickle_data'), data)
        os.remove('data_json')
        os.remove('data_toml')
        os.remove('data_yaml')
        os.remove('pickle_data')
        # res_pickle = fabrica('pickle').dumps(a_dict)
        # res_toml = fabrica('toml').dumps(a_dict)
        # res_yaml = fabrica('yaml').dumps(a_dict)
        #
        # self.assertEqual(fabrica('pickle').loads(res_pickle),data )
        # self.assertEqual(fabrica('toml').loads(res_toml), data)
        # self.assertEqual(fabrica('yaml').loads(res_yaml), data)


class TestDeSer(unittest.TestCase):
    def test_atom(self):
        a_int = de_prepare_data(prepare_data(9))
        a_float = de_prepare_data(prepare_data(3.14))
        self.assertEqual(a_int, 9)
        self.assertEqual(a_float, 3.14)

    def test_simplices(self):
        list_data = [1,2,3]
        a_list = de_prepare_data(prepare_data(list_data))
        dict_data =  {'data': [{'vbh': bytes([6, 9, 123]), 'y':('x', 5),'o': {8, 'z'}}]}
        a_dict = de_prepare_data(prepare_data(dict_data))
        a_exp = {'data': [{'o': [8, 'z'], 'vbh': [6, 9, 123], 'y': ['x', 5]}]}
        self.assertEqual(a_list,list_data)
        self.assertEqual(a_dict,a_exp)

    def test_func(self):
        a_func = de_prepare_data(prepare_data(summ))
        self.assertEqual(a_func(3), "the res is 4")
        # self.assertEqual(a_dict, a_exp)
#
# class TestDeSer(unittest.TestCase):
#     def test_magic(self):
