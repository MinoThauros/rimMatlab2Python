import pandas as pd
new_data = pd.read_csv("data/AuMn25nm2Output30V.csv")
#print(new_data.head())

class Data:
    """fetches all the csv files
    """
    def data2Output30V(self):
        new_data = pd.read_csv("data/AuMn25nm2Output30V.csv")
        new_data.columns=['Ids','Vds']
        #print(newdatatrue)
        return new_data
    def data2Output45V(self):
        new_data = pd.read_csv("data/AuMn25nm2Output45V.csv")
        new_data.columns=['Ids','Vds']
        #print(newdatatrue)
        return new_data
    def data2output60v(self):
        new_data = pd.read_csv("data/AuMn25nm2Output60V.csv")
        new_data.columns=['Ids','Vds']
        #print(newdatatrue)
        return new_data
    def data2Transfer3VF(self):
        new_data = pd.read_csv("data/AuMn25nm2Transfer3VF.csv")
        new_data.columns=['Ids','Vds']
        #print(newdatatrue)
        return new_data
    def data2Transfer50VF(self):
        new_data = pd.read_csv("data/AuMn25nm2Transfer50VF.csv")
        new_data.columns=['Ids','Vds']
        #print(newdatatrue)
        return new_data
    
data=Data()

