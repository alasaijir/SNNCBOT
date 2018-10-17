import vk_api, random, sys, datetime
from vk_api.longpoll import VkLongPoll, VkEventType


def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = True

    return key, remember_device

def main():
    bad_words = [
        'пидор', 'ты пидор', 'ти пидор',
        'пэдро', 'ты пэдро', 'ти пэдро',
        'пыдар', 'ты пыдар', 'ти пыдар',
        'пидр', 'ты пидр', 'ти пидр',
        'ты пизда', 'ти пизда',
        'Пидорас', 'ты пидорас', 'ти пидорас',
        'тварь', 'ты тварь', 'ти тварь',
        'говно', 'ты говно', 'ти говно',
        'ты сука', 'ти сука',
        'член','ты член', 'ти член',
        'даун', 'ты даун', 'ти даун',
        'аутист', 'ты аутист', 'ти аутист',
        'долбаеб', 'ты долбаеб', 'ти долбаеб',
        'долбаёб', 'ты долбаёб', 'ти долбаёб',
        'долбоеб', 'ты долбоеб', 'ти долбоеб',
        'долбоёб', 'ты долбоёб', 'ти долбоёб',
        'говноед', 'ты говноед', 'ти говноед',
        'ты блядь', 'ти блядь',
        'ты блять', 'ти блять',
        'пошел нахуй', 'пошел ты нахуй', 'иди нахуй', 'иди на хуй', 'пошел на хуй',
        'ты хуй', 'ти хуй',
        'иди в пизду', 'пошел в пизду',
        'гей', 'ты гей', 'ти гей',
        'чмо', 'ты чмо', 'ти чмо',
        'чьмо', 'ты чьмо', 'ти чьмо',
        'лох', 'ты лох', 'ти лох',
        'соси','гондон','гандон',
    ]

    maty = [
        'хуй', 'залупа', 'пизда', 'ебать', 'ебал', 'ебаный', 'ебанный', 'ебал в рот', 'ебаный рот', 'ебанный рот', 'в пизду','блять','блядь','бля', 'ублюдок мать твою',
        'сука', 'похуй', 'нахуй', 'хули', 'хуя', 'хуи', 'ебись'
    ]

    SHS = [
        'саня хуй соси','хуй саня соси', 'соси хуй саня', 'схс', 'схс', 'сxс', 'сxc', 'сxс', 'сxс', 'сxc',
        'бот, скинь дз', 'саня пидор',

    ]

    rhythm ={
        ' Да ': 'Манда',
        ' да ': 'Манда',
        ' ДА ': 'Манда',
        'Да': 'Манда',
        'да': 'Манда',
        'ДА': 'Манда',
        ' Нет ': 'Пидора ответ',
        ' нет ': 'Пидора ответ',
        ' НЕТ ': 'Пидора ответ',
        'Нет': 'Пидора ответ',
        'нет': 'Пидора ответ',
        'НЕТ': 'Пидора ответ',
        ' ну ': 'Баранки гну',
        ' Ну ': 'Баранки гну',
        ' НУ ': 'Баранки гну',
        'ну': 'Баранки гну',
        'Ну': 'Баранки гну',
        'НУ': 'Баранки гну',
    }

    commands = {
        '!Пидор': 'chooseOneGay()',
        '!пидор': 'chooseOneGay()',
        '!ПИДОР': 'chooseOneGay()',
        '!ролл': 'getRandomNumber()',
        '!Ролл': 'getRandomNumber()',
        '!РОЛЛ': 'getRandomNumber()',
        '!дн': 'yesOrNo()',
        '!Дн': 'yesOrNo()',
        '!ДН': 'yesOrNo()',
        '!матан': 'getMATAN()',
        '!Матан': 'getMATAN()',
        '!МАТАН': 'getMATAN()',


    }

    nety = [
        'Нету'
    ]

    idS = {
        125116747:'Денис Авраменко', 139463233:'Даша Григорьева', 160015143:'Владислав Кухарев', 161047756:'Тимофей Машко', 163355437:'Надежда Дудачёва', 172095785:'Влад Сотников',
        175486984:'Александр Сибирцев', 176734676:'Полина Петроченко', 179124539:'Саша Буткевич', 183107358:'Александра Иванкович',
        184860650:'Георгий Черных', 194566360:'Илья Брехун', 205808093:'Иван Уткевич', 206688465:'Никон Кукар-Бухтияров', 209771910:'Мария Сафаралиева',
        221230319:'Кирилл Медведев', 260328935:'Кирилл Ярцев', 300429635:'Даниил Сорокин', 300960822:'Карина Орлова', 313545438:'Екатерина Вергель',
        398455414:'Ренат Валевич', 505809708:'Флоренсий Капитольевич'
    }

    idS2 = {
        125116747: 'Денис Авраменко', 139463233: 'Даша Григорьева', 160015143: 'Владислав Кухарев',
        161047756: 'Тимофей Машко', 163355437: 'Надежда Дудачёва', 172095785: 'Влад Сотников',
        175486984: 'Александр Сибирцев', 176734676: 'Полина Петроченко', 179124539: 'Саша Буткевич',
        183107358: 'Александра Иванкович',
        184860650: 'Георгий Черных', 194566360: 'Илья Брехун', 205808093: 'Иван Уткевич',
        206688465: 'Никон Кукар-Бухтияров', 209771910: 'Мария Сафаралиева',
        221230319: 'Кирилл Медведев', 260328935: 'Кирилл Ярцев', 300429635: 'Даниил Сорокин',
        300960822: 'Карина Орлова', 313545438: 'Екатерина Вергель',
        398455414: 'Ренат Валевич', 505809708: 'Флоренсий Капитольевич',
        339016009: 'Арина Мкртычян', 307714219: 'Екатерина Потапова'
    }


    login, password = 'x', 'x'
    vk_session = vk_api.VkApi(login, password, auth_handler=auth_handler)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    longpoll = VkLongPoll(vk_session, mode=2)


    for event in longpoll.listen():
        print('New event', event.type)

        if event.type == VkEventType.MESSAGE_NEW:
            print('Новое сообщение:')

            if event.from_me:
                print('От меня для: ', end = '')
            elif event.to_me:
                print('Для меня от: ', end = '')

            if event.from_user:
                print(event.user_id)
            elif event.from_chat:
                print(event.user_id, 'в беседе', event.chat_id)
            elif event.from_group:
                print('группы', event.group_id)

            print('Текст: ', event.text)
            print()

            messageText = str(event.text)


            def chooseOneGay():
                dict_members = vk_session.get_api().messages.getConversationMembers(peer_id=2000000072, fields='id')
                a1 = []
                for mass in dict_members['profiles']:
                    var1 = mass.get('id')
                    a1.append(var1)
                print (a1)
                random.shuffle(a1)
                lenghtA1 = len(a1)
                randomGay = random.randint(0, lenghtA1-1)
                randomGayNameAndSurename = idS.get(a1[randomGay])
                return randomGayNameAndSurename

            def getRandomNumber():
                randomNumber = random.randint(0, 100)
                return randomNumber

            def yesOrNo():
                randomYesOrNo = random.randint(0,1)
                if randomYesOrNo == 1:
                    return 'Да!'
                elif randomYesOrNo == 0:
                    return 'Нет!'

            def getMATAN():
                getMatanDic = vk_session.get_api().messages.getHistory(user_id=175486984,count=10)
                getMatanDic = getMatanDic.get('items')
                for i in getMatanDic:
                    if i.get('text') == str(datetime.datetime.now().day) + ' ' + 'МАТАН':
                        i = i.get('attachments')
                        i = i[0]
                        print (type(i))
                        typeAtt = i.get('type')
                        attIdDict = i.get('photo')
                        attOwnerId = attIdDict.get('owner_id')
                        attMediaId = attIdDict.get('id')
                        media = typeAtt+str(attOwnerId)+'_'+str(attMediaId)
                        return media


            def checBadWord(mtInner):
                mtInner = mtInner.lower()
                for i1 in bad_words:
                    ii1 = mtInner.find(i1)
                    if ii1 != -1 and event.user_id != 175486984:
                        return True

            def checBadWord2(mtInner):
                mtInner = mtInner.lower()
                for i1 in bad_words:
                    ii1 = mtInner.find(i1)
                    if ii1 != -1 and event.user_id != 175486984:
                        return i1

            def checkMaty(messageText):
                messageText = messageText.lower()
                for i2 in maty:
                    i2 = messageText.find(i2)
                    if i2 != -1 and event.user_id != 175486984:
                        return True

            def checkSHS(messageText):
                messageText = messageText.lower()
                for i3 in SHS:
                    i3 = messageText.find(i3)
                    if i3 != -1 and event.user_id != 175486984:
                        return True

            def chechRhythm():
                for i4 in rhythm:
                    if messageText == i4.lower() or messageText == i4.upper() or messageText == i4:
                        return True

            def checkCommands():
                for i5 in commands:
                    if messageText == i5.lower() or messageText == i5.upper() or messageText == i5:
                        return True
            def checkNety():
                for i6 in nety:
                    if messageText == i6.lower() or messageText == i6.upper() or messageText == i6:
                        return True

            if checkCommands() == True:
                if event.from_chat:
                    commandId = commands.get(messageText)
                    if commandId == 'chooseOneGay()':
                        vk_session.get_api().messages.send(chat_id=int(event.chat_id), message='Я думаю, что пидор: \n' + str(chooseOneGay()) +'\n'+'[ BOT // ' + ' ' +datetime.datetime.today().strftime("%Y-%m-%d, %H.%M.%S") +' ]')
                        continue
                    elif commandId == 'getRandomNumber()':
                        randomNumber = getRandomNumber()
                        vk_session.get_api().messages.send(chat_id=int(event.chat_id),message=str(randomNumber)+'\n'+'[ BOT // ' + ' ' +datetime.datetime.today().strftime("%Y-%m-%d, %H.%M.%S") +' ]')
                        continue
                    elif commandId == 'yesOrNo()':
                        randomYesOrNo = yesOrNo()
                        vk_session.get_api().messages.send(chat_id=int(event.chat_id), message=str(randomYesOrNo) + '\n' + '[ BOT // ' + ' ' + datetime.datetime.today().strftime("%Y-%m-%d, %H.%M.%S") + ' ]')
                        continue
                    elif commandId == 'getMATAN()':
                        attachMATAN = getMATAN()
                        vk_session.get_api().messages.send(chat_id=int(event.chat_id), message=str('Математика на сл. урок') + '\n' + '[ BOT // ' + ' ' + datetime.datetime.today().strftime("%Y-%m-%d, %H.%M.%S") + ' ]', attachment = str(attachMATAN))
                        continue
            elif checBadWord(messageText) == True:
                if event.from_user: #and str(event.user_id) != '175486984':
                    vk_session.get_api().messages.send(user_id=int(event.user_id), message='Сам ' +str(checBadWord2(messageText))+ '\n'+'[ BOT // ' + ' ' +datetime.datetime.today().strftime("%Y-%m-%d; %H.%M.%S") +' ]')
                    continue
                elif event.from_chat: # and str(event.user_id) != '175486984':
                    vk_session.get_api().messages.send(chat_id=int(event.chat_id), message='Сам ' + str(checBadWord2(messageText))+ '\n'+'[ BOT // ' + ' ' +datetime.datetime.today().strftime("%Y-%m-%d; %H.%M.%S") +' ]' )
                    continue
            elif checkMaty(messageText) == True:
                if event.from_user:# and str(event.user_id) != '175486984':
                    vk_session.get_api().messages.send(user_id=int(event.user_id), message='Не матерись!'+'\n'+'[ BOT // ' + ' ' +datetime.datetime.today().strftime("%Y-%m-%d, %H.%M.%S") +' ]')
                    continue
                elif event.from_chat:# and str(event.user_id) != '175486984':
                    vk_session.get_api().messages.send(chat_id=int(event.chat_id), message='Не матерись!'+'\n'+'[ BOT // ' + ' ' +datetime.datetime.today().strftime("%Y-%m-%d, %H.%M.%S") +' ]')
                    continue
            elif messageText == 'КОД КРАСНЫЙ 228':
                if event.from_user and str(event.user_id) == '175486984':
                    sys.exit()
            elif checkSHS(messageText) == True:
                if event.from_chat and str(event.user_id) != '175486984':
                    vk_session.get_api().messages.send(chat_id=int(event.chat_id),attachment='photo175486984_456242877')
                    vk_session.get_api().messages.removeChatUser(chat_id=int(event.chat_id),user_id=int(event.user_id))
                    continue
            elif chechRhythm() == True:
                if event.from_chat:
                    vk_session.get_api().messages.send(chat_id=int(event.chat_id), message=str(rhythm.get(messageText))+'\n'+'[ BOT // ' + ' ' +datetime.datetime.today().strftime("%Y-%m-%d, %H.%M.%S") +' ]')
                    continue



        #elif event.type == VkEventType.MESSAGE_EDIT:
            #if event.from_chat:
                #vk_session.get_api().messages.send(chat_id=int(event.chat_id), message=str(idS2.get(event.user_id))+ ' отредактировал сообщение \n' + '[ BOT // ' + ' ' + datetime.datetime.today().strftime("%Y-%m-%d; %H.%M.%S") + ' ]')
        #elif event.type == VkEventType.MESSAGE_FLAGS_SET:
            #if event.from_chat:
                #if event.mask == 131200:
                    #vk_session.get_api().messages.send(chat_id=int(event.chat_id), message='Кто-то удалил сообщение 😑\n' + '[ BOT // ' + ' ' + datetime.datetime.today().strftime("%Y-%m-%d; %H.%M.%S") + ' ]')


if __name__ == '__main__':
    main()
