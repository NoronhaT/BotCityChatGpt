import time
import webbrowser
import selenium.common.exceptions
from botcity.web import WebBot
from botcity.web import By
import requests
import os
import shutil
import openai
import pyautogui as pya
from googletrans import Translator
import ftfy




# Utilizo Google Translate para converter a solicitação do usuário para o inglês e melhorar os resultados da busca de
# img.

translator = Translator()
chrome_path= r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
print('---------------------------------------------')
print('ASSISTENTE DE ENVIO DE POSTAGENS - BotCitySocilMedia')

diretorio_atual = os.getcwd()
diretorio_chave = diretorio_atual + '/Chave'
diretorio_video = diretorio_atual + '/Videos'
diretorio_fotos = diretorio_atual + '/Fotos'
diretorio_frases = diretorio_atual + '/Frases'
diretorio_imagens = diretorio_atual + '\Imagem'


def criar_diretorios():
    # Checa se o diretório existe e o cria caso não.
    if not os.path.exists(diretorio_atual + "/Videos"):
        os.makedirs(diretorio_atual + "/Videos")
        print('CRIANDO O DIRETÓRIO PARA REELS')
    if not os.path.exists(diretorio_atual + "/Fotos"):
        os.makedirs(diretorio_atual + "/Fotos")
        print('CRIANDO O DIRETÓRIO PARA FEED')
    if not os.path.exists(diretorio_atual + "/Frases"):
        os.makedirs(diretorio_atual + "/Frases")
        print('CRIANDO O DIRETÓRIO PARA Frases')
    if not os.path.exists(diretorio_atual + '/Chave'):
        os.makedirs(diretorio_atual + '/Chave')
        print('CRIANDO O DIRETÓRIA PARA Chave')
    if not os.path.exists(diretorio_atual + '/Imagem'):
        os.makedirs(diretorio_atual + '/Imagem')
        print('CRIANDO O DIRETÓRIA PARA Imagem')


def user():
    try:
        print('Procurando pelo seu login')
        print('-------------------------')
        with open(diretorio_chave + '/user.txt', 'r') as key:
            for i in key:
                print('Usuário encontrado!')
                print('-------------------')

    except Exception:

        print('Login não encontrado, insira novamente: ')
        usuario_instagram = input('Insira seu nome de usuário:')
        with open(diretorio_chave + '/user.txt', 'w', encoding='utf-8') as key:
            key.write(usuario_instagram)


def senha():
    try:
        print('Procurando pelo seu login')
        print('-------------------------')
        with open(diretorio_chave + '/pass.txt', 'r') as key:
            for i in key:
                print('senha encontrada!')
                print('-------------------------')

    except Exception:

        print('Senha não encontrada, insira novamente: ')
        print('-------------------------')
        senha_instagram = input('Insira sua senha:')
        with open(diretorio_chave + '/pass.txt', 'w', encoding='utf-8') as key:
            key.write(senha_instagram)


def chave_openia():
    try:
        print('Procurando pela chave da OpenIa')
        print('-------------------------')
        with open(diretorio_chave + '/chave.txt', 'r') as key:
            for i in key:
                print('Chave encontrada!' + '\n' + 'Prosseguindo com o programa.')

    except Exception:

        print('Chave não encontrada, é necessário inserir uma chave: ')
        print('-------------------------')
        chave = input('Insira chave:')
        with open(diretorio_chave + '/chave.txt', 'w', encoding='utf-8') as key:
            key.write(chave)


def tema():
    print('Selecione uma das opções, sendo número:' + '\n' + '1- para Feed' + '\n' + '2- para Stories')
    print('---------------------------------------------')
    assunto = '1'  #por enquanto só suporte a publicações de feed

    if assunto == '1':
        print('Lançamento em Feeds')

        with open(diretorio_frases + '/opcao.txt', 'w', encoding='utf-8') as opcao:
            opcao.write(assunto)

    elif assunto == '2':
        print('Lançamento em Stories')

        with open(diretorio_frases + '/opcao.txt', 'w', encoding='utf-8') as opcao:
            opcao.write(assunto)

    else:
        print('É necessário que você selecione uma opção válida')
        print('---------------------------------------------')
        tema()


def frase_tema():
    print('Escreva detalhadamente sobre o que será o seu post')
    print('---------------------------------------------')
    frase = input("Sobre o que será o post?: ")
    frase = frase + ' insira hashtags ao final do texto escrito.'
    with open(diretorio_frases + '/texto.txt', 'w', encoding='utf-8') as theme:
        theme.write(frase)


def buscador_imagem():
    # remover arquivo anterior
    shutil.rmtree(diretorio_imagens)
    print('Que tipo de imagem você quer inserir no seu post?')
    busca = input('Insira a imagem a ser buscada: ')
    print('-------------------------------------------------')
    print(f'Sua busca de imagem é: {busca}')

    trad = translator.translate(busca)

    busca = str(trad.text)

    if not os.path.exists(diretorio_atual + '/Imagem'):
        os.makedirs(diretorio_atual + '/Imagem')

    response = openai.Image.create(
        prompt=busca,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    res = requests.get(image_url, stream=True)
    print('Verifique a imagem em seu browser.')
    webbrowser.get('chrome').open_new_tab(image_url)
    time.sleep(10)
    print('------------------------------------------------------------------------')

    imagem_ia = busca + '.jpg'

    if res.status_code == 200:
        with open(imagem_ia, 'wb') as f:
            shutil.copyfileobj(res.raw, f)


    shutil.move(imagem_ia, diretorio_imagens)





# PARAMETROS

try:
    with open(diretorio_chave + '/user.txt', 'r') as userw:
        for i in userw:
            usuario_instagram = i
    with open(diretorio_chave + '/pass.txt', 'r') as passw:
        for i in passw:
            senha_instagram = i
    with open(diretorio_frases + '/opcao.txt', 'r') as option:
        for i in option:
            opcao = i
    with open(diretorio_frases + '/texto.txt', 'r') as option:
        for i in option:
            texto = i
except FileNotFoundError:
    pass


def openia():
    chave = []
    pergunta = []

    with open(diretorio_frases + '/texto.txt', 'r') as assunto:
        for i in assunto:
            pergunta.append(i)

    with open(diretorio_chave + '/chave.txt', 'r') as key:
        for i in key:
            chave.append(i)
    openai.api_key = chave[0]
    gpt_prompt = pergunta[0]
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=gpt_prompt,
        temperature=0.5,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    resposta = (response['choices'][0]['text'])

    with open(diretorio_frases + '/openia.txt', 'w', encoding='utf-8') as codigo:
        codigo.write(resposta)


class Bot(WebBot):
    def action(self, execution=None):

        self.headless = False
        # WebDriver path
        self.driver_path = r"C:\bin\chromedriver.exe"
        # website.
        self.browse("https://www.instagram.com/")
        self.maximize_window()

        print(f'PÁGINA ACESSADA: {self.page_title()}')

        self.wait(5000)
        print('executando o login...')
        print('---------------')

        try:
            print('Nome de usuário')
            print('---------------')
            nome_user = self.find_element(
                '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input',
                by=By.XPATH)
            nome_user.send_keys(usuario_instagram)

            print('Senha')
            print('-----')

            self.tab()
            self.paste(senha_instagram)
            self.enter()

            self.wait(5000)
            print('Login efetuado com sucesso!')
            print('---------------')

            if self.find_element(
                selector="/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]",
                by=By.XPATH):
                    self.find_element(
                        selector="/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]",
                        by=By.XPATH).click()
            self.wait(10000)

            print('Iniciando postagem')
            print('---------------')
            postar = self.find_element(selector='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div['
                                                '1]/div/div/div/div/div[2]/div[7]/div/div/a/div', by=By.XPATH)

            postar.click()
            self.wait(10000)
            adicionar = self.find_element(selector='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div['
                                                   '3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div['
                                                   '2]/div/button', by=By.XPATH)
            print('buscando imagem')
            print('---------------')
            adicionar.click()

            if self.find_element(
                    selector='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]',
                    by=By.XPATH):
                self.find_element(
                    selector='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]',
                    by=By.XPATH).click()
            else:
                print('Ignorando um elemento adicional')
                print('---------------')

            self.wait(10000)

            dir_imagem = os.listdir(diretorio_imagens)
            imagem = dir_imagem[0]
            caminho = os.path.join(diretorio_imagens,imagem)

            pya.write(caminho)
            pya.press('enter')
            self.wait(3000)

            botao_avancar = self.find_element(selector='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div['
                                                       '3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div['
                                                       '3]/div/button', by=By.XPATH)
            botao_avancar.click()
            self.wait(3000)
            print('Avançando com a postagem...')
            botao_avancar_dois = self.find_element(
                selector='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button',
                by=By.XPATH)
            botao_avancar_dois.click()
            self.wait(5000)
            print('Avançando com a inserção do texto...')
            print('------------------------------------')
            post = []

            post = []

            with open(diretorio_frases + '/openia.txt', 'r', encoding='utf-8') as txt:
                for i in txt:
                    post.append(i)
            post = ' '.join(post)
            post = ftfy.fix_text(post)

            postagem = self.find_element(
                selector='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea',
                by=By.XPATH)
            postagem.click()
            self.wait(3000)
            postagem.send_keys(post)


            print(f'Escrevendo sobre {post}')
            print('---------------')
            self.wait(10000)

            print('Publicando seu post!')
            print('---------------')
            compartilhar = self.find_element(
                selector='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button',
                by=By.XPATH)
            compartilhar.click()

            print('Ação executada com sucesso!')
            print('---------------')
            input('Dê um enter para sair')


        except selenium.common.exceptions.NoSuchWindowException:
            print('Algo durante o processo falhou, tentando novamente em 1 minuto')
            for i in range(60):
                self.wait(1000)
                print(i)

            print('reiniciando')
            print('-----------')
            return Bot.main()

    def not_found(self, label):
        print(f"Elemento não encontrado: {label}")


if __name__ == '__main__':
    criar_diretorios()
    user()
    senha()
    chave_openia()
    tema()
    frase_tema()
    openia()
    buscador_imagem()
    Bot.main()
