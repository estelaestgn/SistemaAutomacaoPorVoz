import speech_recognition as sr
import pyfirmata

pinCozinha = 13
pinSala = 12
pinQuarto = 8

port = 'COM4'
board = pyfirmata.Arduino(port)

#Função para ouvir e reconhecer a fala
def ouvir_microfone():

    #Habilita o microfone do usuário
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
    #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        #Frase para o usuario dizer algo
        print("Diga alguma coisa: ")

        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
    try:
        #Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio,language='pt-BR')

        if "acender cozinha" in frase:
            board.digital[13].write(1)

        elif "apagar cozinha" in frase:
            board.digital[13].write(0)

        elif "acender sala" in frase:
            board.digital[12].write(1)

        elif "apagar sala" in frase:
            board.digital[12].write(0)

        elif "acender quarto" in frase:
            board.digital[8].write(1)

        elif "apagar quarto" in frase:
            board.digital[8].write(0)

        #Retorna a frase pronunciada
        print("Você disse: " + frase)

    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")

    return frase

ouvir_microfone()