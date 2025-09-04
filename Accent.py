'''
Write a sentence in English in the affirmative form,
and it will check if it contains the verb to be.
If it does, it will return the sentence as a question with the verb swapped.
If not, it will add an auxiliary verb and turn it into a question.
'''

class Accent:
           
    def threeSteps(self, question):

        verb_Tobe = ["i am", "you are", "he is", "she is",  "it is", "we are", "they are"] 
        verb_TobeInverted = ["am i", "are you", "is he", "is she", "is it", "are we", "are they"]

        # Ordena por tamanho decrescente para evitar conflito he is / she is
        verbs_sorted = sorted(zip(verb_Tobe, verb_TobeInverted), key=lambda x: len(x[0]), reverse=True)

        for original, inverted in verbs_sorted:
            if original.lower() in question.lower():
                start_index = question.lower().find(original.lower())
                end_index = start_index + len(original)
                result = question[:start_index] + inverted + question[end_index:]
                print(f"{result}?")
                return  

        # Se nenhum verbo TO BE foi encontrado
        print("Não foi identificado o Verbo ToBe")
        
        # Add DO and DOES when the verb TO BE is not present.

question = input("Digite a Frase no Afirmativo: ")
answer = Accent()
answer.threeSteps(question)









    