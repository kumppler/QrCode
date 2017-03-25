import pyqrcode

def qrcode():
    strNomeCliente = "Nome do Cliente:"
    strResponsavelCliente = "Nome do Responsavel:"
    strTelefone = "Telefone:"
    
    print(strNomeCliente),
    cliente = input()
    print(strResponsavelCliente),
    responsavel = input()
    print(strTelefone)
    telefone = input()
    
    strDadoCliente = strNomeCliente + cliente + "\015" + strResponsavelCliente + responsavel + "\015" + strTelefone + telefone
    
    q = pyqrcode.create(strDadoCliente)
    q.png('QrCode.png' , scale=6)
    print('QR code criado com sucesso')

if __name__ == '__main__':
    qrcode()
