#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pi.py
#  
#  Copyright 2018 20181bsi0121 <20181bsi0121@SR6192>
#  
# 

def main():

    numerador = 4; denominador = 1; fracao = 0; cont = 0;

    while abs(numerador/denominador) >= 0.0001:
       
        if cont%2==0:
            fracao = fracao + (numerador/denominador)
        else:
            fracao = fracao - (numerador/denominador)  

        denominador = denominador+2;

        cont = cont +1;   
    
    print('Valor PI %.4f '%(fracao));

    return 0

if __name__ == '__main__':
	main()
