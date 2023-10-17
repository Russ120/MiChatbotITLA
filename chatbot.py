import random
import re
import datos as resp


def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_message(split_message)
    return response




def message_probability(user_message, recognized_words, single_response=False, required_word=[],segund_required_word=[]):
    message_certainty=0
    has_required_words=True
    has_segund_required_words=True

    for word in user_message:
        if word in recognized_words:
            message_certainty+=1

    percentage = float(message_certainty) / float(len(recognized_words))


    for word in required_word:
        if word not in user_message:
            has_required_words=False
            break

    for word in segund_required_word:
        if word not in user_message:
            has_segund_required_words=False
            break

    if has_required_words or has_segund_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0




def check_all_message(message):
    highest_prob={}



    def response(bot_response, list_of_words, single_response = False, required_word=[],segund_required_word=[]):
        nonlocal highest_prob

        highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_word, segund_required_word)

#Saludo
    response(resp.saludo, resp.saluLC, single_response = True)
    

#Horario Oficinas
    response(resp.horarioDeOficinas, resp.horarioLC, single_response = True)


#Solicitar Carnet
    response(resp.solicitarCarnet, resp.solicitarCarnet, required_word=['carnet'])


#Carreras del ITLA
    response(resp.carrerasITLA, resp.carrerasLC ,single_response = True)


#retirar una asignatura
    response(resp.retirarAsignatura, resp.retirarLC, required_word=['retirar'], segund_required_word=['retiro'])


#donde realizar pagos
    response(resp.realizarPagos, resp.realizarLC, required_word=['donde'])


#Formas de pago
    response(resp.formasDePago, resp.formasLC, single_response = True)


#Inscribirse en linea
    response(resp.inscripcionVirtual,resp.inscripcionLC, single_response = True)


#Año que se fundó
    response(resp.añoFundadoITLA,resp.añoFundadoLC,single_response = True)


#Mision del itla
    response(resp.misionITLA, resp.misionLC, single_response = True)


#procedimiento para obtener tickets de transporte
    response(resp.procedimientoTikectsTransp, resp.procedimientoLC, required_word=['transporte'])


#Quien es el Rector del itla
    response(resp.rectorITLA, resp.rectorLC, single_response = True)



    best_match = max(highest_prob,key=highest_prob.get)
    
    return unknown() if highest_prob[best_match] < 1 else best_match





def unknown():

    response=['No entendí, por favor formular la pregunta de otra forma','No tengo programada la respuesta a esta pregunta',
               'Lo siento no tengo esta informacion, dirigete a nuestra plataforma https://itla.edu.do para obtenerla'][random.randrange(3)]
    return response





while True:

    consulta = input('You: ')
    print("Sir:"+get_response(consulta) + "\n")