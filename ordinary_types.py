import types
import json
import inspect

def prepare_data(raw_data):
    simplicies = [list,tuple,set]
    atom = [str, int, float, bool,type(None)]
    etalon = type(raw_data)
    if etalon in simplicies:
        res = []
        for el in raw_data:
            res.append(prepare_data(el))
        return res
    elif  etalon in atom:
        return raw_data
    elif etalon == types.FunctionType:
        tmp_data = inspect.getmembers(raw_data)
        my_code  = raw_data.__code__.co_names
        my_globals = raw_data.__globals__
        my_globals_res = {}
        for k in my_code.keys():
            if k in my_code and inspect.isbuiltin(my_globals[k]) is False:
                my_globals_res[k]=my_globals[k]



        # my_globals = set(my_code).intersection(set(my_globals))
        my_name = raw_data.__name__
        my_argdefs = raw_data.__defaults__
        my_closure = raw_data.__closure__

        types.CodeType()
        types.FunctionType()
    elif etalon == dict:
        res = {}
        for k,v in raw_data.items():
            kk = prepare_data(k)
            vv  = prepare_data(k)
            res[kk]=vv
        return res
    else:
        tmp_data = inspect.getmembers(raw_data)
        res = {}
        for el in tmp_data:
            kk = prepare_data(el[0])
            vv = prepare_data(el[1])
            res[kk] = vv
        return res


def p(c):
    return "the res is {}".format(c)

def summ(a=9,b=1):
    return p(a+b)

prepare_data(summ)