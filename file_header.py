from datetime import datetime 

_file_header = ['*']*240

def set_bank_code(bank_code : int) -> None: # G001
    # 1 to 3	Bank code.	Bank code where the sub issuer has an account opened by Dock
    # (use zeros to the left to fill in the remaining positions in case of 1 or 2 digits).

    bank_code = str(bank_code).zfill(3)
    _file_header[0:3] = bank_code

def set_lot_code(lot_code=0) -> None: # G002
    # 4 to 7	Lot code.	Fill in zeros.
    _file_header[3:7] = str(lot_code).zfill(4)

def set_register_type(register_type=0) -> None: # G003
    # 8	Registration type.	Fill in 0.
    _file_header[7:8] = str(register_type)

def set_G004_brancos() -> None: # G004 lol
    # Uso Exclusivo FEBRABAN / CNAB 
    # 9 até 17
    _file_header[8:17] = ' '*9
    # 133 até 142
    _file_header[132:142] = ' '*10
    # 212 até 240
    _file_header[211:240] = ' '*29

def set_tipo_registro_empresa(type : int) -> None: # G005
    # 18 até 18
    # 0 = Isento / Não Informado
    # 1 = CPF
    # 2 = CGC / CNPJ
    # 3 = PIS / PASEP
    # 9 = Outros
    _file_header[17:18] = str(type)

def set_registro_empresa(number : int) -> None: # G006
    # 19 to 32
    _file_header[18:32] = str(number).zfill(14)

def set_convenio_code(code='') -> None: # G007
    # 33 até 52
    if len(code):
        _file_header[32:52] = code.zfill(20)
    else:
        _file_header[32:52] = ' '*20

def set_agencia(agencia : int) -> None: # G008
    # 53 até 57
    _file_header[52:57] = str(agencia).zfill(5)

def set_digito_agencia(digito_agencia) -> None: # G009
    # 58 até 58
    _file_header[57:58] = str(digito_agencia)

def set_numero_conta_corrente(numero_conta : int) -> None: # G010
    # 59 até 70
    _file_header[58:70] = str(numero_conta).zfill(12)

def set_digito_conta_corrente(digito_conta) -> None: # G011
    # 71 até 71
    _file_header[70:71] = str(digito_conta)

def set_digito_agconta(digito_agconta='') -> None: # G012
    # 72 até 72
    if len(str(digito_agconta)):
        _file_header[71:72] = str(digito_agconta)
    else:
        _file_header[71:72] = ' '

def set_nome_empresa(nome_empresa : str) -> None: # G013
    # 73 até 102
    _file_header[72:102] = nome_empresa.ljust(30, ' ')

def set_nome_banco(nome_banco : str) -> None: # G014
    # 103 até 132
    _file_header[102:132] = nome_banco.ljust(30, ' ')

def set_codigo_remessa_retorno(codigo : int) -> None: # G015
    # 143 até 143
    # 1 Remessa (cliente banco)
    # 2 Retorno (banco cliente)
    _file_header[142:143] = str(codigo)

def set_data_geracao_arquivo(): # G016
    # 144 até 151
    _file_header[143:151] = datetime.now().strftime("%d%m%Y")

def set_hora_geracao_arquivo(): # G017
    # 152 até 157
    _file_header[151:157] = datetime.now().strftime("%H%M%S")

def set_numero_sequencial_arquivo(nsa : int): # G018
    # 158 até 163
    _file_header[157:163] = str(nsa).zfill(6)

def set_numero_versao(): # G019
    # 164 até 166
    _file_header[163:166] = '103'

def set_densidade_gravacao(bpi=1600): # G020
    # 167 até 171
    _file_header[166:171] = str(bpi).zfill(5)

def set_observacoes_banco(): # G021
    # 172 até 191
    # espaço reservado para uso do banco.
    _file_header[171:191] = ' '*20

def set_observacoes_empresa(obs=''):
    # 192 até 211
    if len(obs):
        obs = obs[:20]
        _file_header[191:211] = obs.ljust(20, ' ')
    else:
        _file_header[191:211] = ' '*20



set_G004_brancos()

# Controle
set_bank_code('77')
set_lot_code()
set_register_type()

# Empresa
set_tipo_registro_empresa(2)
set_registro_empresa('44274504000175')
set_convenio_code()
set_agencia('987')
set_digito_agencia('3')
set_numero_conta_corrente('72985')
set_digito_conta_corrente('0')
set_digito_agconta()
set_nome_empresa('EMPRESA S/A')
set_nome_banco('BANCO INTER S/A')

# Arquivo
set_codigo_remessa_retorno(1)
set_data_geracao_arquivo()
set_hora_geracao_arquivo()
set_numero_sequencial_arquivo(1)
set_numero_versao()
set_densidade_gravacao()

set_observacoes_banco()
set_observacoes_empresa()

print(''.join(_file_header))