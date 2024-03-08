# Desafio -4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.
#Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

import time

def test_lights(switches):
    # Ligar o primeiro interruptor
    switches[0] = True
    time.sleep(1)  # Esperar um tempo suficiente para a lâmpada esquentar

    # Ligar o segundo interruptor e desligar o primeiro
    switches[1] = True
    switches[0] = False
    time.sleep(1)  # Esperar um tempo suficiente para a lâmpada esquentar

    # Descobrir qual lâmpada está acesa
    for i, switch in enumerate(switches):
        if switch:
            return i  # Retorna o índice da lâmpada acesa

# Inicializa os interruptores (False = desligado, True = ligado)
switches = [False, False, False]

# Testa as lâmpadas
lamp_index = test_lights(switches)

# Determina qual interruptor controla cada lâmpada
if lamp_index == 0:
    print("O primeiro interruptor controla a primeira lâmpada.")
    print("O segundo interruptor controla a terceira lâmpada.")
    print("O terceiro interruptor controla a segunda lâmpada.")
elif lamp_index == 1:
    print("O primeiro interruptor controla a terceira lâmpada.")
    print("O segundo interruptor controla a primeira lâmpada.")
    print("O terceiro interruptor controla a segunda lâmpada.")
else:
    print("O primeiro interruptor controla a terceira lâmpada.")
    print("O segundo interruptor controla a segunda lâmpada.")
    print("O terceiro interruptor controla a primeira lâmpada.")
