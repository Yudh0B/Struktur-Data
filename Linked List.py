class Node:
    def __init__(self,data):
        self.item = data
        self.nref = None
        self.pref = None
class linkedList:
    def __init__(self):
        self.nodeS = None
        
    def insert_awal(self,data):
        if self.nodes is None:
            nodeN = Node(data)
            self.nodeS = nodeN
            print("Nilai anda sudah masuk")
        else :
            print("listnya tidak kosong")
            
#prog utama
list_baru = linkedList()
list_baru.insert_awal(50)
