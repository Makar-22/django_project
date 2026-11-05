from django.shortcuts import render
from random import randint
import random
commonoutput=[]
commonlist=['Доспех быстрого снятия','Дымящий доспех','Наручный клинок','Несломимая стрела','Опрокидывающий боеприпас','Осенённый луной меч','Сверкающий доспех','Щит экспрессии']
uncommonlist=['Адамантиновый доспех',

'Адское оружие',

'Грозовой бумеранг',

'Доспех грибковых спор',

'Доспех из змеиной чешуи',

'Доспех моряка',

'Доспехи невесомости',

'Доспехи падшего',

'Дротик-искатель',

'Кольцо затуманивания',

'Кольцо защиты разума',

'Кольцо оратора',

'Кольцо остроумия Головоломщика',

'Кольцо плавания',

'Кольцо правды',

'Кольцо прыжков',

'Кольцо тепла',

'Кольцо хождения по воде',

'Кровавое копьё',

'Крылатые боеприпасы',

'Латы Рыцарского Братства',

'Мифрильная кольчужная рубаха Ванрака',

'Мифрильный доспех',

'Метательное копьё молнии',

'Меч мести',

'Оружие предупреждения',

'Печатка гильдии Азориус',

'Печатка гильдии Бороса',

'Печатка гильдии Голгари',

'Печатка гильдии Груул',

'Печатка гильдии Димир',
'Печатка гильдии Иззет',

'Печатка гильдии Орзова',
'Печатка гильдии Ракдоса',
'Печатка гильдии Селезнии',

'Печатка гильдии Симиков',

'Панцирный доспех разума',

'Праща ниспровержения великанов',

'Разрушающее остриё',

'Рассекатель',
'Реззур',

'Светоносная',

'Секира кровавой ярости',

'Сушёная пиявка',

'Тёмный укус зимы',

'Трезубец командования рыбами',

'Щит часового',

'Щит черепахи',

'Щит-бумеранг']
rarelist=['Арбалет звёздострел',

'Бедренная кость святой Марковии',

'Булава кары',

'Булава распада',

'Булава ужаса',

'Гроза свежевателей',

'Доспех Зефира',

'Доспех сопротивления',

'Доспех странника пустоты',

'Доспех уязвимости',

'Доспехи Мрака',

'Доспехи фей',

'Драконий страж',

'Жестокая рапира +1',

'Жестокое оружие',

'Змеиный клык',

'Игла починки',

'Кольцо влияния на животных',

'Кольцо временного спасения',

'Кольцо защиты',

'Кольцо падения пёрышком',

'Кольцо проникающего зрения',

'Кольцо свободных действий',

'Кольцо сопротивления',

'Кольцо тарана',

'Кольцо уклонения',

'Кольцо хранения заклинаний',

'Кираса Баланса',

'Кожаный доспех голема',

'Красивый проклёпанный кожаный доспех',

'Кадило фанатика',

'Кинжал драконьего зуба',

'Кинжал слепого зрения',

'Кинжал яда',

'Клинок Ахерона',

'Клинок игрока',

'Клинок разума',

'Крыло дракона',

'Ловящий стрелы щит',

'Лук Воспламенения',

'Миззиевый доспех',

'Мифрильные полулаты +1',

'Меч кражи жизни',

'Меч ранения',

'Оружие неминуемой гибели',

'Плеть жертвоприношения',

'Плеть разума',

'Праща двух зайцев',

'Пронзатель',

'Расплавленная бронзовая кожа',

'Разрушающий цеп',
'Сверкающий Лунный Лук',

'Сияющий клевец',

'Солнечный клинок',

'Солнечный молот',

'Счётчик костей',
'Таранный щит',

'Топор берсерка',

'Топор дровосека',

'Убийца великанов',

'Убийца драконов',

'Убийца мертвецов',

'Хватающий кнут',

'Хрустальный клинок',

'Шкура демона',

'Щит Дальнего Взора',

'Щит Парии',

'Щит притягивания снарядов',

'Эльфийская кольчуга',
'Язык пламени']
unrarelist=['Боевая кирка камнетворца',

'Боеприпасы кровавого искателя',

'Вор девяти жизней',

'Громобой',

'Демонический доспех',

'Доспех Антимагии',

'Доспех защиты',

'Доспех из драконьей чешуи',

'Доспех наемника Хеварда',

'Доспех последней битвы',

'Дварфский метатель',

'Живой доспех',

'Живой щит',

'Заводные доспехи,'

'Зловещий Коготь',

'Кольцо дружелюбия',

'Кольцо красной ярости',

'Кольцо падающих звёзд',

'Кольцо регенерации',

'Кольцо телекинеза',

'Клинок дурака',

'Клинок кровопролития',
'Клинок Медузы',

'Клинок превращения',

'Кнут–щупальце Диррна',

'Копьё злословия',

'Кровавый топор',

'Латы дварфов',

'Лук клятвы',

'Лук мелодий',

'Меч остроты',

'Меч отцов',

'Молот рунного фокуса',

'Морозный клинок',

'Ножницы отсекающие судьбу',

'Охотничье пальто',

'Оружие повеления Трона',

'Оружие разрушения силы',

'Рогатое кольцо',

'Руидиевый доспех',

'Руидиевый щит',

'Руидиевое оружие',

'Сапфировый баклер',

'Светящийся Разрушитель',

'Скимитар скорости',

'Снаряды Альтемоны для пращи',

'Сокрушитель сумерек',

'Сталь',

'Стрела убийства',

'Танцующий меч',

'Тиарулай',

'Трезубец зова приливов',

'Щит от заклинаний',

'Щит с руной Увен',
'Эльфийский метатель']
legendarylist=['Взы-взы',

'Волна',

'Высекающий искры',

'Вэйз',

'Доспех неуязвимости',

'Двуручный серебряный меч',

'Длинный лук исцеляющего очага',

'Драконье копьё',

'Еретик',

'Железный клык',

'Закладка',

'Защитник',

'Кольцо командования элементалями',

'Кольцо невидимости',

'Кольцо отражения заклинаний',

'Кольцо призыва джинна',

'Кольцо трёх желаний',

'Кираса камнелома',

'Кольчуга ифритов',

'Клинок Красного Волшебника',

'Клинок удачи',

'Крик Жнеца',

'Латный доспех эфирности',

'Лазурное лезвие',

'Лунный клинок',

'Маталоток',

'Меч гибели',

'Меч головоруб',

'Меч ответа',

'Меч Плановых Измерений',

'Молот грома',
'Непенте',

'Несущая Рассвет',

'Обсидианово-кремневые латы дракона',

'Перст ветра',

'Приносящая ночь',

'Рассекатель орков',

'Ритуальный нож Ракдосов',

'Силовой доспех',

'Святой мститель',

'Секира Гурта',

'Сокрушитель',

'Солнечный меч',

'Топазовый аннигилятор',

'Топитель',

'Хазирун',

'Храмовый пожиратель',

'Цеп Тиамат',

'Чёрный клинок',

'Шкура дикого стража',

'Щит пылающего дредноута',

'Щит скрытого лорда',

'Эгида Эвриаллы']
artifactlist=['Акмон, молот Пирфора',

'Булава черной короны',

'Воля когтя',

'Декелла, двузубец Тассы',

'Кольцо зимы',

'Клинок Авернуса',

'Клинок разбитых зеркал',

'Кровавая смерть',

'Крусор, копьё Гелиода',

'Мастикс, кнут Эреба',

'Меч Зариэли',

'Меч Каса',

'Плеть теней',

'Ползучий молотильщик',

'Сеющий разорение',

'Тесло Аннама',

'Топор владык дварфов',

'Шелковая ненависть',

'Эфиксида, лук Нилеи']
def index(request):
    a=randint(1,20)
    return render(request,'main/main_page.html',{'money':a} )

def about(request):
    return render(request,'main/about.html')
def catalog(request):
    return render(request,'main/catalog.html')
def game(request):
    return render(request, 'main/game.html')
def level1(request):
    money1=randint(100,3000)
    common=randint(0,2)
    uncommon=randint(0,1)
    rare=0
    epic=0
    legendary=0
    artifact=0
    #common 7#
    if common>=1:
     numm1=randint(0,7)
     commonart1=commonlist[numm1]
    else:
          commonart1='Обычные предметы отсутствуют'
    if common>=2:
     numm2=randint(0,7)
     commonart2=commonlist[numm2]
    else:
          commonart2=''
    if common>=3:
     numm3=randint(0,7)
     commonart3=commonlist[numm3]
    else:
          commonart3=''
    if common>=4:
     numm4=randint(0,7)
     commonart4=commonlist[numm4]
    else:
          commonart4=''
    #uncommon 48#
    if uncommon>=1:
     numm1=randint(0,48)
     uncommonart1=uncommonlist[numm1]
    else:
          uncommonart1='Необычные предметы отсутствуют'
    if uncommon>=2:
     numm2=randint(0,48)
     uncommonart2=uncommonlist[numm2]
    else:
          uncommonart2=''
    if uncommon>=3:
     numm3=randint(0,48)
     uncommonart3=uncommonlist[numm3]
    else:
          uncommonart3=''
    if uncommon>=4:
     numm4=randint(0,48)
     uncommonart4=uncommonlist[numm4]
    else:
          uncommonart4=''
    #rare 68#
    if rare>=1:
     numm1=randint(0,68)
     rareart1=rarelist[numm1]
    else:
          rareart1='Редкие предметы отсутствуют'
    if rare>=2:
     numm2=randint(0,68)
     rareart2=rarelist[numm2]
    else:
          rareart2=''
    if rare>=3:
     numm3=randint(0,68)
     rareart3=rarelist[numm3]
    else:
          rareart3=''
    if rare>=4:
     numm4=randint(0,68)
     rareart4=rarelist[numm4]
    else:
          rareart4=''
          #unrare(epic) 53#
    if epic>=1:
     numm1=randint(0,53)
     unrareart1=unrarelist[numm1]
    else:
          unrareart1='Сверхедкие предметы отсутствуют'
    if epic>=2:
     numm2=randint(0,53)
     unrareart2=unrarelist[numm2]
    else:
          unrareart2=''
    if epic>=3:
     numm3=randint(0,53)
     unrareart3=unrarelist[numm3]
    else:
          unrareart3=''
    if epic>=4:
     numm4=randint(0,53)
     unrareart4=unrarelist[numm4]
    else:
          unrareart4=''
    #legendary 52#
    if legendary>=1:
     numm1=randint(0,52)
     legendaryart1=legendarylist[numm1]
    else:
          legendaryart1='Легендарные предметы отсутствуют'
    if legendary>=2:
     numm2=randint(0,52)
     legendaryart2=legendarylist[numm2]
    else:
          legendaryart2=''
    if legendary>=3:
     numm3=randint(0,52)
     legendaryart3=legendarylist[numm3]
    else:
          legendaryart3=''
    if legendary>=4:
     numm4=randint(0,52)
     legendaryart4=legendarylist[numm4]
    else:
          legendaryart4=''
    #artifact 18#
    if artifact>=1:
     numm1=randint(0,18)
     artifactart1=artifactlist[numm1]
    else:
          artifactart1='Предметы редкости "Артефакт" отсутствуют'
    if artifact>=2:
     numm2=randint(0,18)
     artifactart2=artifactlist[numm2]
    else:
          artifactart2=''
    if artifact>=3:
     numm3=randint(0,18)
     artifactart3=artifactlist[numm3]
    else:
          artifactart3=''
    if artifact>=4:
     numm4=randint(0,18)
     artifactart4=artifactlist[numm4]
    else:
          artifactart4=''
    data={
        'money1':money1,
        'commonart1':commonart1,
        'commonart2':commonart2,
        'commonart3':commonart3,
        'commonart4':commonart4,
        'uncommonart1':uncommonart1,
        'uncommonart2':uncommonart2,
        'uncommonart3':uncommonart3,
        'uncommonart4':uncommonart4,
        'rareart1':rareart1,
        'rareart2':rareart2,
        'rareart3':rareart3,
        'rareart4':rareart4,
        'unrareart1':unrareart1,
        'unrareart2':unrareart2,
        'unrareart3':unrareart3,
        'unrareart4':unrareart4,
        'legendaryart1':legendaryart1,
        'legendaryart2':legendaryart2,
        'legendaryart3':legendaryart3,
        'legendaryart4':legendaryart4,
        'artifactart1':artifactart1,
        'artifactart2':artifactart2,
        'artifactart3':artifactart3,
        'artifactart4':artifactart4,
    }
    return render(request,'main/lvl_shablon.html' , data)
def level2(request):
    money1=randint(200,3500)
    common=randint(0,3)
    uncommon=randint(0,1)
    rare=randint(0,1)
    epic=0
    legendary=0
    artifact=0
    #common#
    if common>=1:
     numm1=randint(0,7)
     commonart1=commonlist[numm1]
    else:
          commonart1='Обычные предметы отсутствуют'
    if common>=2:
     numm2=randint(0,7)
     commonart2=commonlist[numm2]
    else:
          commonart2=''
    if common>=3:
     numm3=randint(0,7)
     commonart3=commonlist[numm3]
    else:
          commonart3=''
    if common>=4:
     numm4=randint(0,7)
     commonart4=commonlist[numm4]
    else:
          commonart4=''
    #uncommon#
    if uncommon>=1:
     numm1=randint(0,48)
     uncommonart1=uncommonlist[numm1]
    else:
          uncommonart1='Необычные предметы отсутствуют'
    if uncommon>=2:
     numm2=randint(0,48)
     uncommonart2=uncommonlist[numm2]
    else:
          uncommonart2=''
    if uncommon>=3:
     numm3=randint(0,48)
     uncommonart3=uncommonlist[numm3]
    else:
          uncommonart3=''
    if uncommon>=4:
     numm4=randint(0,48)
     uncommonart4=uncommonlist[numm4]
    else:
          uncommonart4=''
    #rare#
    if rare>=1:
     numm1=randint(0,68)
     rareart1=rarelist[numm1]
    else:
          rareart1='Редкие предметы отсутствуют'
    if rare>=2:
     numm2=randint(0,68)
     rareart2=rarelist[numm2]
    else:
          rareart2=''
    if rare>=3:
     numm3=randint(0,68)
     rareart3=rarelist[numm3]
    else:
          rareart3=''
    if rare>=4:
     numm4=randint(0,68)
     rareart4=rarelist[numm4]
    else:
          rareart4=''
          #unrare(epic)#
    if epic>=1:
     numm1=randint(0,53)
     unrareart1=unrarelist[numm1]
    else:
          unrareart1='Сверхедкие предметы отсутствуют'
    if epic>=2:
     numm2=randint(0,53)
     unrareart2=unrarelist[numm2]
    else:
          unrareart2=''
    if epic>=3:
     numm3=randint(0,53)
     unrareart3=unrarelist[numm3]
    else:
          unrareart3=''
    if epic>=4:
     numm4=randint(0,53)
     unrareart4=unrarelist[numm4]
    else:
          unrareart4=''
    #legendary#
    if legendary>=1:
     numm1=randint(0,52)
     legendaryart1=legendarylist[numm1]
    else:
          legendaryart1='Легендарные предметы отсутствуют'
    if legendary>=2:
     numm2=randint(0,52)
     legendaryart2=legendarylist[numm2]
    else:
          legendaryart2=''
    if legendary>=3:
     numm3=randint(0,52)
     legendaryart3=legendarylist[numm3]
    else:
          legendaryart3=''
    if legendary>=4:
     numm4=randint(0,52)
     legendaryart4=legendarylist[numm4]
    else:
          legendaryart4=''
    #artifact#
    if artifact>=1:
     numm1=randint(0,18)
     artifactart1=artifactlist[numm1]
    else:
          artifactart1='Предметы редкости "Артефакт" отсутствуют'
    if artifact>=2:
     numm2=randint(0,18)
     artifactart2=artifactlist[numm2]
    else:
          artifactart2=''
    if artifact>=3:
     numm3=randint(0,18)
     artifactart3=artifactlist[numm3]
    else:
          artifactart3=''
    if artifact>=4:
     numm4=randint(0,18)
     artifactart4=artifactlist[numm4]
    else:
          artifactart4=''
    data={
        'money1':money1,
        'commonart1':commonart1,
        'commonart2':commonart2,
        'commonart3':commonart3,
        'commonart4':commonart4,
        'uncommonart1':uncommonart1,
        'uncommonart2':uncommonart2,
        'uncommonart3':uncommonart3,
        'uncommonart4':uncommonart4,
        'rareart1':rareart1,
        'rareart2':rareart2,
        'rareart3':rareart3,
        'rareart4':rareart4,
        'unrareart1':unrareart1,
        'unrareart2':unrareart2,
        'unrareart3':unrareart3,
        'unrareart4':unrareart4,
        'legendaryart1':legendaryart1,
        'legendaryart2':legendaryart2,
        'legendaryart3':legendaryart3,
        'legendaryart4':legendaryart4,
        'artifactart1':artifactart1,
        'artifactart2':artifactart2,
        'artifactart3':artifactart3,
        'artifactart4':artifactart4,
    }
    return render(request,'main/lvl_shablon.html' , data)
def level3(request):
    money1=randint(300,4000)
    common=randint(0,3)
    uncommon=randint(0,2)
    rare=randint(0,1)
    epic=0
    legendary=0
    artifact=0
    #common#
    if common>=1:
     numm1=randint(0,7)
     commonart1=commonlist[numm1]
    else:
          commonart1='Обычные предметы отсутствуют'
    if common>=2:
     numm2=randint(0,7)
     commonart2=commonlist[numm2]
    else:
          commonart2=''
    if common>=3:
     numm3=randint(0,7)
     commonart3=commonlist[numm3]
    else:
          commonart3=''
    if common>=4:
     numm4=randint(0,7)
     commonart4=commonlist[numm4]
    else:
          commonart4=''
    #uncommon#
    if uncommon>=1:
     numm1=randint(0,48)
     uncommonart1=uncommonlist[numm1]
    else:
          uncommonart1='Необычные предметы отсутствуют'
    if uncommon>=2:
     numm2=randint(0,48)
     uncommonart2=uncommonlist[numm2]
    else:
          uncommonart2=''
    if uncommon>=3:
     numm3=randint(0,48)
     uncommonart3=uncommonlist[numm3]
    else:
          uncommonart3=''
    if uncommon>=4:
     numm4=randint(0,48)
     uncommonart4=uncommonlist[numm4]
    else:
          uncommonart4=''
    #rare#
    if rare>=1:
     numm1=randint(0,68)
     rareart1=rarelist[numm1]
    else:
          rareart1='Редкие предметы отсутствуют'
    if rare>=2:
     numm2=randint(0,68)
     rareart2=rarelist[numm2]
    else:
          rareart2=''
    if rare>=3:
     numm3=randint(0,68)
     rareart3=rarelist[numm3]
    else:
          rareart3=''
    if rare>=4:
     numm4=randint(0,68)
     rareart4=rarelist[numm4]
    else:
          rareart4=''
          #unrare(epic)#
    if epic>=1:
     numm1=randint(0,53)
     unrareart1=unrarelist[numm1]
    else:
          unrareart1='Сверхедкие предметы отсутствуют'
    if epic>=2:
     numm2=randint(0,53)
     unrareart2=unrarelist[numm2]
    else:
          unrareart2=''
    if epic>=3:
     numm3=randint(0,53)
     unrareart3=unrarelist[numm3]
    else:
          unrareart3=''
    if epic>=4:
     numm4=randint(0,53)
     unrareart4=unrarelist[numm4]
    else:
          unrareart4=''
    #legendary#
    if legendary>=1:
     numm1=randint(0,52)
     legendaryart1=legendarylist[numm1]
    else:
          legendaryart1='Легендарные предметы отсутствуют'
    if legendary>=2:
     numm2=randint(0,52)
     legendaryart2=legendarylist[numm2]
    else:
          legendaryart2=''
    if legendary>=3:
     numm3=randint(0,52)
     legendaryart3=legendarylist[numm3]
    else:
          legendaryart3=''
    if legendary>=4:
     numm4=randint(0,52)
     legendaryart4=legendarylist[numm4]
    else:
          legendaryart4=''
    #artifact#
    if artifact>=1:
     numm1=randint(0,18)
     artifactart1=artifactlist[numm1]
    else:
          artifactart1='Предметы редкости "Артефакт" отсутствуют'
    if artifact>=2:
     numm2=randint(0,18)
     artifactart2=artifactlist[numm2]
    else:
          artifactart2=''
    if artifact>=3:
     numm3=randint(0,18)
     artifactart3=artifactlist[numm3]
    else:
          artifactart3=''
    if artifact>=4:
     numm4=randint(0,18)
     artifactart4=artifactlist[numm4]
    else:
          artifactart4=''
    data={
        'money1':money1,
        'commonart1':commonart1,
        'commonart2':commonart2,
        'commonart3':commonart3,
        'commonart4':commonart4,
        'uncommonart1':uncommonart1,
        'uncommonart2':uncommonart2,
        'uncommonart3':uncommonart3,
        'uncommonart4':uncommonart4,
        'rareart1':rareart1,
        'rareart2':rareart2,
        'rareart3':rareart3,
        'rareart4':rareart4,
        'unrareart1':unrareart1,
        'unrareart2':unrareart2,
        'unrareart3':unrareart3,
        'unrareart4':unrareart4,
        'legendaryart1':legendaryart1,
        'legendaryart2':legendaryart2,
        'legendaryart3':legendaryart3,
        'legendaryart4':legendaryart4,
        'artifactart1':artifactart1,
        'artifactart2':artifactart2,
        'artifactart3':artifactart3,
        'artifactart4':artifactart4,
    }
    return render(request,'main/lvl_shablon.html' , data)
def level4(request):
    money1=randint(500,4300)
    common=randint(0,4)
    uncommon=randint(0,2)
    rare=randint(0,1)
    epic=0
    legendary=0
    artifact=0
    #common#
    if common>=1:
     numm1=randint(0,7)
     commonart1=commonlist[numm1]
    else:
          commonart1='Обычные предметы отсутствуют'
    if common>=2:
     numm2=randint(0,7)
     commonart2=commonlist[numm2]
    else:
          commonart2=''
    if common>=3:
     numm3=randint(0,7)
     commonart3=commonlist[numm3]
    else:
          commonart3=''
    if common>=4:
     numm4=randint(0,7)
     commonart4=commonlist[numm4]
    else:
          commonart4=''
    #uncommon#
    if uncommon>=1:
     numm1=randint(0,48)
     uncommonart1=uncommonlist[numm1]
    else:
          uncommonart1='Необычные предметы отсутствуют'
    if uncommon>=2:
     numm2=randint(0,48)
     uncommonart2=uncommonlist[numm2]
    else:
          uncommonart2=''
    if uncommon>=3:
     numm3=randint(0,48)
     uncommonart3=uncommonlist[numm3]
    else:
          uncommonart3=''
    if uncommon>=4:
     numm4=randint(0,48)
     uncommonart4=uncommonlist[numm4]
    else:
          uncommonart4=''
    #rare#
    if rare>=1:
     numm1=randint(0,68)
     rareart1=rarelist[numm1]
    else:
          rareart1='Редкие предметы отсутствуют'
    if rare>=2:
     numm2=randint(0,68)
     rareart2=rarelist[numm2]
    else:
          rareart2=''
    if rare>=3:
     numm3=randint(0,68)
     rareart3=rarelist[numm3]
    else:
          rareart3=''
    if rare>=4:
     numm4=randint(0,68)
     rareart4=rarelist[numm4]
    else:
          rareart4=''
          #unrare(epic)#
    if epic>=1:
     numm1=randint(0,53)
     unrareart1=unrarelist[numm1]
    else:
          unrareart1='Сверхедкие предметы отсутствуют'
    if epic>=2:
     numm2=randint(0,53)
     unrareart2=unrarelist[numm2]
    else:
          unrareart2=''
    if epic>=3:
     numm3=randint(0,53)
     unrareart3=unrarelist[numm3]
    else:
          unrareart3=''
    if epic>=4:
     numm4=randint(0,53)
     unrareart4=unrarelist[numm4]
    else:
          unrareart4=''
    #legendary#
    if legendary>=1:
     numm1=randint(0,52)
     legendaryart1=legendarylist[numm1]
    else:
          legendaryart1='Легендарные предметы отсутствуют'
    if legendary>=2:
     numm2=randint(0,52)
     legendaryart2=legendarylist[numm2]
    else:
          legendaryart2=''
    if legendary>=3:
     numm3=randint(0,52)
     legendaryart3=legendarylist[numm3]
    else:
          legendaryart3=''
    if legendary>=4:
     numm4=randint(0,52)
     legendaryart4=legendarylist[numm4]
    else:
          legendaryart4=''
    #artifact#
    if artifact>=1:
     numm1=randint(0,18)
     artifactart1=artifactlist[numm1]
    else:
          artifactart1='Предметы редкости "Артефакт" отсутствуют'
    if artifact>=2:
     numm2=randint(0,18)
     artifactart2=artifactlist[numm2]
    else:
          artifactart2=''
    if artifact>=3:
     numm3=randint(0,18)
     artifactart3=artifactlist[numm3]
    else:
          artifactart3=''
    if artifact>=4:
     numm4=randint(0,18)
     artifactart4=artifactlist[numm4]
    else:
          artifactart4=''
    data={
        'money1':money1,
        'commonart1':commonart1,
        'commonart2':commonart2,
        'commonart3':commonart3,
        'commonart4':commonart4,
        'uncommonart1':uncommonart1,
        'uncommonart2':uncommonart2,
        'uncommonart3':uncommonart3,
        'uncommonart4':uncommonart4,
        'rareart1':rareart1,
        'rareart2':rareart2,
        'rareart3':rareart3,
        'rareart4':rareart4,
        'unrareart1':unrareart1,
        'unrareart2':unrareart2,
        'unrareart3':unrareart3,
        'unrareart4':unrareart4,
        'legendaryart1':legendaryart1,
        'legendaryart2':legendaryart2,
        'legendaryart3':legendaryart3,
        'legendaryart4':legendaryart4,
        'artifactart1':artifactart1,
        'artifactart2':artifactart2,
        'artifactart3':artifactart3,
        'artifactart4':artifactart4,
    }
    
    return render(request,'main/lvl_shablon.html' , data)
def level5(request):
    money1=randint(4000,10000)
    common=randint(1,4)
    uncommon=randint(1,2)
    rare=randint(1,1)
    epic=0
    legendary=0
    artifact=0
    chance=randint(1,100)
    if chance>30 and chance<63:
            epic=1
    if chance>30 and chance<41:
            legendary=1
    if chance==50:
            artifact=1
    #common#
    if common>=1:
     numm1=randint(0,7)
     commonart1=commonlist[numm1]
    else:
          commonart1='Обычные предметы отсутствуют'
    if common>=2:
     numm2=randint(0,7)
     commonart2=commonlist[numm2]
    else:
          commonart2=''
    if common>=3:
     numm3=randint(0,7)
     commonart3=commonlist[numm3]
    else:
          commonart3=''
    if common>=4:
     numm4=randint(0,7)
     commonart4=commonlist[numm4]
    else:
          commonart4=''
    #uncommon#
    if uncommon>=1:
     numm1=randint(0,48)
     uncommonart1=uncommonlist[numm1]
    else:
          uncommonart1='Необычные предметы отсутствуют'
    if uncommon>=2:
     numm2=randint(0,48)
     uncommonart2=uncommonlist[numm2]
    else:
          uncommonart2=''
    if uncommon>=3:
     numm3=randint(0,48)
     uncommonart3=uncommonlist[numm3]
    else:
          uncommonart3=''
    if uncommon>=4:
     numm4=randint(0,48)
     uncommonart4=uncommonlist[numm4]
    else:
          uncommonart4=''
    #rare#
    if rare>=1:
     numm1=randint(0,68)
     rareart1=rarelist[numm1]
    else:
          rareart1='Редкие предметы отсутствуют'
    if rare>=2:
     numm2=randint(0,68)
     rareart2=rarelist[numm2]
    else:
          rareart2=''
    if rare>=3:
     numm3=randint(0,68)
     rareart3=rarelist[numm3]
    else:
          rareart3=''
    if rare>=4:
     numm4=randint(0,68)
     rareart4=rarelist[numm4]
    else:
          rareart4=''
          #unrare(epic)#
    if epic>=1:
     numm1=randint(0,53)
     unrareart1=unrarelist[numm1]
    else:
          unrareart1='Сверхедкие предметы отсутствуют'
    if epic>=2:
     numm2=randint(0,53)
     unrareart2=unrarelist[numm2]
    else:
          unrareart2=''
    if epic>=3:
     numm3=randint(0,53)
     unrareart3=unrarelist[numm3]
    else:
          unrareart3=''
    if epic>=4:
     numm4=randint(0,53)
     unrareart4=unrarelist[numm4]
    else:
          unrareart4=''
    #legendary#
    if legendary>=1:
     numm1=randint(0,52)
     legendaryart1=legendarylist[numm1]
    else:
          legendaryart1='Легендарные предметы отсутствуют'
    if legendary>=2:
     numm2=randint(0,52)
     legendaryart2=legendarylist[numm2]
    else:
          legendaryart2=''
    if legendary>=3:
     numm3=randint(0,52)
     legendaryart3=legendarylist[numm3]
    else:
          legendaryart3=''
    if legendary>=4:
     numm4=randint(0,52)
     legendaryart4=legendarylist[numm4]
    else:
          legendaryart4=''
    #artifact#
    if artifact>=1:
     numm1=randint(0,18)
     artifactart1=artifactlist[numm1]
    else:
          artifactart1='Предметы редкости "Артефакт" отсутствуют'
    if artifact>=2:
     numm2=randint(0,18)
     artifactart2=artifactlist[numm2]
    else:
          artifactart2=''
    if artifact>=3:
     numm3=randint(0,18)
     artifactart3=artifactlist[numm3]
    else:
          artifactart3=''
    if artifact>=4:
     numm4=randint(0,18)
     artifactart4=artifactlist[numm4]
    else:
          artifactart4=''
    data={
        'money1':money1,
        'commonart1':commonart1,
        'commonart2':commonart2,
        'commonart3':commonart3,
        'commonart4':commonart4,
        'uncommonart1':uncommonart1,
        'uncommonart2':uncommonart2,
        'uncommonart3':uncommonart3,
        'uncommonart4':uncommonart4,
        'rareart1':rareart1,
        'rareart2':rareart2,
        'rareart3':rareart3,
        'rareart4':rareart4,
        'unrareart1':unrareart1,
        'unrareart2':unrareart2,
        'unrareart3':unrareart3,
        'unrareart4':unrareart4,
        'legendaryart1':legendaryart1,
        'legendaryart2':legendaryart2,
        'legendaryart3':legendaryart3,
        'legendaryart4':legendaryart4,
        'artifactart1':artifactart1,
        'artifactart2':artifactart2,
        'artifactart3':artifactart3,
        'artifactart4':artifactart4,
    }
    return render(request,'main/lvl_shablon.html' , data)
def level6(request):
    money1=randint(4500,11000)
    common=randint(1,5)
    uncommon=randint(1,3)
    rare=randint(1,2)
    chance=randint(1,100)
    epic=0
    legendary=0
    artifact=0
    if chance>30 and chance<68:
            epic=1
    if chance>30 and chance<43:
            legendary=1
    if chance==50:
            artifact=1
    #common#
    if common>=1:
     numm1=randint(0,7)
     commonart1=commonlist[numm1]
    else:
          commonart1='Обычные предметы отсутствуют'
    if common>=2:
     numm2=randint(0,7)
     commonart2=commonlist[numm2]
    else:
          commonart2=''
    if common>=3:
     numm3=randint(0,7)
     commonart3=commonlist[numm3]
    else:
          commonart3=''
    if common>=4:
     numm4=randint(0,7)
     commonart4=commonlist[numm4]
    else:
          commonart4=''
    #uncommon#
    if uncommon>=1:
     numm1=randint(0,48)
     uncommonart1=uncommonlist[numm1]
    else:
          uncommonart1='Необычные предметы отсутствуют'
    if uncommon>=2:
     numm2=randint(0,48)
     uncommonart2=uncommonlist[numm2]
    else:
          uncommonart2=''
    if uncommon>=3:
     numm3=randint(0,48)
     uncommonart3=uncommonlist[numm3]
    else:
          uncommonart3=''
    if uncommon>=4:
     numm4=randint(0,48)
     uncommonart4=uncommonlist[numm4]
    else:
          uncommonart4=''
    #rare#
    if rare>=1:
     numm1=randint(0,68)
     rareart1=rarelist[numm1]
    else:
          rareart1='Редкие предметы отсутствуют'
    if rare>=2:
     numm2=randint(0,68)
     rareart2=rarelist[numm2]
    else:
          rareart2=''
    if rare>=3:
     numm3=randint(0,68)
     rareart3=rarelist[numm3]
    else:
          rareart3=''
    if rare>=4:
     numm4=randint(0,68)
     rareart4=rarelist[numm4]
    else:
          rareart4=''
          #unrare(epic)#
    if epic>=1:
     numm1=randint(0,53)
     unrareart1=unrarelist[numm1]
    else:
          unrareart1='Сверхедкие предметы отсутствуют'
    if epic>=2:
     numm2=randint(0,53)
     unrareart2=unrarelist[numm2]
    else:
          unrareart2=''
    if epic>=3:
     numm3=randint(0,53)
     unrareart3=unrarelist[numm3]
    else:
          unrareart3=''
    if epic>=4:
     numm4=randint(0,53)
     unrareart4=unrarelist[numm4]
    else:
          unrareart4=''
    #legendary#
    if legendary>=1:
     numm1=randint(0,52)
     legendaryart1=legendarylist[numm1]
    else:
          legendaryart1='Легендарные предметы отсутствуют'
    if legendary>=2:
     numm2=randint(0,52)
     legendaryart2=legendarylist[numm2]
    else:
          legendaryart2=''
    if legendary>=3:
     numm3=randint(0,52)
     legendaryart3=legendarylist[numm3]
    else:
          legendaryart3=''
    if legendary>=4:
     numm4=randint(0,52)
     legendaryart4=legendarylist[numm4]
    else:
          legendaryart4=''
    #artifact#
    if artifact>=1:
     numm1=randint(0,18)
     artifactart1=artifactlist[numm1]
    else:
          artifactart1='Предметы редкости "Артефакт" отсутствуют'
    if artifact>=2:
     numm2=randint(0,18)
     artifactart2=artifactlist[numm2]
    else:
          artifactart2=''
    if artifact>=3:
     numm3=randint(0,18)
     artifactart3=artifactlist[numm3]
    else:
          artifactart3=''
    if artifact>=4:
     numm4=randint(0,18)
     artifactart4=artifactlist[numm4]
    else:
          artifactart4=''
    data={
        'money1':money1,
        'commonart1':commonart1,
        'commonart2':commonart2,
        'commonart3':commonart3,
        'commonart4':commonart4,
        'uncommonart1':uncommonart1,
        'uncommonart2':uncommonart2,
        'uncommonart3':uncommonart3,
        'uncommonart4':uncommonart4,
        'rareart1':rareart1,
        'rareart2':rareart2,
        'rareart3':rareart3,
        'rareart4':rareart4,
        'unrareart1':unrareart1,
        'unrareart2':unrareart2,
        'unrareart3':unrareart3,
        'unrareart4':unrareart4,
        'legendaryart1':legendaryart1,
        'legendaryart2':legendaryart2,
        'legendaryart3':legendaryart3,
        'legendaryart4':legendaryart4,
        'artifactart1':artifactart1,
        'artifactart2':artifactart2,
        'artifactart3':artifactart3,
        'artifactart4':artifactart4,
    }
    return render(request,'main/lvl_shablon.html' , data)
def level7(request):
    money1=randint(5500,11500)
    common=randint(1,4)
    uncommon=randint(1,3)
    rare=randint(1,2)
    chance=randint(1,100)
    epic=0
    legendary=0
    artifact=0
    if chance>30 and chance<70:
            epic=1
    if chance>30 and chance<44:
            legendary=1
    if chance==50 or chance==51:
            artifact=1
    #common#
    if common>=1:
     numm1=randint(0,7)
     commonart1=commonlist[numm1]
    else:
          commonart1='Обычные предметы отсутствуют'
    if common>=2:
     numm2=randint(0,7)
     commonart2=commonlist[numm2]
    else:
          commonart2=''
    if common>=3:
     numm3=randint(0,7)
     commonart3=commonlist[numm3]
    else:
          commonart3=''
    if common>=4:
     numm4=randint(0,7)
     commonart4=commonlist[numm4]
    else:
          commonart4=''
    #uncommon#
    if uncommon>=1:
     numm1=randint(0,48)
     uncommonart1=uncommonlist[numm1]
    else:
          uncommonart1='Необычные предметы отсутствуют'
    if uncommon>=2:
     numm2=randint(0,48)
     uncommonart2=uncommonlist[numm2]
    else:
          uncommonart2=''
    if uncommon>=3:
     numm3=randint(0,48)
     uncommonart3=uncommonlist[numm3]
    else:
          uncommonart3=''
    if uncommon>=4:
     numm4=randint(0,48)
     uncommonart4=uncommonlist[numm4]
    else:
          uncommonart4=''
    #rare#
    if rare>=1:
     numm1=randint(0,68)
     rareart1=rarelist[numm1]
    else:
          rareart1='Редкие предметы отсутствуют'
    if rare>=2:
     numm2=randint(0,68)
     rareart2=rarelist[numm2]
    else:
          rareart2=''
    if rare>=3:
     numm3=randint(0,68)
     rareart3=rarelist[numm3]
    else:
          rareart3=''
    if rare>=4:
     numm4=randint(0,68)
     rareart4=rarelist[numm4]
    else:
          rareart4=''
          #unrare(epic)#
    if epic>=1:
     numm1=randint(0,53)
     unrareart1=unrarelist[numm1]
    else:
          unrareart1='Сверхедкие предметы отсутствуют'
    if epic>=2:
     numm2=randint(0,53)
     unrareart2=unrarelist[numm2]
    else:
          unrareart2=''
    if epic>=3:
     numm3=randint(0,53)
     unrareart3=unrarelist[numm3]
    else:
          unrareart3=''
    if epic>=4:
     numm4=randint(0,53)
     unrareart4=unrarelist[numm4]
    else:
          unrareart4=''
    #legendary#
    if legendary>=1:
     numm1=randint(0,52)
     legendaryart1=legendarylist[numm1]
    else:
          legendaryart1='Легендарные предметы отсутствуют'
    if legendary>=2:
     numm2=randint(0,52)
     legendaryart2=legendarylist[numm2]
    else:
          legendaryart2=''
    if legendary>=3:
     numm3=randint(0,52)
     legendaryart3=legendarylist[numm3]
    else:
          legendaryart3=''
    if legendary>=4:
     numm4=randint(0,52)
     legendaryart4=legendarylist[numm4]
    else:
          legendaryart4=''
    #artifact#
    if artifact>=1:
     numm1=randint(0,18)
     artifactart1=artifactlist[numm1]
    else:
          artifactart1='Предметы редкости "Артефакт" отсутствуют'
    if artifact>=2:
     numm2=randint(0,18)
     artifactart2=artifactlist[numm2]
    else:
          artifactart2=''
    if artifact>=3:
     numm3=randint(0,18)
     artifactart3=artifactlist[numm3]
    else:
          artifactart3=''
    if artifact>=4:
     numm4=randint(0,18)
     artifactart4=artifactlist[numm4]
    else:
          artifactart4=''
    data={
        'money1':money1,
        'commonart1':commonart1,
        'commonart2':commonart2,
        'commonart3':commonart3,
        'commonart4':commonart4,
        'uncommonart1':uncommonart1,
        'uncommonart2':uncommonart2,
        'uncommonart3':uncommonart3,
        'uncommonart4':uncommonart4,
        'rareart1':rareart1,
        'rareart2':rareart2,
        'rareart3':rareart3,
        'rareart4':rareart4,
        'unrareart1':unrareart1,
        'unrareart2':unrareart2,
        'unrareart3':unrareart3,
        'unrareart4':unrareart4,
        'legendaryart1':legendaryart1,
        'legendaryart2':legendaryart2,
        'legendaryart3':legendaryart3,
        'legendaryart4':legendaryart4,
        'artifactart1':artifactart1,
        'artifactart2':artifactart2,
        'artifactart3':artifactart3,
        'artifactart4':artifactart4,
    }
    return render(request,'main/lvl_shablon.html' , data)
def level8(request):
    money1=randint(6200,12700)
    common=randint(1,4)
    uncommon=randint(1,3)
    rare=randint(1,2)
    chance=randint(1,100)
    epic=0
    legendary=0
    artifact=0
    if chance>30 and chance<75:
            epic=1
    if chance>30 and chance<45:
            legendary=1
    if chance==50 or chance==51:
            artifact=1
    #common#
    if common>=1:
     numm1=randint(0,7)
     commonart1=commonlist[numm1]
    else:
          commonart1='Обычные предметы отсутствуют'
    if common>=2:
     numm2=randint(0,7)
     commonart2=commonlist[numm2]
    else:
          commonart2=''
    if common>=3:
     numm3=randint(0,7)
     commonart3=commonlist[numm3]
    else:
          commonart3=''
    if common>=4:
     numm4=randint(0,7)
     commonart4=commonlist[numm4]
    else:
          commonart4=''
    #uncommon#
    if uncommon>=1:
     numm1=randint(0,48)
     uncommonart1=uncommonlist[numm1]
    else:
          uncommonart1='Необычные предметы отсутствуют'
    if uncommon>=2:
     numm2=randint(0,48)
     uncommonart2=uncommonlist[numm2]
    else:
          uncommonart2=''
    if uncommon>=3:
     numm3=randint(0,48)
     uncommonart3=uncommonlist[numm3]
    else:
          uncommonart3=''
    if uncommon>=4:
     numm4=randint(0,48)
     uncommonart4=uncommonlist[numm4]
    else:
          uncommonart4=''
    #rare#
    if rare>=1:
     numm1=randint(0,68)
     rareart1=rarelist[numm1]
    else:
          rareart1='Редкие предметы отсутствуют'
    if rare>=2:
     numm2=randint(0,68)
     rareart2=rarelist[numm2]
    else:
          rareart2=''
    if rare>=3:
     numm3=randint(0,68)
     rareart3=rarelist[numm3]
    else:
          rareart3=''
    if rare>=4:
     numm4=randint(0,68)
     rareart4=rarelist[numm4]
    else:
          rareart4=''
          #unrare(epic)#
    if epic>=1:
     numm1=randint(0,53)
     unrareart1=unrarelist[numm1]
    else:
          unrareart1='Сверхедкие предметы отсутствуют'
    if epic>=2:
     numm2=randint(0,53)
     unrareart2=unrarelist[numm2]
    else:
          unrareart2=''
    if epic>=3:
     numm3=randint(0,53)
     unrareart3=unrarelist[numm3]
    else:
          unrareart3=''
    if epic>=4:
     numm4=randint(0,53)
     unrareart4=unrarelist[numm4]
    else:
          unrareart4=''
    #legendary#
    if legendary>=1:
     numm1=randint(0,52)
     legendaryart1=legendarylist[numm1]
    else:
          legendaryart1='Легендарные предметы отсутствуют'
    if legendary>=2:
     numm2=randint(0,52)
     legendaryart2=legendarylist[numm2]
    else:
          legendaryart2=''
    if legendary>=3:
     numm3=randint(0,52)
     legendaryart3=legendarylist[numm3]
    else:
          legendaryart3=''
    if legendary>=4:
     numm4=randint(0,52)
     legendaryart4=legendarylist[numm4]
    else:
          legendaryart4=''
    #artifact#
    if artifact>=1:
     numm1=randint(0,18)
     artifactart1=artifactlist[numm1]
    else:
          artifactart1='Предметы редкости "Артефакт" отсутствуют'
    if artifact>=2:
     numm2=randint(0,18)
     artifactart2=artifactlist[numm2]
    else:
          artifactart2=''
    if artifact>=3:
     numm3=randint(0,18)
     artifactart3=artifactlist[numm3]
    else:
          artifactart3=''
    if artifact>=4:
     numm4=randint(0,18)
     artifactart4=artifactlist[numm4]
    else:
          artifactart4=''
    data={
        'money1':money1,
        'commonart1':commonart1,
        'commonart2':commonart2,
        'commonart3':commonart3,
        'commonart4':commonart4,
        'uncommonart1':uncommonart1,
        'uncommonart2':uncommonart2,
        'uncommonart3':uncommonart3,
        'uncommonart4':uncommonart4,
        'rareart1':rareart1,
        'rareart2':rareart2,
        'rareart3':rareart3,
        'rareart4':rareart4,
        'unrareart1':unrareart1,
        'unrareart2':unrareart2,
        'unrareart3':unrareart3,
        'unrareart4':unrareart4,
        'legendaryart1':legendaryart1,
        'legendaryart2':legendaryart2,
        'legendaryart3':legendaryart3,
        'legendaryart4':legendaryart4,
        'artifactart1':artifactart1,
        'artifactart2':artifactart2,
        'artifactart3':artifactart3,
        'artifactart4':artifactart4,
    }
    return render(request,'main/lvl_shablon.html' , data)
def level9(request):
    money1=randint(7000,13300)
    common=randint(1,4)
    uncommon=randint(1,3)
    rare=randint(1,2)
    chance=randint(1,100)
    epic=0
    legendary=0
    artifact=0
    if chance>30 and chance<78:
            epic=1
    if chance>30 and chance<47:
            legendary=1
    #common#
    if common>=1:
     numm1=randint(0,7)
     commonart1=commonlist[numm1]
    else:
          commonart1='Обычные предметы отсутствуют'
    if common>=2:
     numm2=randint(0,7)
     commonart2=commonlist[numm2]
    else:
          commonart2=''
    if common>=3:
     numm3=randint(0,7)
     commonart3=commonlist[numm3]
    else:
          commonart3=''
    if common>=4:
     numm4=randint(0,7)
     commonart4=commonlist[numm4]
    else:
          commonart4=''
    #uncommon#
    if uncommon>=1:
     numm1=randint(0,48)
     uncommonart1=uncommonlist[numm1]
    else:
          uncommonart1='Необычные предметы отсутствуют'
    if uncommon>=2:
     numm2=randint(0,48)
     uncommonart2=uncommonlist[numm2]
    else:
          uncommonart2=''
    if uncommon>=3:
     numm3=randint(0,48)
     uncommonart3=uncommonlist[numm3]
    else:
          uncommonart3=''
    if uncommon>=4:
     numm4=randint(0,48)
     uncommonart4=uncommonlist[numm4]
    else:
          uncommonart4=''
    #rare#
    if rare>=1:
     numm1=randint(0,68)
     rareart1=rarelist[numm1]
    else:
          rareart1='Редкие предметы отсутствуют'
    if rare>=2:
     numm2=randint(0,68)
     rareart2=rarelist[numm2]
    else:
          rareart2=''
    if rare>=3:
     numm3=randint(0,68)
     rareart3=rarelist[numm3]
    else:
          rareart3=''
    if rare>=4:
     numm4=randint(0,68)
     rareart4=rarelist[numm4]
    else:
          rareart4=''
          #unrare(epic)#
    if epic>=1:
     numm1=randint(0,53)
     unrareart1=unrarelist[numm1]
    else:
          unrareart1='Сверхедкие предметы отсутствуют'
    if epic>=2:
     numm2=randint(0,53)
     unrareart2=unrarelist[numm2]
    else:
          unrareart2=''
    if epic>=3:
     numm3=randint(0,53)
     unrareart3=unrarelist[numm3]
    else:
          unrareart3=''
    if epic>=4:
     numm4=randint(0,53)
     unrareart4=unrarelist[numm4]
    else:
          unrareart4=''
    #legendary#
    if legendary>=1:
     numm1=randint(0,52)
     legendaryart1=legendarylist[numm1]
    else:
          legendaryart1='Легендарные предметы отсутствуют'
    if legendary>=2:
     numm2=randint(0,52)
     legendaryart2=legendarylist[numm2]
    else:
          legendaryart2=''
    if legendary>=3:
     numm3=randint(0,52)
     legendaryart3=legendarylist[numm3]
    else:
          legendaryart3=''
    if legendary>=4:
     numm4=randint(0,52)
     legendaryart4=legendarylist[numm4]
    else:
          legendaryart4=''
    #artifact#
    if artifact>=1:
     numm1=randint(0,18)
     artifactart1=artifactlist[numm1]
    else:
          artifactart1='Предметы редкости "Артефакт" отсутствуют'
    if artifact>=2:
     numm2=randint(0,18)
     artifactart2=artifactlist[numm2]
    else:
          artifactart2=''
    if artifact>=3:
     numm3=randint(0,18)
     artifactart3=artifactlist[numm3]
    else:
          artifactart3=''
    if artifact>=4:
     numm4=randint(0,18)
     artifactart4=artifactlist[numm4]
    else:
          artifactart4=''
    data={
        'money1':money1,
        'commonart1':commonart1,
        'commonart2':commonart2,
        'commonart3':commonart3,
        'commonart4':commonart4,
        'uncommonart1':uncommonart1,
        'uncommonart2':uncommonart2,
        'uncommonart3':uncommonart3,
        'uncommonart4':uncommonart4,
        'rareart1':rareart1,
        'rareart2':rareart2,
        'rareart3':rareart3,
        'rareart4':rareart4,
        'unrareart1':unrareart1,
        'unrareart2':unrareart2,
        'unrareart3':unrareart3,
        'unrareart4':unrareart4,
        'legendaryart1':legendaryart1,
        'legendaryart2':legendaryart2,
        'legendaryart3':legendaryart3,
        'legendaryart4':legendaryart4,
        'artifactart1':artifactart1,
        'artifactart2':artifactart2,
        'artifactart3':artifactart3,
        'artifactart4':artifactart4,
    }
    return render(request,'main/lvl_shablon.html' , data)
def level10(request):
    money1=randint(7800,14000)
    common=randint(1,4)
    uncommon=randint(1,3)
    rare=randint(1,2)
    chance=randint(1,100)
    epic=0
    legendary=0
    artifact=0
    if chance>30 and chance<83:
            epic=randint(1,2)
    if chance>30 and chance<57:
            legendary=1
    if chance>30 and chance<38:
            artifact=1
    #common#
    if common>=1:
     numm1=randint(0,7)
     commonart1=commonlist[numm1]
    else:
          commonart1='Обычные предметы отсутствуют'
    if common>=2:
     numm2=randint(0,7)
     commonart2=commonlist[numm2]
    else:
          commonart2=''
    if common>=3:
     numm3=randint(0,7)
     commonart3=commonlist[numm3]
    else:
          commonart3=''
    if common>=4:
     numm4=randint(0,7)
     commonart4=commonlist[numm4]
    else:
          commonart4=''
    #uncommon#
    if uncommon>=1:
     numm1=randint(0,48)
     uncommonart1=uncommonlist[numm1]
    else:
          uncommonart1='Необычные предметы отсутствуют'
    if uncommon>=2:
     numm2=randint(0,48)
     uncommonart2=uncommonlist[numm2]
    else:
          uncommonart2=''
    if uncommon>=3:
     numm3=randint(0,48)
     uncommonart3=uncommonlist[numm3]
    else:
          uncommonart3=''
    if uncommon>=4:
     numm4=randint(0,48)
     uncommonart4=uncommonlist[numm4]
    else:
          uncommonart4=''
    #rare#
    if rare>=1:
     numm1=randint(0,68)
     rareart1=rarelist[numm1]
    else:
          rareart1='Редкие предметы отсутствуют'
    if rare>=2:
     numm2=randint(0,68)
     rareart2=rarelist[numm2]
    else:
          rareart2=''
    if rare>=3:
     numm3=randint(0,68)
     rareart3=rarelist[numm3]
    else:
          rareart3=''
    if rare>=4:
     numm4=randint(0,68)
     rareart4=rarelist[numm4]
    else:
          rareart4=''
          #unrare(epic)#
    if epic>=1:
     numm1=randint(0,53)
     unrareart1=unrarelist[numm1]
    else:
          unrareart1='Сверхедкие предметы отсутствуют'
    if epic>=2:
     numm2=randint(0,53)
     unrareart2=unrarelist[numm2]
    else:
          unrareart2=''
    if epic>=3:
     numm3=randint(0,53)
     unrareart3=unrarelist[numm3]
    else:
          unrareart3=''
    if epic>=4:
     numm4=randint(0,53)
     unrareart4=unrarelist[numm4]
    else:
          unrareart4=''
    #legendary#
    if legendary>=1:
     numm1=randint(0,52)
     legendaryart1=legendarylist[numm1]
    else:
          legendaryart1='Легендарные предметы отсутствуют'
    if legendary>=2:
     numm2=randint(0,52)
     legendaryart2=legendarylist[numm2]
    else:
          legendaryart2=''
    if legendary>=3:
     numm3=randint(0,52)
     legendaryart3=legendarylist[numm3]
    else:
          legendaryart3=''
    if legendary>=4:
     numm4=randint(0,52)
     legendaryart4=legendarylist[numm4]
    else:
          legendaryart4=''
    #artifact#
    if artifact>=1:
     numm1=randint(0,18)
     artifactart1=artifactlist[numm1]
    else:
          artifactart1='Предметы редкости "Артефакт" отсутствуют'
    if artifact>=2:
     numm2=randint(0,18)
     artifactart2=artifactlist[numm2]
    else:
          artifactart2=''
    if artifact>=3:
     numm3=randint(0,18)
     artifactart3=artifactlist[numm3]
    else:
          artifactart3=''
    if artifact>=4:
     numm4=randint(0,18)
     artifactart4=artifactlist[numm4]
    else:
          artifactart4=''
    data={
        'money1':money1,
        'commonart1':commonart1,
        'commonart2':commonart2,
        'commonart3':commonart3,
        'commonart4':commonart4,
        'uncommonart1':uncommonart1,
        'uncommonart2':uncommonart2,
        'uncommonart3':uncommonart3,
        'uncommonart4':uncommonart4,
        'rareart1':rareart1,
        'rareart2':rareart2,
        'rareart3':rareart3,
        'rareart4':rareart4,
        'unrareart1':unrareart1,
        'unrareart2':unrareart2,
        'unrareart3':unrareart3,
        'unrareart4':unrareart4,
        'legendaryart1':legendaryart1,
        'legendaryart2':legendaryart2,
        'legendaryart3':legendaryart3,
        'legendaryart4':legendaryart4,
        'artifactart1':artifactart1,
        'artifactart2':artifactart2,
        'artifactart3':artifactart3,
        'artifactart4':artifactart4,
    }
    return render(request,'main/lvl_shablon.html' , data)
def level11(request):
    money1=randint(10000,20000)
    common=randint(1,4)
    uncommon=randint(1,4)
    rare=randint(1,3)
    epic=randint(1,2)
    legendary=0
    artifact=0
    chance=randint(1,100)
    if chance>30 and chance<60:
            legendary=randint(1,2)
    if chance>30 and chance<43:
            artifact=1
    #common#
    if common>=1:
     numm1=randint(0,7)
     commonart1=commonlist[numm1]
    else:
          commonart1='Обычные предметы отсутствуют'
    if common>=2:
     numm2=randint(0,7)
     commonart2=commonlist[numm2]
    else:
          commonart2=''
    if common>=3:
     numm3=randint(0,7)
     commonart3=commonlist[numm3]
    else:
          commonart3=''
    if common>=4:
     numm4=randint(0,7)
     commonart4=commonlist[numm4]
    else:
          commonart4=''
    #uncommon#
    if uncommon>=1:
     numm1=randint(0,48)
     uncommonart1=uncommonlist[numm1]
    else:
          uncommonart1='Необычные предметы отсутствуют'
    if uncommon>=2:
     numm2=randint(0,48)
     uncommonart2=uncommonlist[numm2]
    else:
          uncommonart2=''
    if uncommon>=3:
     numm3=randint(0,48)
     uncommonart3=uncommonlist[numm3]
    else:
          uncommonart3=''
    if uncommon>=4:
     numm4=randint(0,48)
     uncommonart4=uncommonlist[numm4]
    else:
          uncommonart4=''
    #rare#
    if rare>=1:
     numm1=randint(0,68)
     rareart1=rarelist[numm1]
    else:
          rareart1='Редкие предметы отсутствуют'
    if rare>=2:
     numm2=randint(0,68)
     rareart2=rarelist[numm2]
    else:
          rareart2=''
    if rare>=3:
     numm3=randint(0,68)
     rareart3=rarelist[numm3]
    else:
          rareart3=''
    if rare>=4:
     numm4=randint(0,68)
     rareart4=rarelist[numm4]
    else:
          rareart4=''
          #unrare(epic)#
    if epic>=1:
     numm1=randint(0,53)
     unrareart1=unrarelist[numm1]
    else:
          unrareart1='Сверхедкие предметы отсутствуют'
    if epic>=2:
     numm2=randint(0,53)
     unrareart2=unrarelist[numm2]
    else:
          unrareart2=''
    if epic>=3:
     numm3=randint(0,53)
     unrareart3=unrarelist[numm3]
    else:
          unrareart3=''
    if epic>=4:
     numm4=randint(0,53)
     unrareart4=unrarelist[numm4]
    else:
          unrareart4=''
    #legendary#
    if legendary>=1:
     numm1=randint(0,52)
     legendaryart1=legendarylist[numm1]
    else:
          legendaryart1='Легендарные предметы отсутствуют'
    if legendary>=2:
     numm2=randint(0,52)
     legendaryart2=legendarylist[numm2]
    else:
          legendaryart2=''
    if legendary>=3:
     numm3=randint(0,52)
     legendaryart3=legendarylist[numm3]
    else:
          legendaryart3=''
    if legendary>=4:
     numm4=randint(0,52)
     legendaryart4=legendarylist[numm4]
    else:
          legendaryart4=''
    #artifact#
    if artifact>=1:
     numm1=randint(0,18)
     artifactart1=artifactlist[numm1]
    else:
          artifactart1='Предметы редкости "Артефакт" отсутствуют'
    if artifact>=2:
     numm2=randint(0,18)
     artifactart2=artifactlist[numm2]
    else:
          artifactart2=''
    if artifact>=3:
     numm3=randint(0,18)
     artifactart3=artifactlist[numm3]
    else:
          artifactart3=''
    if artifact>=4:
     numm4=randint(0,18)
     artifactart4=artifactlist[numm4]
    else:
          artifactart4=''
    data={
        'money1':money1,
        'commonart1':commonart1,
        'commonart2':commonart2,
        'commonart3':commonart3,
        'commonart4':commonart4,
        'uncommonart1':uncommonart1,
        'uncommonart2':uncommonart2,
        'uncommonart3':uncommonart3,
        'uncommonart4':uncommonart4,
        'rareart1':rareart1,
        'rareart2':rareart2,
        'rareart3':rareart3,
        'rareart4':rareart4,
        'unrareart1':unrareart1,
        'unrareart2':unrareart2,
        'unrareart3':unrareart3,
        'unrareart4':unrareart4,
        'legendaryart1':legendaryart1,
        'legendaryart2':legendaryart2,
        'legendaryart3':legendaryart3,
        'legendaryart4':legendaryart4,
        'artifactart1':artifactart1,
        'artifactart2':artifactart2,
        'artifactart3':artifactart3,
        'artifactart4':artifactart4,
    }
    return render(request,'main/lvl_shablon.html', data )
def level12(request):
    money1=randint(15000,30000)
    common=randint(1,4)
    uncommon=randint(1,4)
    rare=randint(1,4)
    epic=randint(1,2)
    legendary=0
    artifact=0
    chance=randint(1,100)
    if chance>20 and chance<60:
             legendary=randint(1,2)
    if chance>30 and chance<50:
             artifact=1
    #common#
    if common>=1:
     numm1=randint(0,7)
     commonart1=commonlist[numm1]
    else:
          commonart1='Обычные предметы отсутствуют'
    if common>=2:
     numm2=randint(0,7)
     commonart2=commonlist[numm2]
    else:
          commonart2=''
    if common>=3:
     numm3=randint(0,7)
     commonart3=commonlist[numm3]
    else:
          commonart3=''
    if common>=4:
     numm4=randint(0,7)
     commonart4=commonlist[numm4]
    else:
          commonart4=''
    #uncommon#
    if uncommon>=1:
     numm1=randint(0,48)
     uncommonart1=uncommonlist[numm1]
    else:
          uncommonart1='Необычные предметы отсутствуют'
    if uncommon>=2:
     numm2=randint(0,48)
     uncommonart2=uncommonlist[numm2]
    else:
          uncommonart2=''
    if uncommon>=3:
     numm3=randint(0,48)
     uncommonart3=uncommonlist[numm3]
    else:
          uncommonart3=''
    if uncommon>=4:
     numm4=randint(0,48)
     uncommonart4=uncommonlist[numm4]
    else:
          uncommonart4=''
    #rare#
    if rare>=1:
     numm1=randint(0,68)
     rareart1=rarelist[numm1]
    else:
          rareart1='Редкие предметы отсутствуют'
    if rare>=2:
     numm2=randint(0,68)
     rareart2=rarelist[numm2]
    else:
          rareart2=''
    if rare>=3:
     numm3=randint(0,68)
     rareart3=rarelist[numm3]
    else:
          rareart3=''
    if rare>=4:
     numm4=randint(0,68)
     rareart4=rarelist[numm4]
    else:
          rareart4=''
          #unrare(epic)#
    if epic>=1:
     numm1=randint(0,53)
     unrareart1=unrarelist[numm1]
    else:
          unrareart1='Сверхедкие предметы отсутствуют'
    if epic>=2:
     numm2=randint(0,53)
     unrareart2=unrarelist[numm2]
    else:
          unrareart2=''
    if epic>=3:
     numm3=randint(0,53)
     unrareart3=unrarelist[numm3]
    else:
          unrareart3=''
    if epic>=4:
     numm4=randint(0,53)
     unrareart4=unrarelist[numm4]
    else:
          unrareart4=''
    #legendary#
    if legendary>=1:
     numm1=randint(0,52)
     legendaryart1=legendarylist[numm1]
    else:
          legendaryart1='Легендарные предметы отсутствуют'
    if legendary>=2:
     numm2=randint(0,52)
     legendaryart2=legendarylist[numm2]
    else:
          legendaryart2=''
    if legendary>=3:
     numm3=randint(0,52)
     legendaryart3=legendarylist[numm3]
    else:
          legendaryart3=''
    if legendary>=4:
     numm4=randint(0,52)
     legendaryart4=legendarylist[numm4]
    else:
          legendaryart4=''
    #artifact#
    if artifact>=1:
     numm1=randint(0,18)
     artifactart1=artifactlist[numm1]
    else:
          artifactart1='Предметы редкости "Артефакт" отсутствуют'
    if artifact>=2:
     numm2=randint(0,18)
     artifactart2=artifactlist[numm2]
    else:
          artifactart2=''
    if artifact>=3:
     numm3=randint(0,18)
     artifactart3=artifactlist[numm3]
    else:
          artifactart3=''
    if artifact>=4:
     numm4=randint(0,18)
     artifactart4=artifactlist[numm4]
    else:
          artifactart4=''
    data={
        'money1':money1,
        'commonart1':commonart1,
        'commonart2':commonart2,
        'commonart3':commonart3,
        'commonart4':commonart4,
        'uncommonart1':uncommonart1,
        'uncommonart2':uncommonart2,
        'uncommonart3':uncommonart3,
        'uncommonart4':uncommonart4,
        'rareart1':rareart1,
        'rareart2':rareart2,
        'rareart3':rareart3,
        'rareart4':rareart4,
        'unrareart1':unrareart1,
        'unrareart2':unrareart2,
        'unrareart3':unrareart3,
        'unrareart4':unrareart4,
        'legendaryart1':legendaryart1,
        'legendaryart2':legendaryart2,
        'legendaryart3':legendaryart3,
        'legendaryart4':legendaryart4,
        'artifactart1':artifactart1,
        'artifactart2':artifactart2,
        'artifactart3':artifactart3,
        'artifactart4':artifactart4,
    }
    return render(request,'main/lvl_shablon.html' , data)
def level13(request):
    money1=randint(18000,40000)
    common=randint(1,4)
    uncommon=randint(1,4)
    rare=randint(1,3)
    epic=randint(1,3)
    legendary=0
    artifact=0
    chance=randint(1,100)
    if chance>10 and chance<60:
            legendary=randint(1,2)
    if chance>30 and chance<55:
            artifact=randint(1,2)
    #common#
    if common>=1:
     numm1=randint(0,7)
     commonart1=commonlist[numm1]
    else:
          commonart1='Обычные предметы отсутствуют'
    if common>=2:
     numm2=randint(0,7)
     commonart2=commonlist[numm2]
    else:
          commonart2=''
    if common>=3:
     numm3=randint(0,7)
     commonart3=commonlist[numm3]
    else:
          commonart3=''
    if common>=4:
     numm4=randint(0,7)
     commonart4=commonlist[numm4]
    else:
          commonart4=''
    #uncommon#
    if uncommon>=1:
     numm1=randint(0,48)
     uncommonart1=uncommonlist[numm1]
    else:
          uncommonart1='Необычные предметы отсутствуют'
    if uncommon>=2:
     numm2=randint(0,48)
     uncommonart2=uncommonlist[numm2]
    else:
          uncommonart2=''
    if uncommon>=3:
     numm3=randint(0,48)
     uncommonart3=uncommonlist[numm3]
    else:
          uncommonart3=''
    if uncommon>=4:
     numm4=randint(0,48)
     uncommonart4=uncommonlist[numm4]
    else:
          uncommonart4=''
    #rare#
    if rare>=1:
     numm1=randint(0,68)
     rareart1=rarelist[numm1]
    else:
          rareart1='Редкие предметы отсутствуют'
    if rare>=2:
     numm2=randint(0,68)
     rareart2=rarelist[numm2]
    else:
          rareart2=''
    if rare>=3:
     numm3=randint(0,68)
     rareart3=rarelist[numm3]
    else:
          rareart3=''
    if rare>=4:
     numm4=randint(0,68)
     rareart4=rarelist[numm4]
    else:
          rareart4=''
          #unrare(epic)#
    if epic>=1:
     numm1=randint(0,53)
     unrareart1=unrarelist[numm1]
    else:
          unrareart1='Сверхедкие предметы отсутствуют'
    if epic>=2:
     numm2=randint(0,53)
     unrareart2=unrarelist[numm2]
    else:
          unrareart2=''
    if epic>=3:
     numm3=randint(0,53)
     unrareart3=unrarelist[numm3]
    else:
          unrareart3=''
    if epic>=4:
     numm4=randint(0,53)
     unrareart4=unrarelist[numm4]
    else:
          unrareart4=''
    #legendary#
    if legendary>=1:
     numm1=randint(0,52)
     legendaryart1=legendarylist[numm1]
    else:
          legendaryart1='Легендарные предметы отсутствуют'
    if legendary>=2:
     numm2=randint(0,52)
     legendaryart2=legendarylist[numm2]
    else:
          legendaryart2=''
    if legendary>=3:
     numm3=randint(0,52)
     legendaryart3=legendarylist[numm3]
    else:
          legendaryart3=''
    if legendary>=4:
     numm4=randint(0,52)
     legendaryart4=legendarylist[numm4]
    else:
          legendaryart4=''
    #artifact#
    if artifact>=1:
     numm1=randint(0,18)
     artifactart1=artifactlist[numm1]
    else:
          artifactart1='Предметы редкости "Артефакт" отсутствуют'
    if artifact>=2:
     numm2=randint(0,18)
     artifactart2=artifactlist[numm2]
    else:
          artifactart2=''
    if artifact>=3:
     numm3=randint(0,18)
     artifactart3=artifactlist[numm3]
    else:
          artifactart3=''
    if artifact>=4:
     numm4=randint(0,18)
     artifactart4=artifactlist[numm4]
    else:
          artifactart4=''
    data={
        'money1':money1,
        'commonart1':commonart1,
        'commonart2':commonart2,
        'commonart3':commonart3,
        'commonart4':commonart4,
        'uncommonart1':uncommonart1,
        'uncommonart2':uncommonart2,
        'uncommonart3':uncommonart3,
        'uncommonart4':uncommonart4,
        'rareart1':rareart1,
        'rareart2':rareart2,
        'rareart3':rareart3,
        'rareart4':rareart4,
        'unrareart1':unrareart1,
        'unrareart2':unrareart2,
        'unrareart3':unrareart3,
        'unrareart4':unrareart4,
        'legendaryart1':legendaryart1,
        'legendaryart2':legendaryart2,
        'legendaryart3':legendaryart3,
        'legendaryart4':legendaryart4,
        'artifactart1':artifactart1,
        'artifactart2':artifactart2,
        'artifactart3':artifactart3,
        'artifactart4':artifactart4,
    }
    return render(request,'main/lvl_shablon.html' , data)
def level14(request):
    money1=randint(25000,48000)
    common=randint(1,4)
    uncommon=randint(1,4)
    rare=randint(1,4)
    epic=randint(1,3)
    legendary=0
    artifact=0
    chance=randint(1,100)
    if chance>10 and chance<65:
            legendary=randint(1,2)
    if chance>30 and chance<58:
            artifact=randint(1,2)
    #common#
    if common>=1:
     numm1=randint(0,7)
     commonart1=commonlist[numm1]
    else:
          commonart1='Обычные предметы отсутствуют'
    if common>=2:
     numm2=randint(0,7)
     commonart2=commonlist[numm2]
    else:
          commonart2=''
    if common>=3:
     numm3=randint(0,7)
     commonart3=commonlist[numm3]
    else:
          commonart3=''
    if common>=4:
     numm4=randint(0,7)
     commonart4=commonlist[numm4]
    else:
          commonart4=''
    #uncommon#
    if uncommon>=1:
     numm1=randint(0,48)
     uncommonart1=uncommonlist[numm1]
    else:
          uncommonart1='Необычные предметы отсутствуют'
    if uncommon>=2:
     numm2=randint(0,48)
     uncommonart2=uncommonlist[numm2]
    else:
          uncommonart2=''
    if uncommon>=3:
     numm3=randint(0,48)
     uncommonart3=uncommonlist[numm3]
    else:
          uncommonart3=''
    if uncommon>=4:
     numm4=randint(0,48)
     uncommonart4=uncommonlist[numm4]
    else:
          uncommonart4=''
    #rare#
    if rare>=1:
     numm1=randint(0,68)
     rareart1=rarelist[numm1]
    else:
          rareart1='Редкие предметы отсутствуют'
    if rare>=2:
     numm2=randint(0,68)
     rareart2=rarelist[numm2]
    else:
          rareart2=''
    if rare>=3:
     numm3=randint(0,68)
     rareart3=rarelist[numm3]
    else:
          rareart3=''
    if rare>=4:
     numm4=randint(0,68)
     rareart4=rarelist[numm4]
    else:
          rareart4=''
          #unrare(epic)#
    if epic>=1:
     numm1=randint(0,53)
     unrareart1=unrarelist[numm1]
    else:
          unrareart1='Сверхедкие предметы отсутствуют'
    if epic>=2:
     numm2=randint(0,53)
     unrareart2=unrarelist[numm2]
    else:
          unrareart2=''
    if epic>=3:
     numm3=randint(0,53)
     unrareart3=unrarelist[numm3]
    else:
          unrareart3=''
    if epic>=4:
     numm4=randint(0,53)
     unrareart4=unrarelist[numm4]
    else:
          unrareart4=''
    #legendary#
    if legendary>=1:
     numm1=randint(0,52)
     legendaryart1=legendarylist[numm1]
    else:
          legendaryart1='Легендарные предметы отсутствуют'
    if legendary>=2:
     numm2=randint(0,52)
     legendaryart2=legendarylist[numm2]
    else:
          legendaryart2=''
    if legendary>=3:
     numm3=randint(0,52)
     legendaryart3=legendarylist[numm3]
    else:
          legendaryart3=''
    if legendary>=4:
     numm4=randint(0,52)
     legendaryart4=legendarylist[numm4]
    else:
          legendaryart4=''
    #artifact#
    if artifact>=1:
     numm1=randint(0,18)
     artifactart1=artifactlist[numm1]
    else:
          artifactart1='Предметы редкости "Артефакт" отсутствуют'
    if artifact>=2:
     numm2=randint(0,18)
     artifactart2=artifactlist[numm2]
    else:
          artifactart2=''
    if artifact>=3:
     numm3=randint(0,18)
     artifactart3=artifactlist[numm3]
    else:
          artifactart3=''
    if artifact>=4:
     numm4=randint(0,18)
     artifactart4=artifactlist[numm4]
    else:
          artifactart4=''
    data={
        'money1':money1,
        'commonart1':commonart1,
        'commonart2':commonart2,
        'commonart3':commonart3,
        'commonart4':commonart4,
        'uncommonart1':uncommonart1,
        'uncommonart2':uncommonart2,
        'uncommonart3':uncommonart3,
        'uncommonart4':uncommonart4,
        'rareart1':rareart1,
        'rareart2':rareart2,
        'rareart3':rareart3,
        'rareart4':rareart4,
        'unrareart1':unrareart1,
        'unrareart2':unrareart2,
        'unrareart3':unrareart3,
        'unrareart4':unrareart4,
        'legendaryart1':legendaryart1,
        'legendaryart2':legendaryart2,
        'legendaryart3':legendaryart3,
        'legendaryart4':legendaryart4,
        'artifactart1':artifactart1,
        'artifactart2':artifactart2,
        'artifactart3':artifactart3,
        'artifactart4':artifactart4,
    }
    return render(request,'main/lvl_shablon.html' , data)
def level15(request):
    money1=randint(29000,56000)
    common=randint(1,4)
    uncommon=randint(1,4)
    rare=randint(1,4)
    epic=randint(1,3)
    legendary=0
    artifact=0
    chance=randint(1,100)
    if chance>5 and chance<70:
            legendary=randint(1,2)
        
    if chance>30 and chance<70:
            artifact=randint(1,2)
    #common#
    if common>=1:
     numm1=randint(0,7)
     commonart1=commonlist[numm1]
    else:
          commonart1='Обычные предметы отсутствуют'
    if common>=2:
     numm2=randint(0,7)
     commonart2=commonlist[numm2]
    else:
          commonart2=''
    if common>=3:
     numm3=randint(0,7)
     commonart3=commonlist[numm3]
    else:
          commonart3=''
    if common>=4:
     numm4=randint(0,7)
     commonart4=commonlist[numm4]
    else:
          commonart4=''
    #uncommon#
    if uncommon>=1:
     numm1=randint(0,48)
     uncommonart1=uncommonlist[numm1]
    else:
          uncommonart1='Необычные предметы отсутствуют'
    if uncommon>=2:
     numm2=randint(0,48)
     uncommonart2=uncommonlist[numm2]
    else:
          uncommonart2=''
    if uncommon>=3:
     numm3=randint(0,48)
     uncommonart3=uncommonlist[numm3]
    else:
          uncommonart3=''
    if uncommon>=4:
     numm4=randint(0,48)
     uncommonart4=uncommonlist[numm4]
    else:
          uncommonart4=''
    #rare#
    if rare>=1:
     numm1=randint(0,68)
     rareart1=rarelist[numm1]
    else:
          rareart1='Редкие предметы отсутствуют'
    if rare>=2:
     numm2=randint(0,68)
     rareart2=rarelist[numm2]
    else:
          rareart2=''
    if rare>=3:
     numm3=randint(0,68)
     rareart3=rarelist[numm3]
    else:
          rareart3=''
    if rare>=4:
     numm4=randint(0,68)
     rareart4=rarelist[numm4]
    else:
          rareart4=''
          #unrare(epic)#
    if epic>=1:
     numm1=randint(0,53)
     unrareart1=unrarelist[numm1]
    else:
          unrareart1='Сверхедкие предметы отсутствуют'
    if epic>=2:
     numm2=randint(0,53)
     unrareart2=unrarelist[numm2]
    else:
          unrareart2=''
    if epic>=3:
     numm3=randint(0,53)
     unrareart3=unrarelist[numm3]
    else:
          unrareart3=''
    if epic>=4:
     numm4=randint(0,53)
     unrareart4=unrarelist[numm4]
    else:
          unrareart4=''
    #legendary#
    if legendary>=1:
     numm1=randint(0,52)
     legendaryart1=legendarylist[numm1]
    else:
          legendaryart1='Легендарные предметы отсутствуют'
    if legendary>=2:
     numm2=randint(0,52)
     legendaryart2=legendarylist[numm2]
    else:
          legendaryart2=''
    if legendary>=3:
     numm3=randint(0,52)
     legendaryart3=legendarylist[numm3]
    else:
          legendaryart3=''
    if legendary>=4:
     numm4=randint(0,52)
     legendaryart4=legendarylist[numm4]
    else:
          legendaryart4=''
    #artifact#
    if artifact>=1:
     numm1=randint(0,18)
     artifactart1=artifactlist[numm1]
    else:
          artifactart1='Предметы редкости "Артефакт" отсутствуют'
    if artifact>=2:
     numm2=randint(0,18)
     artifactart2=artifactlist[numm2]
    else:
          artifactart2=''
    if artifact>=3:
     numm3=randint(0,18)
     artifactart3=artifactlist[numm3]
    else:
          artifactart3=''
    if artifact>=4:
     numm4=randint(0,18)
     artifactart4=artifactlist[numm4]
    else:
          artifactart4=''
    data={
        'money1':money1,
        'commonart1':commonart1,
        'commonart2':commonart2,
        'commonart3':commonart3,
        'commonart4':commonart4,
        'uncommonart1':uncommonart1,
        'uncommonart2':uncommonart2,
        'uncommonart3':uncommonart3,
        'uncommonart4':uncommonart4,
        'rareart1':rareart1,
        'rareart2':rareart2,
        'rareart3':rareart3,
        'rareart4':rareart4,
        'unrareart1':unrareart1,
        'unrareart2':unrareart2,
        'unrareart3':unrareart3,
        'unrareart4':unrareart4,
        'legendaryart1':legendaryart1,
        'legendaryart2':legendaryart2,
        'legendaryart3':legendaryart3,
        'legendaryart4':legendaryart4,
        'artifactart1':artifactart1,
        'artifactart2':artifactart2,
        'artifactart3':artifactart3,
        'artifactart4':artifactart4,
    }
    return render(request,'main/lvl_shablon.html' , data)
def level16(request):
    money1=randint(50000,100000)
    common=randint(1,4)
    uncommon=randint(1,4)
    rare=randint(1,4)
    legendary=0
    artifact=0
    epic=randint(1,3)
    chance=randint(1,100)
    if chance>5 and chance<75:
            legendary=randint(1,2)
    if chance>20 and chance<70:
            artifact=randint(1,3)
    #common#
    if common>=1:
     numm1=randint(0,7)
     commonart1=commonlist[numm1]
    else:
          commonart1='Обычные предметы отсутствуют'
    if common>=2:
     numm2=randint(0,7)
     commonart2=commonlist[numm2]
    else:
          commonart2=''
    if common>=3:
     numm3=randint(0,7)
     commonart3=commonlist[numm3]
    else:
          commonart3=''
    if common>=4:
     numm4=randint(0,7)
     commonart4=commonlist[numm4]
    else:
          commonart4=''
    #uncommon#
    if uncommon>=1:
     numm1=randint(0,48)
     uncommonart1=uncommonlist[numm1]
    else:
          uncommonart1='Необычные предметы отсутствуют'
    if uncommon>=2:
     numm2=randint(0,48)
     uncommonart2=uncommonlist[numm2]
    else:
          uncommonart2=''
    if uncommon>=3:
     numm3=randint(0,48)
     uncommonart3=uncommonlist[numm3]
    else:
          uncommonart3=''
    if uncommon>=4:
     numm4=randint(0,48)
     uncommonart4=uncommonlist[numm4]
    else:
          uncommonart4=''
    #rare#
    if rare>=1:
     numm1=randint(0,68)
     rareart1=rarelist[numm1]
    else:
          rareart1='Редкие предметы отсутствуют'
    if rare>=2:
     numm2=randint(0,68)
     rareart2=rarelist[numm2]
    else:
          rareart2=''
    if rare>=3:
     numm3=randint(0,68)
     rareart3=rarelist[numm3]
    else:
          rareart3=''
    if rare>=4:
     numm4=randint(0,68)
     rareart4=rarelist[numm4]
    else:
          rareart4=''
          #unrare(epic)#
    if epic>=1:
     numm1=randint(0,53)
     unrareart1=unrarelist[numm1]
    else:
          unrareart1='Сверхедкие предметы отсутствуют'
    if epic>=2:
     numm2=randint(0,53)
     unrareart2=unrarelist[numm2]
    else:
          unrareart2=''
    if epic>=3:
     numm3=randint(0,53)
     unrareart3=unrarelist[numm3]
    else:
          unrareart3=''
    if epic>=4:
     numm4=randint(0,53)
     unrareart4=unrarelist[numm4]
    else:
          unrareart4=''
    #legendary#
    if legendary>=1:
     numm1=randint(0,52)
     legendaryart1=legendarylist[numm1]
    else:
          legendaryart1='Легендарные предметы отсутствуют'
    if legendary>=2:
     numm2=randint(0,52)
     legendaryart2=legendarylist[numm2]
    else:
          legendaryart2=''
    if legendary>=3:
     numm3=randint(0,52)
     legendaryart3=legendarylist[numm3]
    else:
          legendaryart3=''
    if legendary>=4:
     numm4=randint(0,52)
     legendaryart4=legendarylist[numm4]
    else:
          legendaryart4=''
    #artifact#
    if artifact>=1:
     numm1=randint(0,18)
     artifactart1=artifactlist[numm1]
    else:
          artifactart1='Предметы редкости "Артефакт" отсутствуют'
    if artifact>=2:
     numm2=randint(0,18)
     artifactart2=artifactlist[numm2]
    else:
          artifactart2=''
    if artifact>=3:
     numm3=randint(0,18)
     artifactart3=artifactlist[numm3]
    else:
          artifactart3=''
    if artifact>=4:
     numm4=randint(0,18)
     artifactart4=artifactlist[numm4]
    else:
          artifactart4=''
    data={
        'money1':money1,
        'commonart1':commonart1,
        'commonart2':commonart2,
        'commonart3':commonart3,
        'commonart4':commonart4,
        'uncommonart1':uncommonart1,
        'uncommonart2':uncommonart2,
        'uncommonart3':uncommonart3,
        'uncommonart4':uncommonart4,
        'rareart1':rareart1,
        'rareart2':rareart2,
        'rareart3':rareart3,
        'rareart4':rareart4,
        'unrareart1':unrareart1,
        'unrareart2':unrareart2,
        'unrareart3':unrareart3,
        'unrareart4':unrareart4,
        'legendaryart1':legendaryart1,
        'legendaryart2':legendaryart2,
        'legendaryart3':legendaryart3,
        'legendaryart4':legendaryart4,
        'artifactart1':artifactart1,
        'artifactart2':artifactart2,
        'artifactart3':artifactart3,
        'artifactart4':artifactart4,
    }
    return render(request,'main/lvl_shablon.html' , data)
def level17(request):
    money1=randint(60000,120000)
    common=randint(1,4)
    uncommon=randint(1,4)
    legendary=0
    artifact=0
    rare=randint(1,4)
    epic=randint(1,3)
    chance=randint(1,100)
    if chance>5 and chance<90:
            legendary=randint(1,2)
    if chance>20 and chance<75:
            artifact=randint(1,3)
    #common#
    if common>=1:
     numm1=randint(0,7)
     commonart1=commonlist[numm1]
    else:
          commonart1='Обычные предметы отсутствуют'
    if common>=2:
     numm2=randint(0,7)
     commonart2=commonlist[numm2]
    else:
          commonart2=''
    if common>=3:
     numm3=randint(0,7)
     commonart3=commonlist[numm3]
    else:
          commonart3=''
    if common>=4:
     numm4=randint(0,7)
     commonart4=commonlist[numm4]
    else:
          commonart4=''
    #uncommon#
    if uncommon>=1:
     numm1=randint(0,48)
     uncommonart1=uncommonlist[numm1]
    else:
          uncommonart1='Необычные предметы отсутствуют'
    if uncommon>=2:
     numm2=randint(0,48)
     uncommonart2=uncommonlist[numm2]
    else:
          uncommonart2=''
    if uncommon>=3:
     numm3=randint(0,48)
     uncommonart3=uncommonlist[numm3]
    else:
          uncommonart3=''
    if uncommon>=4:
     numm4=randint(0,48)
     uncommonart4=uncommonlist[numm4]
    else:
          uncommonart4=''
    #rare#
    if rare>=1:
     numm1=randint(0,68)
     rareart1=rarelist[numm1]
    else:
          rareart1='Редкие предметы отсутствуют'
    if rare>=2:
     numm2=randint(0,68)
     rareart2=rarelist[numm2]
    else:
          rareart2=''
    if rare>=3:
     numm3=randint(0,68)
     rareart3=rarelist[numm3]
    else:
          rareart3=''
    if rare>=4:
     numm4=randint(0,68)
     rareart4=rarelist[numm4]
    else:
          rareart4=''
          #unrare(epic)#
    if epic>=1:
     numm1=randint(0,53)
     unrareart1=unrarelist[numm1]
    else:
          unrareart1='Сверхедкие предметы отсутствуют'
    if epic>=2:
     numm2=randint(0,53)
     unrareart2=unrarelist[numm2]
    else:
          unrareart2=''
    if epic>=3:
     numm3=randint(0,53)
     unrareart3=unrarelist[numm3]
    else:
          unrareart3=''
    if epic>=4:
     numm4=randint(0,53)
     unrareart4=unrarelist[numm4]
    else:
          unrareart4=''
    #legendary#
    if legendary>=1:
     numm1=randint(0,52)
     legendaryart1=legendarylist[numm1]
    else:
          legendaryart1='Легендарные предметы отсутствуют'
    if legendary>=2:
     numm2=randint(0,52)
     legendaryart2=legendarylist[numm2]
    else:
          legendaryart2=''
    if legendary>=3:
     numm3=randint(0,52)
     legendaryart3=legendarylist[numm3]
    else:
          legendaryart3=''
    if legendary>=4:
     numm4=randint(0,52)
     legendaryart4=legendarylist[numm4]
    else:
          legendaryart4=''
    #artifact#
    if artifact>=1:
     numm1=randint(0,18)
     artifactart1=artifactlist[numm1]
    else:
          artifactart1='Предметы редкости "Артефакт" отсутствуют'
    if artifact>=2:
     numm2=randint(0,18)
     artifactart2=artifactlist[numm2]
    else:
          artifactart2=''
    if artifact>=3:
     numm3=randint(0,18)
     artifactart3=artifactlist[numm3]
    else:
          artifactart3=''
    if artifact>=4:
     numm4=randint(0,18)
     artifactart4=artifactlist[numm4]
    else:
          artifactart4=''
    data={
        'money1':money1,
        'commonart1':commonart1,
        'commonart2':commonart2,
        'commonart3':commonart3,
        'commonart4':commonart4,
        'uncommonart1':uncommonart1,
        'uncommonart2':uncommonart2,
        'uncommonart3':uncommonart3,
        'uncommonart4':uncommonart4,
        'rareart1':rareart1,
        'rareart2':rareart2,
        'rareart3':rareart3,
        'rareart4':rareart4,
        'unrareart1':unrareart1,
        'unrareart2':unrareart2,
        'unrareart3':unrareart3,
        'unrareart4':unrareart4,
        'legendaryart1':legendaryart1,
        'legendaryart2':legendaryart2,
        'legendaryart3':legendaryart3,
        'legendaryart4':legendaryart4,
        'artifactart1':artifactart1,
        'artifactart2':artifactart2,
        'artifactart3':artifactart3,
        'artifactart4':artifactart4,
    }
    return render(request,'main/lvl_shablon.html' , data)
def level18(request):
    money1=randint(100000,1200000)
    common=randint(1,4)
    uncommon=randint(1,4)
    rare=randint(1,4)
    artifact=0
    epic=randint(1,3)
    chance=randint(1,100)
    legendary=randint(1,2)
    if chance>20 and chance<75:
            artifact=randint(1,3)
    #common#
    if common>=1:
     numm1=randint(0,7)
     commonart1=commonlist[numm1]
    else:
          commonart1='Обычные предметы отсутствуют'
    if common>=2:
     numm2=randint(0,7)
     commonart2=commonlist[numm2]
    else:
          commonart2=''
    if common>=3:
     numm3=randint(0,7)
     commonart3=commonlist[numm3]
    else:
          commonart3=''
    if common>=4:
     numm4=randint(0,7)
     commonart4=commonlist[numm4]
    else:
          commonart4=''
    #uncommon#
    if uncommon>=1:
     numm1=randint(0,48)
     uncommonart1=uncommonlist[numm1]
    else:
          uncommonart1='Необычные предметы отсутствуют'
    if uncommon>=2:
     numm2=randint(0,48)
     uncommonart2=uncommonlist[numm2]
    else:
          uncommonart2=''
    if uncommon>=3:
     numm3=randint(0,48)
     uncommonart3=uncommonlist[numm3]
    else:
          uncommonart3=''
    if uncommon>=4:
     numm4=randint(0,48)
     uncommonart4=uncommonlist[numm4]
    else:
          uncommonart4=''
    #rare#
    if rare>=1:
     numm1=randint(0,68)
     rareart1=rarelist[numm1]
    else:
          rareart1='Редкие предметы отсутствуют'
    if rare>=2:
     numm2=randint(0,68)
     rareart2=rarelist[numm2]
    else:
          rareart2=''
    if rare>=3:
     numm3=randint(0,68)
     rareart3=rarelist[numm3]
    else:
          rareart3=''
    if rare>=4:
     numm4=randint(0,68)
     rareart4=rarelist[numm4]
    else:
          rareart4=''
          #unrare(epic)#
    if epic>=1:
     numm1=randint(0,53)
     unrareart1=unrarelist[numm1]
    else:
          unrareart1='Сверхедкие предметы отсутствуют'
    if epic>=2:
     numm2=randint(0,53)
     unrareart2=unrarelist[numm2]
    else:
          unrareart2=''
    if epic>=3:
     numm3=randint(0,53)
     unrareart3=unrarelist[numm3]
    else:
          unrareart3=''
    if epic>=4:
     numm4=randint(0,53)
     unrareart4=unrarelist[numm4]
    else:
          unrareart4=''
    #legendary#
    if legendary>=1:
     numm1=randint(0,52)
     legendaryart1=legendarylist[numm1]
    else:
          legendaryart1='Легендарные предметы отсутствуют'
    if legendary>=2:
     numm2=randint(0,52)
     legendaryart2=legendarylist[numm2]
    else:
          legendaryart2=''
    if legendary>=3:
     numm3=randint(0,52)
     legendaryart3=legendarylist[numm3]
    else:
          legendaryart3=''
    if legendary>=4:
     numm4=randint(0,52)
     legendaryart4=legendarylist[numm4]
    else:
          legendaryart4=''
    #artifact#
    if artifact>=1:
     numm1=randint(0,18)
     artifactart1=artifactlist[numm1]
    else:
          artifactart1='Предметы редкости "Артефакт" отсутствуют'
    if artifact>=2:
     numm2=randint(0,18)
     artifactart2=artifactlist[numm2]
    else:
          artifactart2=''
    if artifact>=3:
     numm3=randint(0,18)
     artifactart3=artifactlist[numm3]
    else:
          artifactart3=''
    if artifact>=4:
     numm4=randint(0,18)
     artifactart4=artifactlist[numm4]
    else:
          artifactart4=''
    data={
        'money1':money1,
        'commonart1':commonart1,
        'commonart2':commonart2,
        'commonart3':commonart3,
        'commonart4':commonart4,
        'uncommonart1':uncommonart1,
        'uncommonart2':uncommonart2,
        'uncommonart3':uncommonart3,
        'uncommonart4':uncommonart4,
        'rareart1':rareart1,
        'rareart2':rareart2,
        'rareart3':rareart3,
        'rareart4':rareart4,
        'unrareart1':unrareart1,
        'unrareart2':unrareart2,
        'unrareart3':unrareart3,
        'unrareart4':unrareart4,
        'legendaryart1':legendaryart1,
        'legendaryart2':legendaryart2,
        'legendaryart3':legendaryart3,
        'legendaryart4':legendaryart4,
        'artifactart1':artifactart1,
        'artifactart2':artifactart2,
        'artifactart3':artifactart3,
        'artifactart4':artifactart4,
    }
    return render(request,'main/lvl_shablon.html' , data)
def level19(request):
    money1=randint(100000,1200000)
    common=randint(1,4)
    uncommon=randint(1,4)
    rare=randint(1,4)
    artifact=0
    epic=randint(1,4)
    chance=randint(1,100)
    legendary=randint(1,4)
    if chance>20 and chance<75:
            artifact=randint(1,3)
    #common#
    if common>=1:
     numm1=randint(0,7)
     commonart1=commonlist[numm1]
    else:
          commonart1='Обычные предметы отсутствуют'
    if common>=2:
     numm2=randint(0,7)
     commonart2=commonlist[numm2]
    else:
          commonart2=''
    if common>=3:
     numm3=randint(0,7)
     commonart3=commonlist[numm3]
    else:
          commonart3=''
    if common>=4:
     numm4=randint(0,7)
     commonart4=commonlist[numm4]
    else:
          commonart4=''
    #uncommon#
    if uncommon>=1:
     numm1=randint(0,48)
     uncommonart1=uncommonlist[numm1]
    else:
          uncommonart1='Необычные предметы отсутствуют'
    if uncommon>=2:
     numm2=randint(0,48)
     uncommonart2=uncommonlist[numm2]
    else:
          uncommonart2=''
    if uncommon>=3:
     numm3=randint(0,48)
     uncommonart3=uncommonlist[numm3]
    else:
          uncommonart3=''
    if uncommon>=4:
     numm4=randint(0,48)
     uncommonart4=uncommonlist[numm4]
    else:
          uncommonart4=''
    #rare#
    if rare>=1:
     numm1=randint(0,68)
     rareart1=rarelist[numm1]
    else:
          rareart1='Редкие предметы отсутствуют'
    if rare>=2:
     numm2=randint(0,68)
     rareart2=rarelist[numm2]
    else:
          rareart2=''
    if rare>=3:
     numm3=randint(0,68)
     rareart3=rarelist[numm3]
    else:
          rareart3=''
    if rare>=4:
     numm4=randint(0,68)
     rareart4=rarelist[numm4]
    else:
          rareart4=''
          #unrare(epic)#
    if epic>=1:
     numm1=randint(0,53)
     unrareart1=unrarelist[numm1]
    else:
          unrareart1='Сверхедкие предметы отсутствуют'
    if epic>=2:
     numm2=randint(0,53)
     unrareart2=unrarelist[numm2]
    else:
          unrareart2=''
    if epic>=3:
     numm3=randint(0,53)
     unrareart3=unrarelist[numm3]
    else:
          unrareart3=''
    if epic>=4:
     numm4=randint(0,53)
     unrareart4=unrarelist[numm4]
    else:
          unrareart4=''
    #legendary#
    if legendary>=1:
     numm1=randint(0,52)
     legendaryart1=legendarylist[numm1]
    else:
          legendaryart1='Легендарные предметы отсутствуют'
    if legendary>=2:
     numm2=randint(0,52)
     legendaryart2=legendarylist[numm2]
    else:
          legendaryart2=''
    if legendary>=3:
     numm3=randint(0,52)
     legendaryart3=legendarylist[numm3]
    else:
          legendaryart3=''
    if legendary>=4:
     numm4=randint(0,52)
     legendaryart4=legendarylist[numm4]
    else:
          legendaryart4=''
    #artifact#
    if artifact>=1:
     numm1=randint(0,18)
     artifactart1=artifactlist[numm1]
    else:
          artifactart1='Предметы редкости "Артефакт" отсутствуют'
    if artifact>=2:
     numm2=randint(0,18)
     artifactart2=artifactlist[numm2]
    else:
          artifactart2=''
    if artifact>=3:
     numm3=randint(0,18)
     artifactart3=artifactlist[numm3]
    else:
          artifactart3=''
    if artifact>=4:
     numm4=randint(0,18)
     artifactart4=artifactlist[numm4]
    else:
          artifactart4=''
    data={
        'money1':money1,
        'commonart1':commonart1,
        'commonart2':commonart2,
        'commonart3':commonart3,
        'commonart4':commonart4,
        'uncommonart1':uncommonart1,
        'uncommonart2':uncommonart2,
        'uncommonart3':uncommonart3,
        'uncommonart4':uncommonart4,
        'rareart1':rareart1,
        'rareart2':rareart2,
        'rareart3':rareart3,
        'rareart4':rareart4,
        'unrareart1':unrareart1,
        'unrareart2':unrareart2,
        'unrareart3':unrareart3,
        'unrareart4':unrareart4,
        'legendaryart1':legendaryart1,
        'legendaryart2':legendaryart2,
        'legendaryart3':legendaryart3,
        'legendaryart4':legendaryart4,
        'artifactart1':artifactart1,
        'artifactart2':artifactart2,
        'artifactart3':artifactart3,
        'artifactart4':artifactart4,
    }
    return render(request,'main/lvl_shablon.html' , data)
def level20(request):
    money1=randint(100000,1200000)
    common=randint(1,4)
    uncommon=randint(1,4)
    rare=randint(1,4)
    artifact=0
    epic=randint(1,4)
    chance=randint(1,100)
    legendary=randint(1,4)
    if chance>20 and chance<75:
            artifact=randint(1,4)
    #common#
    if common>=1:
     numm1=randint(0,7)
     commonart1=commonlist[numm1]
    else:
          commonart1='Обычные предметы отсутствуют'
    if common>=2:
     numm2=randint(0,7)
     commonart2=commonlist[numm2]
    else:
          commonart2=''
    if common>=3:
     numm3=randint(0,7)
     commonart3=commonlist[numm3]
    else:
          commonart3=''
    if common>=4:
     numm4=randint(0,7)
     commonart4=commonlist[numm4]
    else:
          commonart4=''
    #uncommon#
    if uncommon>=1:
     numm1=randint(0,48)
     uncommonart1=uncommonlist[numm1]
    else:
          uncommonart1='Необычные предметы отсутствуют'
    if uncommon>=2:
     numm2=randint(0,48)
     uncommonart2=uncommonlist[numm2]
    else:
          uncommonart2=''
    if uncommon>=3:
     numm3=randint(0,48)
     uncommonart3=uncommonlist[numm3]
    else:
          uncommonart3=''
    if uncommon>=4:
     numm4=randint(0,48)
     uncommonart4=uncommonlist[numm4]
    else:
          uncommonart4=''
    #rare#
    if rare>=1:
     numm1=randint(0,68)
     rareart1=rarelist[numm1]
    else:
          rareart1='Редкие предметы отсутствуют'
    if rare>=2:
     numm2=randint(0,68)
     rareart2=rarelist[numm2]
    else:
          rareart2=''
    if rare>=3:
     numm3=randint(0,68)
     rareart3=rarelist[numm3]
    else:
          rareart3=''
    if rare>=4:
     numm4=randint(0,68)
     rareart4=rarelist[numm4]
    else:
          rareart4=''
          #unrare(epic)#
    if epic>=1:
     numm1=randint(0,53)
     unrareart1=unrarelist[numm1]
    else:
          unrareart1='Сверхедкие предметы отсутствуют'
    if epic>=2:
     numm2=randint(0,53)
     unrareart2=unrarelist[numm2]
    else:
          unrareart2=''
    if epic>=3:
     numm3=randint(0,53)
     unrareart3=unrarelist[numm3]
    else:
          unrareart3=''
    if epic>=4:
     numm4=randint(0,53)
     unrareart4=unrarelist[numm4]
    else:
          unrareart4=''
    #legendary#
    if legendary>=1:
     numm1=randint(0,52)
     legendaryart1=legendarylist[numm1]
    else:
          legendaryart1='Легендарные предметы отсутствуют'
    if legendary>=2:
     numm2=randint(0,52)
     legendaryart2=legendarylist[numm2]
    else:
          legendaryart2=''
    if legendary>=3:
     numm3=randint(0,52)
     legendaryart3=legendarylist[numm3]
    else:
          legendaryart3=''
    if legendary>=4:
     numm4=randint(0,52)
     legendaryart4=legendarylist[numm4]
    else:
          legendaryart4=''
    #artifact#
    if artifact>=1:
     numm1=randint(0,18)
     artifactart1=artifactlist[numm1]
    else:
          artifactart1='Предметы редкости "Артефакт" отсутствуют'
    if artifact>=2:
     numm2=randint(0,18)
     artifactart2=artifactlist[numm2]
    else:
          artifactart2=''
    if artifact>=3:
     numm3=randint(0,18)
     artifactart3=artifactlist[numm3]
    else:
          artifactart3=''
    if artifact>=4:
     numm4=randint(0,18)
     artifactart4=artifactlist[numm4]
    else:
          artifactart4=''
    data={
        'money1':money1,
        'commonart1':commonart1,
        'commonart2':commonart2,
        'commonart3':commonart3,
        'commonart4':commonart4,
        'uncommonart1':uncommonart1,
        'uncommonart2':uncommonart2,
        'uncommonart3':uncommonart3,
        'uncommonart4':uncommonart4,
        'rareart1':rareart1,
        'rareart2':rareart2,
        'rareart3':rareart3,
        'rareart4':rareart4,
        'unrareart1':unrareart1,
        'unrareart2':unrareart2,
        'unrareart3':unrareart3,
        'unrareart4':unrareart4,
        'legendaryart1':legendaryart1,
        'legendaryart2':legendaryart2,
        'legendaryart3':legendaryart3,
        'legendaryart4':legendaryart4,
        'artifactart1':artifactart1,
        'artifactart2':artifactart2,
        'artifactart3':artifactart3,
        'artifactart4':artifactart4,
    }
    return render(request,'main/lvl_shablon.html' , data)