import numpy as np
import random as rand
import matplotlib.pyplot as plt
import math

class DE:
    def __init__(self, k, probability = 0.9, max_tolerance = 0.5):
        self.k = k
        self.D = 2
        self.pr = probability
        self.tolerance = max_tolerance

        self.VecV = self.createV()
        self.VecU = np.empty((self.k,self.D))

    def createV(self):
        vector = np.empty((self.k,self.D))

        for i in range(self.k):
            for j in range(2):
                vector[i][j] = rand.randint(-10,10)

        return vector


    def mutasi(self):

        for i in range(self.k):
            x = i
            while(x == i):
                x = self.norm(self.k)
            y = x
            while(y == x or y == i):
                y = self.norm(self.k)
            z = y
            while(z == y or z == x or z == i):
                z = self.norm(self.k)
                
            jrand = self.norm(self.D)
            
            for j in range(self.D):
                if (rand.random() <= self.pr):
                    self.VecU[i][j] = (self.VecV[x][j] + self.tolerance * (self.VecV[y][j] - self.VecV[z][j]))
                else:
                    self.VecU[i][j] = self.VecV[i][j]

    def selection(self):
        for i in range(self.k):
            if self.fitness(self.VecU[i][0], self.VecU[i][1]) < self.fitness(self.VecV[i][0], self.VecV[i][1]):
                print('Change '+str(i))
                print(self.VecV[i],' <-- ',self.VecU[i])
                self.VecV[i][0] = self.VecU[i][0]
                self.VecV[i][1] = self.VecU[i][1]

    def fitness(self, x, y):
        return 100 * ((y - (x**2))**2) + ((1 - (x**2))**2)

    def norm(self, x):
        return math.floor(rand.random() * x)

def main():
    k = 5
    data = DE(k)
    eval = k * 8

    fig = plt.figure()
    figd = plt.figure()
    dx = figd.add_subplot(111)
    ax = fig.add_subplot(111)
    print(data.VecV)

    evaluation = 0
    while(evaluation<eval):
        print('---------------------')
        print('Evaluation '+str(evaluation))
        data.mutasi()
        print('Vector U')
        print(data.VecU)
        data.selection()
        print('Selection')
        print(data.VecV)
        
        line1 = ax.plot(data.VecU[:, 0], data.VecU[:, 1],'g.')
        line2 = ax.plot(data.VecV[:, 0], data.VecV[:, 1],'b1')
        line1 = dx.plot(data.VecU[:, 0], data.VecU[:, 1],'g.')
        line2 = dx.plot(data.VecV[:, 0], data.VecV[:, 1],'b1')
        ax.grid(True)
        dx.grid(True)
        ax.set_xlim(-20, 20)
        ax.set_ylim(-20, 20)

        if evaluation < eval/4 or evaluation % 10 == 0 or evaluation > eval - (eval/4):
            fig.savefig('./evol_conc_v'+str(evaluation+1)+'.png')
            figd.savefig('./evol_conc_v'+str(evaluation+1)+'d.png')
            ax.clear()
            dx.clear()
        
        evaluation += 1

if '__main__' == main():
    main()