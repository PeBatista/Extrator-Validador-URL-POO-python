import re
class ExtratorUrl:
    def __init__(self,url):
        self._url = self.sanitiza(url)
        self.valida() # chamando a função na hora da própria instância, dps de receber o primeiro argumento
    
    def sanitiza(self,url):
        if type(url) == str: # se ela for uma String, passe por um Strip
            return url.strip()
        
        else: # se não, se for None ou 0, sei lá
            return ""
        
    
    def valida(self):
        padrao_url_opicionias = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')

        if not self._url: 
            raise ValueError("A URL está vazia!")
        
        if padrao_url_opicionias.match(self._url):
            print("URL cadastrada na Instância")
        else:
            raise ValueError("A URL é inválida")

    def __len__(self):
        return len(self._url)
    
    
        
    @property 
    def base_url(self):
        posicao_interrogacao = self._url.find('?')
        base = self._url[0:posicao_interrogacao] # bytebank.com/cambio
        return base
    
    @property
    def parametros_url(self):
        posicao_interrogacao = self._url.find('?')
        parametros = self._url[posicao_interrogacao+1:]
        return parametros
    
    def __str__(self):
        return f'Instância do Extrator URL: {self._url} \n {self.base_url} \n {self.parametros_url}'
    
    def __eq__(self,other):
        return self._url == other._url

    def valor_parametro(self,parametro):
        
        busca_parametro = self._url.find(parametro)
        indice_valor  = busca_parametro + len(parametro) + 1
        e_comercial = self._url.find("&",indice_valor) 
        
        if e_comercial == -1: # caso ele retorne que não achou o &_comercial, apartir do indice do valor.
            valor = self._url[indice_valor:]
        else: 
            valor = self._url[indice_valor:e_comercial] 
        
        return valor 
        
url = ExtratorUrl("www.bytebank.com.br/cambio?quantidade=100&moedaDestino=800") 
url1 = ExtratorUrl("www.bytebank.com.br/cambio?quantidade=100&moedaDestino=800") 

# dentro da classe:
 # def __eq__(self,other):
    #     return self._url == other._url

print(url == url1) # no terminal: True, mas mesmo sabendo que o ID é diferente
print(f'{id(url)} // `{id(url1)}`') # mesmo que: 2290686574496 // `2290686577200`
