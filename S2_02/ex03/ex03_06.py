#input: dictionary , key
#output: dictionanry khong co tu khoa key

def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else: 
        return False
    
my_dic = {'a': 1, 'b': 2, 'c': 2, 'd' : 7}
key_to_delecte = 'b'
result = xoa_phan_tu(my_dic, key_to_delecte)
if(result):
    print("phan tu da duoc xoa tu dictionary: ", my_dic)
else:
    print("khong tim thay phan tu de xoa trong dictionary")