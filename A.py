#!usr/bin/env python
#-*- coding: utf-8 -*-
#
# Problema  - Acordes intergaláticos
# Tempo de execução limite - 1 seg
# 
# --- Input ---
# A primeira linha da entrada contém dois inteiros, N (2 <= N <= 100000), e Q (1 <= Q <= 100000),
# respectivamente o número de teclas do piano intergalático e a quantidade de acordes. As Q linhas
# seguintes contêm, cada uma, dois inteiros A e B, (0 <= A < B < n), representando um acorde.
# 
# --- Output ---
# Seu programa deve imprimir N inteiros, um por linha, representando as notas associadas às teclas
# do piano, após todos os acordes terem sido tocados
# 
# --- Exemplo ---
#   - Entrada -     - Saída -
#       5 3             5
#       1 2             6
#       0 4             6
#       0 2             2
#                       2
#                       

def getInputs():
    n_keys, n_chords = map( int, raw_input().split() )
    return n_keys, n_chords

def mountData(n_keys, n_chords):
    keys = [1 for i in range(n_keys)]
    chords = list()
    for i in range(n_chords):
        chords.append( map(int, raw_input().split()) )
    return keys, chords

def playChord(keys, chord):
    if len(keys[chord[0] : chord[1] + 1]) == len( set(keys[chord[0] : chord[1] + 1]) ):
        mostfrequent = max( keys[chord[0] : chord[1] + 1] )
    else:
        mostfrequent = max( set(keys[chord[0] : chord[1] + 1]), key=keys.count )

    for index, key in enumerate( keys[chord[0] : chord[1] + 1] ):
        keys[index + chord[0]] = (key + mostfrequent) % 9


if __name__ == '__main__':
    n_keys, n_chords = getInputs()
    keys, chords = mountData(n_keys, n_chords)

    for chord in chords:
        playChord(keys, chord)

    print '\n'.join(str(key) for key in keys)