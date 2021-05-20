import inspect
import re
from pydoc import locate
from types import CodeType, FunctionType

FUNCTION_ATTRIBUTES = [
        "__code__",
        "__name__",
        "__defaults__",
        "__closure__"
    ]

CODE_OBJECT_ARGS = [
        'co_argcount',
        'co_posonlyargcount',
        'co_kwonlyargcount',
        'co_nlocals',
        'co_stacksize',
        'co_flags',
        'co_code',
        'co_consts',
        'co_names',
        'co_varnames',
        'co_filename',
        'co_name',
        'co_firstlineno',
        'co_lnotab',
        'co_freevars',
        'co_cellvars'
    ]


def serialize_object(obj: object):
    ans = {}
    object_type = type(obj)
    if object_type == list:
        ans["type"] = "list"
        ans["value"] = tuple([serialize_object(i) for i in obj])
    elif object_type == dict:
        ans["type"] = "dict"
        ans["value"] = {}

        for i in obj:
            key = serialize_object(i)
            value = serialize_object(obj[i])
            ans["value"][key] = value
        ans["value"] = tuple((k, ans["value"][k]) for k in ans["value"])
    elif object_type == tuple:
        ans["type"] = "tuple"
        ans["value"] = tuple([serialize_object(i) for i in obj])
    elif object_type == bytes:
        ans["type"] = "bytes"
        ans["value"] = tuple([serialize_object(i) for i in obj])
    elif obj is None:
        ans["type"] = "NoneType"
        ans["value"] = None
    elif inspect.isroutine(obj):
        ans["type"] = "function"
        ans["value"] = {}
        members = inspect.getmembers(obj)
        members = [i for i in members if i[0] in [
            "__code__",
            "__name__",
            "__defaults__",
            "__closure__"
        ]]
        for i in members:
            key = serialize_object(i[0])
            value = serialize_object(i[1])
            ans["value"][key] = value
            if i[0] == "__code__":
                key = serialize_object("__globals__")
                ans["value"][key] = {}
                names = i[1].__getattribute__("co_names")
                glob = obj.__getattribute__("__globals__")
                globdict = {}
                for name in names:
                    if name == obj.__name__:
                        globdict[name] = obj.__name__
                    elif name in glob and not inspect.ismodule(name) and name not in __builtins__:
                        globdict[name] = glob[name]
                ans["value"][key] = serialize_object(globdict)
        ans["value"] = tuple((k, ans["value"][k]) for k in ans["value"])

    elif isinstance(obj, (int, float, complex, bool, str)):
        typestr = re.search(r"\'(\w+)\'", str(object_type)).group(1)
        ans["type"] = typestr
        ans["value"] = obj
    else:
        ans["type"] = "instance"
        ans["value"] = {}
        members = inspect.getmembers(obj)
        members = [i for i in members if not callable(i[1])]
        for i in members:
            key = serialize_object(i[0])
            val = serialize_object(i[1])
            ans["value"][key] = val
        ans["value"] = tuple((k, ans["value"][k]) for k in ans["value"])

    ans = tuple((k, ans[k]) for k in ans)
    return ans


def deserialize_object(obj):
    obj = dict((a, b) for a, b in obj)
    object_type = obj["type"]
    result = None
    if object_type == "NoneType":
        result = None
    elif object_type == "bytes":
        result = bytes([deserialize_object(i) for i in obj["value"]])
    elif object_type == "list":
        result = [deserialize_object(i) for i in obj["value"]]
    elif object_type == "tuple":
        result = tuple([deserialize_object(i) for i in obj["value"]])
    elif object_type == "dict":
        result = {}
        for i in obj["value"]:
            val = deserialize_object(i[1])
            result[deserialize_object(i[0])] = val
    elif object_type == "function":
        func = [0] * 4
        code = [0] * 16
        glob = {"__builtins__": __builtins__}
        for i in obj["value"]:
            key = deserialize_object(i[0])

            if key == "__globals__":
                globdict = deserialize_object(i[1])
                for globkey in globdict:
                    glob[globkey] = globdict[globkey]
            elif key == "__code__":
                val = i[1][1][1]
                for arg in val:
                    codeArgKey = deserialize_object(arg[0])
                    if codeArgKey != "__doc__":
                        codeArgVal = deserialize_object(arg[1])
                        index = CODE_OBJECT_ARGS.index(codeArgKey)
                        code[index] = codeArgVal

                code = CodeType(*code)
            else:
                index = FUNCTION_ATTRIBUTES.index(key)
                func[index] = (deserialize_object(i[1]))

        func[0] = code
        func.insert(1, glob)

        result = FunctionType(*func)
        if result.__name__ in result.__getattribute__("__globals__"):
            result.__getattribute__("__globals__")[result.__name__] = result
    else:
        if object_type == "bool":
            result = obj["value"] == "True"
        else:
            result = locate(object_type)(obj["value"])

    return result
