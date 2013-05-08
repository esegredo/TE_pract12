#!/usr/bin/python

import sys, os.path
from uso_modulo import *
from math import *
from pylab import *

def readFile(fileName):
  # Opens the file
  myFile = open(fileName, 'r')
  i = 0
  matriz_exp_error = []

  # Reads the minimum and maximum values
  A = float(myFile.readline())
  B = float(myFile.readline())

  # Foreach identity
  while (i < len(lista_identidades)):
    i += 1
    j = 0
    # Saves the expressions in the first and second positions
    exp_error = [myFile.readline().rstrip('\n'), myFile.readline().rstrip('\n')]
    # Foreach threshold
    while (j < len(lista_umbrales)):
      j += 1
      # Saves the errors percentage
      exp_error.append(float(myFile.readline()))
    # Appends one list into another
    matriz_exp_error.append(exp_error)

  # Closes the file
  myFile.close()
  return [A, B, matriz_exp_error]

def draw(A, B, expr1, expr2, porcentajes, name):
  a = arange(A, B + 0.1, 0.1)
  b = arange(A, B + 0.1, 0.1)
  f1 = eval(expr1)
  f2 = eval(expr2)

  figure(1)
  subplot(211)
  plot(a, f1, 'r', label=expr1)
  plot(a, f2, 'bs', label=expr2)
  legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
  xlim(A, B)

  subplot(212)
  plot(range(len(lista_umbrales)), porcentajes, 'ro')
  xticks(range(len(lista_umbrales)), lista_umbrales)
  ylim(0.0, 100.0)
 
  savefig(name)
  show()
  return 0

if __name__ == '__main__':
  if (len(sys.argv) != 2):
    print 'Correct usage: {0} fileName'.format(sys.argv[0])
  else:
    fileName = sys.argv[1]
    if (not os.path.isfile(fileName)):
      print 'Filename {0} does not exist!'.format(fileName)
    else:
      A, B, matriz = readFile(fileName)
      # Foreach identity draw the corresponding plots
      i = 1
      for ident in matriz:
        draw(A, B, ident[0], ident[1], ident[2:], "identity" + str(i))
        i += 1
