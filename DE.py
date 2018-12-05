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
                if (rand.random() <= self.pr or j == jrand):
                    self.VecU[i][j] = self.VecV[x][j] + self.tolerance * (self.VecV[y][j] - self.VecV[z][j])
                else:
                    self.VecU[i][j] = self.VecV[i][j]

    def selection(self):
        for i in range(self.k):
            if self.fitness(self.VecU[i][0], self.VecU[i][1]) < self.fitness(self.VecV[i][0], self.VecV[i][1]):
                self.VecV[i][0] = self.VecU[i][0]
                self.VecV[i][1] = self.VecU[i][1]

    def fitness(self, x, y):
        return 100 * ((y - (x**2))**2) + ((1 - (x**2))**2)

    def norm(self, x):
        return math.floor(rand.random() * x)
def main():
    data = DE(20)

    print(data.VecV)

    evaluation = 0
    while(evaluation<100):
        data.mutasi()
        data.selection()

        print(evaluation,'\n',data.VecU)
        evaluation += 1
    # k = 40 #Numero de individuos
    # D = 2
    # Cr = 0.9 #Probabilidad de ser mutado de un individuo
    # F = 0.5  #Operador de cruzamiento

    # VectorV = np.empty((k, D))
    # VectorU = np.empty((k, D))

    # #Inicializar los arreglos
    # for i in range(k):
    #     for j in range(2):
    #         VectorV[i][j] = rand.randint(-10, 20)

    # plt.ion()
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.grid(True)
            
    # NumEvaluaciones = 0
    # while(NumEvaluaciones < 200):
    #     for i in range(k):
    #         r0 = i
    #         while(r0 == i):
    #             r0 = norm(k)
    #         r1 = r0
    #         while(r1 == r0 or r1 == i):
    #             r1 = norm(k)
    #         r2 = r1
    #         while(r2 == r1 or r2 == r0 or r2 == i):
    #             r2 = norm(k)
                
    #         jrand = norm(D)
            
    #         for j in range(D):
    #             if (rand.random() <= Cr or j == jrand):
    #                 #Mutaci�n
    #                 VectorU[i][j] = VectorV[r0][j] + F * (VectorV[r1][j] - VectorV[r2][j])
    #             else:
    #                 VectorU[i][j] = VectorV[i][j]

    #     for k in range(k):
    #         if fitness(VectorU[k][0], VectorU[k][1]) < fitness(VectorV[k][0], VectorV[k][1]):
    #             VectorV[k][0] = VectorU[k][0]
    #             VectorV[k][1] = VectorU[k][1]

    #     line1 = ax.plot(VectorU[:, 0], VectorU[:, 1],'b+')
    #     line2 = ax.plot(VectorV[:, 0], VectorV[:, 1],'g*')

    #     ax.set_xlim(-10, 20)
    #     ax.set_ylim(-10, 20)
        
    #     fig.canvas.draw()

    #     ax.clear()
    #     ax.grid(True)
        
    #     NumEvaluaciones += 1

def fitness(x, y):
    #Funcion Rosenbrock en 2D
    return 100 * ((y - (x**2))**2) + ((1 - (x**2))**2)

if '__main__' == main():
    main()