import numpy
import subprocess
import configparser
    
# Trabajo sistemas continuos Ejercicio 4 - Practica 8: Sistemas Continuos

# r = Tasa de crecimiento del numero de presas en ausencia de depredadores
# a = Coeficiente de depredador
# b = Tasa de crecimiento del numero del depresadores en presencia de presas
# m = Tasa de mortalidad del los depredadores

config = configparser.ConfigParser()
config.read('config.ini')
r = int(config['DEFAULT']['r'])
a = int(config['DEFAULT']['a'])
b = int(config['DEFAULT']['b'])
m = int(config['DEFAULT']['m'])

def main():
    
    #Maximo rango 
    max_rango = int(config['DEFAULT']['max_rango'])

    #Valores iniciales
    presa = 2
    depredador = 2
    h = 0.01

    #Se crean los archivos para guardar los datos
    presas_data = open("presas.txt", "w")
    depredadores_data = open("depredadores.txt", "w")
    presas_depredadores_data = open("ambos.txt", "w") 

    #Genera los datos
    for time in numpy.arange(0, max_rango, 0.01, dtype=float):
        presas_data.write(str(time) + ", " + str(presa) + "\n")    
        depredadores_data.write(str(time) + ", " + str(depredador) + "\n")
        presas_depredadores_data.write(str(presa) + ", " + str(depredador) + "\n")    

        #Se calcula usando el Metodo de euler se podria modularizar
        presa_new = euler_presas(presa, h, depredador)
        depredador = euler_depredador(depredador, h, presa)
        presa = presa_new

    #Se cierran los archivos
    presas_data.close()
    depredadores_data.close()
    presas_depredadores_data.close()

    #Subprocesos abrir gnuplot
    proc = subprocess.Popen(['gnuplot','-p'], shell=False, stdin=subprocess.PIPE,)
    proc2 = subprocess.Popen(['gnuplot','-p'], shell=False, stdin=subprocess.PIPE,)
    
    #Primera consigna
    proc.stdin.write('plot "presas.txt" with lines linestyle 1, "depredadores.txt" with lines linestyle 2 \n'.encode())
    
    #Segunda Consigna
    proc2.stdin.write('plot "ambos.txt" with lines linestyle 1 \n'.encode())


def euler_presas(presa, h, depredador): 
    return presa + (h * ((r * presa) - (a * presa * depredador)))


def euler_depredador(depredador, h, presa):
    return depredador + (h * ((b * presa * depredador) - (m * depredador)))

if __name__ == '__main__':
    main()
