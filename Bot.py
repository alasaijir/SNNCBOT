import vk_api, random, sys, datetime
from vk_api.longpoll import VkLongPoll, VkEventType

def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = True

    return key, remember_device

def main():
    bad_words = [
        'Пидор', 'Ты пидор', 'Ти пидор',
        'Пэдро', 'Ты пэдро', 'Ти пэдро',
        'Пыдар', 'Ты пыдар', 'Ти пыдар',
        'Пидр', 'Ты пидр', 'Ти пидр',
        'Ты пизда', 'Ти пизда',
        'Пидорас', 'Ты пидорас', 'Ти пидорас',
        'Тварь', 'Ты тварь', 'Ти тварь',
        'Говно', 'Ты говно', 'Ти говно',
        'Ты сука', 'Ти сука',
        'Член','Ты член', 'Ти член',
        'Даун', 'Ты даун', 'Ти даун',
        'Аутист', 'Ты аутист', 'Ти аутист',
        'Долбаеб', 'Ты долбаеб', 'Ти долбаеб',
        'Долбаёб', 'Ты долбаёб', 'Ти долбаёб',
        'Долбоеб', 'Ты долбоеб', 'Ти долбоеб',
        'Долбоёб', 'Ты долбоёб', 'Ти долбоёб',
        'Говноед', 'Ты говноед', 'Ти говноед',
        'Ты блядь', 'Ти блядь',
        'Ты блять', 'Ти блять',
        'Пошел нахуй', 'Пошел ты нахуй', 'Иди нахуй', 'Иди на хуй', 'Пошел на хуй',
        'Ты хуй', 'Ти хуй',
        'Иди в пизду', 'Пошел в пизду',
        'Гей', 'Ты гей', 'Ти гей',
        'Чмо', 'Ты чмо', 'Ти чмо',
        'Чьмо', 'Ты чьмо', 'Ти чьмо',
        'Лох', 'Ты лох', 'Ти лох',
        'Соси',
    ]

    maty = [
        'Хуй', 'Залупа', 'Пизда', 'Ебать', 'Ебал', 'Ебаный', 'Ебанный', 'Ебал в рот', 'Ебаный рот', 'Ебанный рот', 'В пизду','Блять','Блядь','Бля', 'Ублюдок мать твою',
        'Сука', 'Похуй',
    ]

    SHS = [
        'Саня хуй соси','Хуй саня соси', 'Соси хуй саня', 'Схс', 'Cхс', 'Cxс', 'Cxc', 'Сxс', 'Cxс', 'Сxc',
        'Бот, скинь дз', 'Саня пидор',

    ]

    rhythm ={
        'Да': 'Борода',
        'да': 'Борода',
        'ДА': 'Борода',
        'Нет': 'Пидора ответ',
        'нет': 'Пидора ответ',
        'НЕТ': 'Пидора ответ',
    }

    commands = {
        '!Пидор': 'chooseOneGay()',
        '!пидор': 'chooseOneGay()',
        '!ПИДОР': 'chooseOneGay()',
        '!ролл': 'getRandomNumber()',
        '!Ролл': 'getRandomNumber()',
        '!РОЛЛ': 'getRandomNumber()',

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

    longpoll = VkLongPoll(vk_session)


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


            def checBadWord():
                for i1 in bad_words:
                    if messageText == i1.lower() or messageText == i1.upper() or messageText == i1:
                        return True

            def checkMaty():
                for i2 in maty:
                    if messageText == i2.lower() or messageText == i2.upper() or messageText == i2:
                        return True

            def checkSHS():
                for i3 in SHS:
                    if messageText == i3.lower() or messageText == i3.upper() or messageText == i3:
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


            if checBadWord() == True:
                if event.from_user and str(event.user_id) != '175486984':
                    vk_session.get_api().messages.send(user_id=int(event.user_id), message='Сам ' +str(event.text).lower()+ '\n'+'[ BOT // ' + ' ' +datetime.datetime.today().strftime("%Y-%m-%d; %H.%M.%S") +' ]')
                elif event.from_chat and str(event.user_id) != '175486984':
                    vk_session.get_api().messages.send(chat_id=int(event.chat_id), message='Сам ' + str(event.text).lower()+ '\n'+'[ BOT // ' + ' ' +datetime.datetime.today().strftime("%Y-%m-%d; %H.%M.%S") +' ]' )
            elif checkMaty() == True:
                if event.from_user and str(event.user_id) != '175486984':
                    vk_session.get_api().messages.send(user_id=int(event.user_id), message='Не матерись, а то будет'+'\n \n'+'[ BOT // ' + ' ' +datetime.datetime.today().strftime("%Y-%m-%d, %H.%M.%S") +' ]', attachment='photo175486984_456242876')
                elif event.from_chat and str(event.user_id) != '175486984':
                    vk_session.get_api().messages.send(chat_id=int(event.chat_id), message='Не матерись, а то будет'+'\n \n'+'[ BOT // ' + ' ' +datetime.datetime.today().strftime("%Y-%m-%d, %H.%M.%S") +' ]', attachment='photo175486984_456242876')
            elif messageText == 'КОД КРАСНЫЙ 228':
                if event.from_user and str(event.user_id) == '175486984':
                    sys.exit()
            elif checkSHS() == True:
                if event.from_chat and str(event.user_id) != '175486984':
                    vk_session.get_api().messages.removeChatUser(chat_id=int(event.chat_id),user_id=int(event.user_id))
                    vk_session.get_api().messages.send(chat_id=int(event.chat_id),attachment='photo175486984_456242877')
            elif chechRhythm() == True:
                if event.from_chat:
                    vk_session.get_api().messages.send(chat_id=int(event.chat_id), message=str(rhythm.get(messageText))+'\n'+'[ BOT // ' + ' ' +datetime.datetime.today().strftime("%Y-%m-%d; %H.%M.%S") +' ]')
            elif checkNety() == True:
                if event.from_user and str(event.user_id) != '175486984':
                    vk_session.get_api().messages.send(user_id=int(event.user_id),message='Нет слова нету...' + '\n ' + '[ BOT // ' + ' ' + datetime.datetime.today().strftime( "%Y-%m-%d, %H.%M.%S") + ' ]')
                elif event.from_chat and str(event.user_id) != '175486984':
                    vk_session.get_api().messages.send(chat_id=int(event.chat_id), message='Нет слова нету...' + '\n ' + '[ BOT // ' + ' ' + datetime.datetime.today().strftime("%Y-%m-%d, %H.%M.%S") + ' ]')
            elif checkCommands() == True:
                if event.from_chat:
                    commandId = commands.get(messageText)
                    if commandId == 'chooseOneGay()':
                        vk_session.get_api().messages.send(chat_id=int(event.chat_id), message='Я думаю, что пидор: \n' + str(chooseOneGay()) +'\n'+'[ BOT // ' + ' ' +datetime.datetime.today().strftime("%Y-%m-%d; %H.%M.%S") +' ]')
                    elif commandId == 'getRandomNumber()':
                        randomNumber = getRandomNumber()
                        vk_session.get_api().messages.send(chat_id=int(event.chat_id),message=str(randomNumber)+'\n'+'[ BOT // ' + ' ' +datetime.datetime.today().strftime("%Y-%m-%d; %H.%M.%S") +' ]')
        elif event.type == VkEventType.MESSAGE_EDIT:
            if event.from_chat:
                vk_session.get_api().messages.send(chat_id=int(event.chat_id), message=str(idS2.get(event.user_id))+ ' отредактировал сообщение \n' + '[ BOT // ' + ' ' + datetime.datetime.today().strftime("%Y-%m-%d; %H.%M.%S") + ' ]')
        elif event.type == VkEventType.MESSAGE_FLAGS_SET:
            if event.from_chat:
                if event.mask == 131200:
                    vk_session.get_api().messages.send(chat_id=int(event.chat_id), message='Кто-то удалил сообщение 😑\n' + '[ BOT // ' + ' ' + datetime.datetime.today().strftime("%Y-%m-%d; %H.%M.%S") + ' ]')


if __name__ == '__main__':
    main()
