import xlrd
import pandas as pd
def Z_Score(data):
    lenth = len(data)
    total = sum(data)
    ave = float(total)/lenth
    tempsum = sum([pow(data[i] - ave,2) for i in range(lenth)])
    tempsum = pow(float(tempsum)/lenth,0.5)
    for i in range(lenth):
        data[i] = (data[i] - ave)/tempsum
    return data

def anti_array(data):
    for value in data:
        new_value = - value
        data[i] = new_value
    return data

def read_excel(file):
    ExcelFile = xlrd.open_workbook(file)
    sheet = ExcelFile.sheet_by_index(0)
    names = sheet.col_values(1)[1:]
    cols1 = sheet.col_values(2)[1:]
    cols1 = anti_array(cols1)

    print cols1
    #print sheet.col_values(4)ss
    cols2 = sheet.col_values(3)[1:]
    print cols2

    Z_P = Z_Score(cols1)
    Z_KL = Z_Score(cols2)
    return  names,Z_P,Z_KL

def save_as_excel(value1,value2,value3):
    s0 = pd.Series(value1)
    s1 = pd.Series(value2)
    s2 = pd.Series(value3)
    df = pd.DataFrame({"Amino Acid name":s0,'pearson coefficient':s1,'KL':s2})
    cols = ["Amino Acid name",'pearson coefficient', "KL"]
    df = df.ix[:,cols]
    #del_file(path)
    writer = pd.ExcelWriter('/Users/xg666/Desktop/looppredict/DataAndResult/P-KL_ZScore.xlsx')
    #writer = pd.ExcelWriter('/Users/xg666/Desktop/xqdongV2/project/media/result/result.xlsx')
    df.to_excel(writer, sheet_name = 'Z-score')
    writer.save()
if __name__ == "__main__":
    file = '/Users/xg666/Desktop/looppredict/DataAndResult/P2.xlsx'
    value1,value2,value3 = read_excel(file)
    save_as_excel(value1,value2,value3)

