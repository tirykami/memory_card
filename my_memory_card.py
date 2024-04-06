#Импорт модулей
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout,
        QGroupBox, QButtonGroup, QRadioButton,
        QPushButton, QLabel, QMessageBox)
from random import shuffle

#Сoздаем класс Вопрос
class Question():
        def __init__(self, question, right_answer,wrong1,wrong2,wrong3):
                self.question = question
                self.right_answer = right_answer
                self.wrong1 = wrong1
                self.wrong2 = wrong2
                self.wrong3 = wrong3
#Список вопросов
questions_list = [] 
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))  
questions_list.append(Question('Как называется еврейский Новый год?', 'Рош ха-Шана ', 'Ханука', 'Йом Кипур', 'Кванза'))  
questions_list.append(Question('Сколько звезд на флаге США?', '50', '20', '51', '41'))
questions_list.append(Question('Какая самая редкая группа крови?', "IV группа", "III группа", "II группа", "I группа"))
questions_list.append(Question('Сколько костей в теле человека?', "205", "256", "198", "274"))  
questions_list.append(Question('Сколько сердец у осьминога?', "3", "5", "1", "4")) 
questions_list.append(Question('Какая страна потребляет больше всего шоколада?', "Швейцария", "Бельгия", "Швеция", "Бразилия")) 
questions_list.append(Question('Сколько элементов в таблице Менделеева?', "118", "133", "108", "98")) 
questions_list.append(Question('При какой температуре по Фаренгейту замерзает вода?', "32", "33", "28", "-6")) 
questions_list.append(Question('Сколько ребер в теле человека?', "24", "27", "16", "23")) 
questions_list.append(Question('Сколько часовых поясов в мире?', "24", "12", "14", "18")) 
questions_list.append(Question('Какова длина олимпийского бассейна (в метрах)?', "50", "48", "52", "36")) 
questions_list.append(Question('Какой напиток потребляют больше всего в мире?', "Чай", "Coca-cola", "Fanta", "Кофе")) 
questions_list.append(Question('Что расшифровывается WWW в браузере веб-сайтов?', "World Wide Web", "Write White Wall", "Что это?", "Warm Weather"))
questions_list.append(Question('Какой элемент в таблице Менделеева обозначается химическим символом Sn?', "Олово", "Золото", "Уран", "Железо"))
questions_list.append(Question('Какой стране принадлежит Гренландия?', "Дании", "Швеции", "Ватикану", "Японии"))
questions_list.append(Question('Что такое H2O?', "Вода", "Кислород", "Азот", "Водород"))
questions_list.append(Question('Какой элемент таблицы Менделеева имеет атомный номер 290?', "Московий", "Золото", "Платина", "Гелий"))
questions_list.append(Question('Как расшифровывается марка автомобилей BMW?', "Bayerische Motoren Werke", "Mersedes", "Audi", "Bread White Milk "))
questions_list.append(Question('Создатель языка программирования Python?', "Гвидо ван Россум", "Билл Гейтс", "Я", "Брендан Эйх"))
questions_list.append(Question('Сколько километров всреднем проходит человек за жизнь?', "~220000", "~10000", "~60", "~1200000"))
questions_list.append(Question('Сколько часовых поясов в России?', "11", "24", "1", "8"))
questions_list.append(Question('Самый населенный город в Европе?', "Москва", "Лондон", "Париж", "Люксембург"))
shuffle(questions_list)

#Создание приложения
app = QApplication([])

scoreWin = QMessageBox()
questionAll = QMessageBox()
questionRight = QMessageBox()

btn_OK = QPushButton('Ответить') #Кнопка Ответить
lb_Question = QLabel('Самый сложный вопрос в мире!') #Текст вопроса


RadioGroupBox = QGroupBox("Варианты ответов") #Группа вариантов ответа

#Кнопки-переключатели
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

#Добавление кнопок в группу
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

#Выравнивание виджетов по лайаутам
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

#Добавление группы на лайаут

RadioGroupBox.setLayout(layout_ans1)


AnsGroupBox = QGroupBox("Результат теста") #Группа результатов ответа на вопрос
lb_Result = QLabel('прав ты или нет?') #Надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') #Ответ на вопрос

#Выравнивание группы ответов по лайауту
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res) #добавление группы на лайаут

#Создание горизонтальных лэйаутов

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

#Добавление виджетов на лайауты

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide() #Скрытие группы


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)


layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым

def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос') #Изменение надписи на кнопке ОТВЕТИТЬ на СЛЕДУЮЩИЙ ВОПРОС
    


def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить') #Изменение надписи на кнопке с СЛЕДУЮЩИЙ ВОПРОС на ОТВЕТИТЬ
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана

#Список кнопок-ответов
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

#Функция задавания вопросов
def ask(q: Question):
        shuffle(answers) #Перемешать варианты ответа
        answers[0].setText(q.right_answer)
        answers[1].setText(q.wrong1)
        answers[2].setText(q.wrong2)
        answers[3].setText(q.wrong3)
        lb_Question.setText(q.question) #Поменять текст вопроса
        lb_Correct.setText(q.right_answer) #Показать правильный ответ
        show_question() #Показать вопрос

#Функция показа правильного ответа
def show_correct(res):
        lb_Result.setText(res)
        show_result()
#Функция переключения вопроса на следующий
def next_question():
        a = 0
        #cur_question = randint(0, len(questions_list) - 1) # Перемешиваем порядок вопросов
        q = questions_list[a]
        a += 1
        window.total += 1
        questions_list.pop(0)
        ask(q)
        window.resize(300,300)
#Функция реакции на нажатие кнопок ОТВЕТИТЬ или СЛЕДУЮЩИЙ ВОПРОС
def click_OK():
        if btn_OK.text() == "Ответить": #если надпись на кнопке равна ОТВЕТИТЬ
                check_answer()
        else:
                next_question()
#Функция проверки ответа
def check_answer():
        if answers[0].isChecked():
                show_correct("Правильно!")
                window.score += 1
                questionAll.setText('Всего вопросов: ' + str(window.total))
                questionAll.exec_()
                questionRight.setText('Всего правильных ответов: ' + str(window.score))
                questionRight.exec_()
                scoreWin.setText('Ваш рейтинг: '+ str((window.score / window.total) * 100) + '%')
                scoreWin.exec_()
        else:
                if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
                        show_correct("Неверно")
                        questionAll.setText('Всего вопросов: ' + str(window.total))
                        questionAll.exec_()
                        questionRight.setText('Всего правильных ответов: ' + str(window.score))
                        questionRight.exec_()
                        scoreWin.setText('Ваш рейтинг: '+ str((window.score / window.total) * 100) + '%')
                        scoreWin.exec_()


window = QWidget()
window.total = 0
window.score = 0
window.resize(300,300) #Изменить размер приложения на 300/300 пикс.
window.setLayout(layout_card)
window.setWindowTitle('Memory Card') #Изменение названия приложения на Memory Card
next_question()
btn_OK.clicked.connect(click_OK) # проверяем, что панель ответов показывается при нажатии на кнопку

window.cur_question = -1

window.show() #Показать окно приложения
app.exec() #Возможность закрыть приложение нажатием на красный крестик


               ######          ######                                                  
             ###########    ###########                         
            ############################
             ##########################                       
              ########################                       
                ####################                         
                  ################                               
                    ############                              
                      ########
                        ####

                      
                   

                       ####             ####
                       #|##             #|##            
                       #||#             #||#
                       ####             ####
                                     
                 ##|                           |##
                 ##|                           |##
                  ##\                         /##
                   ###\                     /###
                     ####\               /####
                        ####\_________/####
                            ###########


                                              ####
                                            ###  \     
                                           ##     \
                                          ##       \ 
                          ###/           ##         \           /#####
                         ##/             #           \       /#######
                        ##|--------------#------------|----########
                         ##\             #           /      \########
                          ###\           ##         /           \#####
                                          ##       /   
                                           ##     /   
                                            ###  /  
                                              ####  
                                               


                #####                   #####
                #   #                   #   #
                #   #                   #   #
                #   #                   #   #
                #   #                   #   #
                #####                   #####

                     ###################


