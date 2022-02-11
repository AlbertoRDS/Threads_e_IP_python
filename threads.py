from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto+=velocidade
        time.sleep(0.5)
        print('Piloto: {} km: {} \n'.format(piloto, trajeto))

# def carro2 ( velocidade ) :
#     trajeto = 0
#     while trajeto <= 100 :
#         print('carro2: ' , trajeto)
#         trajeto += velocidade

t_carro1 = Thread(target=carro, args=[1, 'Alberto'])
t_carro2 = Thread(target=carro, args=[2, 'rocha'])

t_carro1.start()
t_carro2.start()