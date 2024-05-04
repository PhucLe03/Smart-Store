import pickle
import ast
import json
# sql query fetchone and label, return a dictionary
def fetchone_then_label(result, description):
    final_res = {}
    for i, col in enumerate(description):
        # print('col', col[0])
        final_res[col[0]] = result[i]
    return final_res


# sql query fetchone and label, return a list of dictionaries
def fetchall_then_label(results, description):
    final_res = []
    for result in results:
        sub_res = fetchone_then_label(result, description)
        final_res.append(sub_res)
    return final_res


# Convert images or files data to binary format
def convert_data(file_name):
    with open(file_name, 'rb') as file:
        binary_data = file.read()
    return binary_data


# Convert `bytearray string` (get from sql query) to `bytearray`
# def convert_bytearray(string):
#     return b"x00"
#     byte_string = string[2:-1]
#     # print('byte', byte_string)
#     # byte_string = ''.join(e for e in byte_string if e != '\x5c')
#     # print('temp', bytes(temp))
    
#     print(byte_string)
#     deserialize_obj = pickle.loads((str(byte_string).encode('latin1')))
#     byte_obj = bytes(deserialize_obj)
#     return byte_obj
#     return bytearray(byte_obj)
import numpy
from json import JSONEncoder
class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)
def ndarray_to_json(array):
    data = {"array" : array}
    return json.dumps(data, cls=NumpyArrayEncoder)
