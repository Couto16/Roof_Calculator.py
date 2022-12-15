


telha_escolhida = input('Escolha o tipo de telha desejada: \n 1 - Telha Romana \n 2 - Telha Francesa \n 3 - Telha Colonial \n 4 - Telha Paulista')

while ( telha_escolhida != '1' and telha_escolhida != 'Telha Romana' and telha_escolhida != '2' and telha_escolhida != 'Telha Francesa' 
and telha_escolhida != '3' and telha_escolhida != 'Telha Colonial' and telha_escolhida != '4' and telha_escolhida != 'Telha Paulista'):
    print('Entrada inválida. Tente novamente:\n')
    telha_escolhida = input('Escolha o tipo de telha desejada: \n 1 - Telha Romana \n 2 - Telha Francesa \n 3 - Telha Colonial \n 4 - Telha Paulista \n')
    
print(telha_escolhida)

madeira_escolhida = input('Escolha o tipo de madeira desejada: \n 1 - Andiroba \n 2 - Angelim \n 3 - Jequitibá \n 4 - Louro Amarelo \n 5 - Pau Marfim \n 6 - Peroba Rosa \n 7 - Pinho do Paraná') 

while ( madeira_escolhida != '1' and madeira_escolhida != 'Andiroba' and madeira_escolhida != '2' and madeira_escolhida != 'Angelim' 
and madeira_escolhida != '3'  and madeira_escolhida != 'Jequitibá' and madeira_escolhida != '4' and madeira_escolhida != 'Louro Amarelo' 
and madeira_escolhida != '5' and madeira_escolhida != 'Pau Marfim' and madeira_escolhida != '6' and madeira_escolhida != 'Peroba Rosa' 
and madeira_escolhida != '7' and madeira_escolhida != 'Pinho do Paraná' ):
    print('Entrada inválida. Tente novamente:\n')
    madeira_escolhida = input('Escolha o tipo de madeira desejada: \n 1 - Andiroba \n 2 - Angelim \n 3 - Jequitibá \n 4 - Louro Amarelo \n 5 - Pau Marfim \n 6 - Peroba Rosa \n 7 - Pinho do Paraná') 

print(madeira_escolhida)

comprimento, largura = input('Escolha o comprimento e a largura do telhado: ').split()
comprimento = float(comprimento)
largura = float(largura)

print(comprimento * largura)


class Madeira: 
    """Molde para madeira"""
    def __init__(self, nome, res_comp_axl, res_flx_est, elast_flx_est):
        self.nome = nome
        self.res_comp_axl = res_comp_axl
        self.res_flx_est = res_flx_est
        self.elast_flx_est = elast_flx_est
    
    def __repr__(self):
        return f'Madeira("{self.nome}", "{self.res_comp_axl}", "{self.res_flx_est}", "{self.elast_flx_est}")'

andiroba = Madeira(nome = 'Andiroba', res_comp_axl = 55.2, res_flx_est = 104.4, elast_flx_est = 11600)
angelim = Madeira(nome = 'angelim', res_comp_axl = 47.2, res_flx_est = 78.4, elast_flx_est = 10210)
jequitiba = Madeira(nome = 'Jequitibá', res_comp_axl = 59.3, res_flx_est = 131.6, elast_flx_est = 10350)
louro_amarelo = Madeira(nome = 'Louro Amarelo', res_comp_axl = 36.2, res_flx_est = 78.8, elast_flx_est = 8660)
pau_marfim = Madeira(nome = 'Pau Marfim', res_comp_axl = 60.1, res_flx_est = 139.9, elast_flx_est = 11720)
peroba_rosa = Madeira(nome = 'Peroba Rosa', res_comp_axl = 55.5, res_flx_est = 105.8, elast_flx_est = 9430)
pinho_parana = Madeira(nome = 'Pinho do Paraná', res_comp_axl = 43.2, res_flx_est = 87.3, elast_flx_est = 10930)



def calc_terca(telha_escolhida, madeira_escolhida):
    LT_1 = 0
    LT_2 = 0

    if telha_escolhida == 'Romana' or telha_escolhida == 1:
        print('Romana')
        LT_1 =  (5.0 * 10**-3 * madeira_escolhida.elast_flx_est) + 124.0
        print(LT_1)
        LT_2 = 0.585 * madeira_escolhida.res_flx_est + 96.2

    elif telha_escolhida == 'Francesa':
        print('Francesa')
        LT_1 = 5.76 * 10**-3 * madeira_escolhida.elast_flx_est + 119.0
        LT_2 = 0.442 * madeira_escolhida.res_flx_est + 118.0

    elif telha_escolhida == 'Colonial':
        print('Colonial')
        LT_1 = 5.04 * 10**-3 * madeira_escolhida.elast_flx_est + 118.0
        LT_2 = 0.606 * madeira_escolhida.res_flx_est + 89.0
    
    elif telha_escolhida == 'Paulista':
        print('Paulista')
        LT_1 = 5.71 * 10**-3 * madeira_escolhida.elast_flx_est + 104.0
        LT_2 = 0.667 * madeira_escolhida.res_flx_est + 78.8
    
    else:
        print('Telha inexistente')

    return print(LT_1, LT_2)



"""
print(calc_terca('Romana', madeira_escolhida))
print(andiroba)
print(angelim)
print(jequitiba)
print(louro_amarelo)
print(pau_marfim)
print(peroba_rosa)
print(pinho_parana)
"""

