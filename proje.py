"""
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]

"""




input = [[1,'a',['cat'],2],[[[3]],'dog'],4,5,[[3,"böcek"]]]
new_input = []

def list_division(self):
    for i in self:
        # print(i)
        if type(i) == list:
            for e in i:
                # print(e)
                if type(e) == list:
                    list_division(e)
                else:
                    new_input.append(e)
        else:
            new_input.append(i)
    return

list_division(input)
print(new_input)
    

# # list_division(input[0])
# # print(new_input)
# print(new_input)

#######################################################################################################
"""
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]

# """

input = [[1, 2], [3, 4], [5, 6, 7],3,5,[2,2,3]]


def turn(self):
    turner = []
    for i in self:
        if type(i) == list:
            i = i[::-1]
            turner.append(i)
        else:
            turner.append(i)
        self = turner        
        self = self[::-1]
    print(self)

turn(input)