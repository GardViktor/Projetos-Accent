'''
Escrever uma frase em ingles no afirmativo
e ele identificar se tem o verdo to be, se sim
vai me retornar a frase em pergunta com o verbo trocado
se não ele vai adicionar um verbo auxiliar e transformar em pergunta
'''

class Accent():

    def __init__(self, question):
        self.question = question
    
    def threeSteps(self):

        verb_Tobe = ["i am", "you are", "he is", "she is", "it is", "we are", "they are"]
        verb_TobeInverted = ["am i", "are you", "is he", "is she", "is it", "are we", "are they"]

        if question in verb_Tobe:
            print(True)
            #Preciso Retornar a posição certinha que corresponde
            #list.index(element, start, end)
            print(verb_Tobe.index(question))
            print(len(question))
            print("Tem verbo ToBe")

        else:
            print(False)
            print(len(question))
            print("Não tem verbo ToBe")

question = input("Digite a Frase: ")

answer = Accent(question)
answer.threeSteps()









    