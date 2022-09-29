
import numpy as np
import matplotlib.pyplot as plt



def LoadTxtMethod(fileName):
    data = np.loadtxt(fileName,dtype=np.float32,delimiter=' ');
    return data

if __name__=="__main__":
    dataR = LoadTxtMethod('D:\\TrackVisualization\\TrackVisualization\\LTrackHeadModel.txt')
    dataL = LoadTxtMethod('D:\\TrackVisualization\\TrackVisualization\\RTrackHeadModel.txt')
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.axis('equal')
    #plt.legend(loc='best',title='R/L track head model figure')
    
    for i in range(0,456):
        ax.scatter(dataR[i][0],dataR[i][1],c = 'b',marker = '.') 

    for i in range(0,456):
        ax.scatter(dataL[i][0],dataL[i][1],c = 'b',marker = '.') 

    plt.show()
    print('dataL=',dataL)
    print('dataR=',dataR)

    
