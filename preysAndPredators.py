import numpy
import subprocess
    
# Trabajo sistemas continuos Ejercicio 4 

# r = Tasa de crecimiento del numero de presas en ausencia de depredadores
# a = Coeficiente de depredador
# b = Tasa de crecimiento del numero del depresadores en presencia de presas
# m = Tasa de mortalidad del los depredadores

r = 3
a = 2
b = 1 
m = 2

def main():
    i = 0
    t = 0

    temp = 20
    presa = 2
    depredador = 2
    f = open("presas.txt", "w")
    t = open("depredadores.txt", "w")
    d = open("ambos.txt", "w") 

    for time in numpy.arange(0, temp, 0.01, dtype=float):
        f.write(str(time) + ", " + str(presa) + "\n")    
        t.write(str(time) + ", " + str(depredador) + "\n")
        d.write(str(presa) + ", " + str(depredador) + "\n")    

        presa_new = presa + (0.01 * ((r * presa) - ((a * presa) * depredador)))
        depredador = depredador + (0.01 * ((b * presa * depredador) - (m * depredador)))
        presa = presa_new

    f.close()
    t.close()
    d.close()

    #Subprocesos 
    proc = subprocess.Popen(['gnuplot','-p'], shell=False, stdin=subprocess.PIPE,)
    proc2 = subprocess.Popen(['gnuplot','-p'], shell=False, stdin=subprocess.PIPE,)
    
    #Primera consigna
    proc.stdin.write('plot "presas.txt" with lines linestyle 1, "depredadores.txt" with lines linestyle 2 \n'.encode())
    
    #Segunda Consigna
    proc2.stdin.write('plot "ambos.txt" with lines linestyle 1 \n'.encode())


if __name__ == '__main__':
    main()
