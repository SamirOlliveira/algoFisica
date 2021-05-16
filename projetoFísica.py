# Este script simples, mas funcional, tem como  intuito
# Servir como correção de problemas de física para estudantes de
#ensino medio, vestibular, enem e afins.
import math 
import time

def traco():
    print('='*90)
#esta função me será util quando eu quiser pular uma linha 

def jump():{
    print('\n ')
}
jump()

#esta função sevirá para a introduçao
def intro():{
    #introdução ao código 
    
    print('''              ==================== AUXÍLIO EM FÍSICA ====================
        Abaixo temos opções de programas de resoluções dos respectivos problemas.
    Forneça as opções de maneira correta, e terá a correção de maneira imediata
    [1]Trabalho
    [2]Ondas

    Bons estudos! :D''')
}
intro()
# definindo variavl de escolha 
jump()
esc = str(input('Digite sua escolha: '))

jump()
traco()
jump()

# estrutura da escolha 
if esc == '1':
    esc2 = str(input('''Selecione o tipo de exercício na qual você
    queira fazer a devida correção:
    1) Trabalho de uma forçã CONSTANTE
    2)Potência e Velocidade
    3)Relação entre trabalho e energia cinética]
    4)Mecânica
    
    selecione a opção: '''))

    traco()

    if esc2 == '1':
        print('Trabalho de uma força constante T = Fº.Dº.α')
        
        esc3 = str(input('o calculo apresenta cosseno de alfa? [s/n]'))
        #convertendo para maiusculo
        conV = esc3.upper()

        if conV == 'N':
            class Trab_FC(): 
                # definindo parametros para a 
                # construção do programa
                def __init__(self, forca, des):
                    self.forca = forca
                    self.des = des
                def calc(self):
                    return print(f'o valor do T = Fº.Dº.α será:\n{self.forca*self.des}j')

            forca = float(input('Digite a força: '))
            des = float(input('Digite o deslocamento: '))

            resul = Trab_FC(forca, des)

            print(resul.calc()) #objeto instanciado + a função 

        else:
            class Trab_FC(): 
                # definindo parametros para a 
                # construção do programa
                def __init__(self, forca, des, alpha):
                    self.forca = forca
                    self.des = des
                    self.alpha = alpha
                def calc(self):
                    return print(f'o valor do T = Fº.Dº.α será:\n{self.forca*self.des*self.alpha}j')

            forca = float(input('Digite a força: '))
            des = float(input('Digite o deslocamento: '))
            alpha = float(input('Digite o valor de alfa: '))

            resul = Trab_FC(forca, des, alpha)

            print(resul.calc()) #objeto instanciado + a função 

    elif esc2 == '2':

        print('Potência e Velocidade')
        
        class PotMedia():
            #passando parametros 
            #construção do programa 
            def __init__(self, forca, Vel_m):
                self.forca = forca
                self.Vel_m = Vel_m
            def calc(self):
                return print(f'o resultado da potência média P= F.V:\n{self.forca*self.Vel_m}')
        
        forca = float(input('Digite a força: '))
        velM = float(input('Digite a velocidade média:'))

        resulta = PotMedia(forca, velM)

        print(resulta.calc())

    elif esc2 == '3':
        print('Relação entre potencia e velocidade')

        class Re_V_P():
            #passando parametros
            #construção do programa
            
            def __init__(self, m_sa, v_º, vf):

                self.m_sa = m_sa
                self.v_º = v_º
                self.vf = vf
                
            #calcLando :D function 

            def calc(self):

                in_i = self.m_sa*(math.pow(self.v_º, 2))/2
                fm = self.m_sa*(math.pow(self.vf, 2))/2

                jump()

                print(f''' A Energia Cinética inicial é, Ec°: {in_i}J 
                A Energia Cinética final é: {fm}J''')
                
                jump()

                # tempo p ficar bonitin

                time.sleep(0.5)

                return(f"O Trabalho da força resultante é Trf: {fm-in_i} j")
            
        m_s = float(input("Digite a massa: "))

        v_i = float(input("Digite a velocidade inicial: "))

        v_f = float(input("Digite a velocidade final: "))
        
        #instanciando o objeto 

        Tfr = Re_V_P(m_s, v_i, v_f)

        print(Tfr.calc())

    elif esc2 == '4': 

        print('''Mecânica (sistema de conservação)
        Para resolver este problema você deverá assinar a baixo
        e desprezar as energias, para que assim, consigamos calcular e mostrar a você
        sua resposta.
        
        Considere pontos °A e pontos °B''')

        #Energia potencial cinética

        Ec = str(input('há energia cinética?[S/N]: '.upper()))

        #Energia potencial gravitacional 

        Epg = str(input('há energia potencial gravitacional?[S/N]: '.upper()))

        #Energia potencial elastica

        Epe = str(input('há energia pitencial elástica?[S/N]: '.upper()))

        if Ec =='S' and Epg=='S' and Epe=='N':
        
        #definindo a classe
            class Epga_Epgc():

                #definindo parâmetros e atributos
                
                def __init__(self, massa, h, ):

                    # definindo massa e altura
                    #para que assim o resultado seja obtido

                    self.massa = massa
                    self.h = h 

                





    