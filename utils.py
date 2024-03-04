LOGGING=False

def log(*args):
    if LOGGING==True:
        print(args)

def flatten_list(array, dict_keyvalue="KeyValue"):
    flat_list = []
    if type(array) in (list, tuple, dict):
        for el in array:
            if type(el)==dict:
                pass
            if type(el) in (list, tuple, dict):
                flat_list = flat_list + flatten_list(el)
            elif type(array)==dict:
                if dict_keyvalue.upper()=="KEY":
                    flat_list.append(el)
                elif dict_keyvalue.upper()=="VALUE":
                    flat_list.append(array[el])
                else:
                    flat_list.append(el)
                    flat_list.append(array[el])
            else:
                flat_list.append(el)
    else:
        flat_list.append(array)

    return flat_list

def list_to_string(list, separator="\n"):
    datavalue = ""
    for info in list:
        if info==None:
            datavalue += separator
        else:
            datavalue += str(info) + separator
    return datavalue

if __name__ == '__main__':
    import unittest
    class TestSum(unittest.TestCase):
        def test_flatten_list(self):
            self.assertEqual(flatten_list([1, 2, 3]), [1, 2, 3], "Should be [1, 2, 3]")
        def test_flatten_tuple(self):
            self.assertEqual(flatten_list((4, 5, 6)), [4, 5, 6], "Should be [4, 5, 6]")
        def test_flatten_dict(self):
            self.assertEqual(flatten_list({"One":1, 2:"Two", 3:3, "Four":'Four'}), ["One", 1, 2, "Two", 3 , 3, "Four", 'Four'], "Should be ['One', 1, 2, 'Two', 3, 3, 'Four', 'Four']")
        def test_flatten_dictoneelement(self):
            self.assertEqual(flatten_list({"OneHunderdOne":'101'}, dict_keyvalue="Both"), ['OneHunderdOne', '101'], "Should be ['OneHunderdOne', '101']")
        def test_flatten_dictkey(self):
            self.assertEqual(flatten_list({"One":1, 2:"Two", 3:3, "Four":'Four'}, "key"), ["One", 2, 3, "Four"], "Should be ['One', 2, 3, 'Four']")
        def test_flatten_dictvalue(self):
            self.assertEqual(flatten_list({"One":1, 2:"Two", 3:3, "Four":'Four'}, "Value"), [1, 'Two', 3, 'Four'], "Should be [1, 'Two', 3, 'Four']")
        def test_flatten_String(self):
            self.assertEqual(flatten_list("TestAString"), ["""TestAString"""], "Should be [1, 'Two', 3, 'Four']")
        def test_flatten_Number(self):
            self.assertEqual(flatten_list(123), [123], "Should be [123]")
        def test_flatten_Complex(self):
            complex_array = ("Anweisung1", ("Anweisung1","butterfly_transparent.png","Eine erste Anweisung","2023-05-12 10:30:34",None,
                             (1,"eine erste Schritt der ersten Anweisung",None,
                             (1,"DIE ANWEISUNG 1"))))

            self.assertEqual(flatten_list(complex_array), ['Anweisung1','Anweisung1','butterfly_transparent.png',
                                                           'Eine erste Anweisung','2023-05-12 10:30:34',None,1,
                                                           'eine erste Schritt der ersten Anweisung',None,1,'DIE ANWEISUNG 1'],
                                                           "Should be [...]")
        def test_list_to_string(self):
            self.assertEqual(list_to_string([1,2,3]), "1\n2\n3\n", """Should be '1
2
3
'""")

    unittest.main()
