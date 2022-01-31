class Pair:
    def __init__(self,key) -> None:
        self.key = key
        self.value = 1

class Dict:
    def __init__(self) -> None:
        self.pair_list = []
    
    def add(self,key):
        if len(self.pair_list) == 0:
            obj = Pair(key)
            self.pair_list.append(obj)

        elif(self.alredy_have_key(key)):
            self.update_value(key,self.get_value(key)+1)
        
    def update_value(self,key,value):
        for i in range(len(self.pair_list)):
            if self.pair_list[i].key == key:
                self.pair_list[i].value = value

    
    def alredy_have_key(self,key):
        for i in range(len(self.pair_list)):
            obj = self.pair_list[i]
            if obj.key == key:
                return True
        return False
    
    def get_value(self,key):
        for i in range(len(self.pair_list)):
            obj = self.pair_list[i]
            if obj.key == key:
                return obj.value
        return 0
    
    def show_dict(self):
        for i in range(len(self.pair_list)):
            obj = self.pair_list[i]
            print("({},{})".format(obj.key,obj.value))
        return


obj = Dict()
obj.add(1)
obj.add(1)
obj.add(1)

obj.show_dict()
        
