# Desafio -3) Descubra a lógica e complete o próximo elemento:
#a) 1, 3, 5, 7, ___
#b) 2, 4, 8, 16, 32, 64, ____
#c) 0, 1, 4, 9, 16, 25, 36, ____
#d) 4, 16, 36, 64, ____
#e) 1, 1, 2, 3, 5, 8, ____
#f) 2,10, 12, 16, 17, 18, 19, ____

#a) 1, 3, 5, 7, ___
sequence_a = [1, 3, 5, 7]
next_a = sequence_a[-1] + 2
print("Próximo elemento da sequência a):", next_a)

# Sequência b)
sequence_b = [2, 4, 8, 16, 32, 64]
next_b = sequence_b[-1] * 2
print("Próximo elemento da sequência b):", next_b)

# Sequência c)
sequence_c = [0, 1, 4, 9, 16, 25, 36]
next_c = sequence_c[-1] + len(sequence_c)**2
print("Próximo elemento da sequência c):", next_c)

# Sequência d)
sequence_d = [4, 16, 36, 64]
next_d = (len(sequence_d)*4)**2
print("Próximo elemento da sequência d):", next_d)

# Sequência e)
sequence_e = [1, 1, 2, 3, 5, 8]
next_e = sequence_e[-1] + sequence_e[-2]
print("Próximo elemento da sequência e):", next_e)

# Sequência f)
sequence_f = [2, 10, 12, 16, 17, 18, 19]
next_f = sequence_f[-1] + 1
print("Próximo elemento da sequência f):", next_f)
