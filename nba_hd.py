# -*- coding: utf-8 -*-

#import sklearn
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import matplotlib.pyplot as plt
#import pylab as pl

def OpenCSV(CSVDir,encoding='gbk'):
    csv = pd.read_csv(CSVDir,encoding=encoding)
    return csv


def PreProcess(csv):
    csv.pop(u'Unnamed: 25')
    csv.pop(u"?")
    csv = csv.loc[:71,:]
    csv.columns = ["Person","Season","Result","Match" ,"FirstLaunch",
                   "Time"  ,"uShoot","Hit"   ,"Shoot" ,"u3Point",
                   "Hit3"  ,"Shoot3","uFree" ,"FHit"  ,"FShoot",
                   "Bank"  ,"FBank" ,"BBank" ,"Assist","Steal",
                   "Block" ,"Mis"   ,"Foul"  ,"Point"]
    #pt1 = pl.plot(csv['FHit'],csv['Point'])
    
    Result = pd.get_dummies(csv['Result'], prefix= 'Result')
    Result.columns = ["R_Win","R_Lose"]
    Result.drop(["R_Lose"],axis=1,inplace=True)
    
    csv = pd.concat([csv,Result],axis=1)
    csv.drop(["Person","Season","Match","uShoot",'u3Point',"uFree",
              'Result','FBank','BBank','FirstLaunch'],axis=1,inplace=True)
    return csv


def findFeature(csv):
    plt.figure()
    

#    pt1 = plt.subplot(111)
#    
#    time_split = csv['Block']
#    
#    bar_width = 0.5
#    
#    pt1.bar(time_split,csv['Time'],bar_width)
#    pt1.bar(time_split+bar_width,csv['Time']*csv['R_Win'],bar_width,color='r')
#    
#    
#    return False
    
    # pt1 : win/Time
    pt1 = plt.subplot(331)
    pt1.set_title("win/Time")
    # pt2 : win/Bank
    pt2 = plt.subplot(332)
    pt2.set_title("win/Bank")
    # pt3 : win/Assist
    pt3 = plt.subplot(333)
    pt3.set_title("win/Assist")
    # pt4 : win/Steal
    pt4 = plt.subplot(334)
    pt4.set_title("win/Steal")
    # pt5 : win/Block
    pt5 = plt.subplot(335)
    pt5.set_title("win/Block")
    # pt6 : win/Foul
    pt6 = plt.subplot(336)
    pt6.set_title("win/Foul")
    # pt7 : win/Point
    pt7 = plt.subplot(337)
    pt7.set_title("win/Point")
    # pt8 : win/Mis
    pt8 = plt.subplot(338)
    pt8.set_title("win/Mis")
    
    
    pt1.scatter(csv['Time'],csv['R_Win'])
    pt2.scatter(csv['Bank'],csv['R_Win'])
    pt3.scatter(csv['Assist'],csv['R_Win'])
    pt4.scatter(csv['Steal'],csv['R_Win'])
    pt5.scatter(csv['Block'],csv['R_Win'])
    pt6.scatter(csv['Foul'],csv['R_Win'])
    pt7.scatter(csv['Point'],csv['R_Win'])
    pt8.scatter(csv['Mis'],csv['R_Win'])



def NaiveBayes(csv):
    # Gaussian
    gs = GaussianNB()
    c = csv.copy()
    c_Tst = c[:5]
    c_Tra = c[5:]
    # Every Column
    R_Win_Tst = c_Tst.pop("R_Win")
    R_Win_Tra = c_Tra.pop("R_Win")
    gs.fit(c_Tra,R_Win_Tra)
    pdt = gs.predict(c_Tst)
    R = pd.DataFrame(columns = ["Predict","Test_Result"])
    R["Predict"] = pdt
    R["Test_Result"] = R_Win_Tst
    return R



def main():
    csvdir = r"D:\Study\PythonProject\Sk_Learn\NBA_HD\Data\1718hd.csv"
    csv = OpenCSV(csvdir)
    csv = PreProcess(csv)
    #findFeature(csv)
    R = NaiveBayes(csv)
    
    return csv,R



if __name__ == "__main__":
    csv,R = main()