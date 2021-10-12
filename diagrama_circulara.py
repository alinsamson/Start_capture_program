import matplotlib.pyplot as plt

#Diagrama circulare

def creare_diagrama_circulara(a,b):
    """
    Functie conceputa pentru a crea o diagrama circulara pentru cele doua argumente.
    Args: a, b - elementele diagramei
    Return: - diagrama circulara procentuala intre cele doua argumente
    """
    slices = [a,b]

    activities = ['TCP','UDP']

    cols = ['g','b']

    plt.pie(slices,

           labels=activities,

           colors=cols,

           startangle=90,

           shadow= True,

           autopct='%.2f%%')

    plt.title('Diagrama circula a pachetelor capturate')

    plt.legend()

    plt.show()


if __name__ == '__main__':
    creare_diagrama_circulara(2,5)
