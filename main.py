from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton, QButtonGroup

from random import shuffle, randint

'''
СТРУКТУРА ПРОЕКТА

1. Описание всех классов и всех функций

- класс Question
    содержит вопрос
    содержит правильный ответ
- функция ask
    принимает в качестве аргумента новый вопрос и варианты ответов.
    меняет вопрос на экране приложения.
- функция check_answer
    проверяет правильность ответа.
    скрывает форму с вопросом и показывает форму с информацией об ответе.
- функция show_question
    выбирает новый вопрос.
    обнуляет радио-кнопки.
    вызывает ask.
    скрывает форму ответа и показывает форму с новым вопросом
- функция show_choice 
    по надписи на кнопке выбирает, вызвать check_answer или show_question

2. Основная часть программы

    1. создание списка вопросов минимум с 3мя вопросами (экземплярами класса Question)
    2. создание приложения и главного окна приложения
    3. создание total и score КАК СВОЙСТВ ОКНА (чтобы можно было обращаться к ним из любой части программы)
    4. создание всех элементов главного окна
        1) надпись-лэйбл с вопросом
        2) группа виджетов с надписью "Варианты ответов" (мы называем её форма вопроса)
        3) радио-кнопки с ответами (их надо поместить в список)
        4) группа радио-кнопок
        5) push-кнопка (push = на неё можно нажать)
        6) группа виджетов с надписью "Результат теста" (мы называем её форма ответа)
        7) надпись-лэйбл с результатом (Правильно / Неправильно)
        8) надпись-лэйбл с правильным ответом)
        лэйауты для формы вопроса (включают в себя пункты 2,3,4)
        лэйауты для формы ответа (включают в себя пункты 6,7,8)
        лэйаут всего окна (включает в себя форму вопроса, форму ответа и пункты 1,5)
    5. отображение нужного лэйаута в форме вопроса
    6. отображение нужного лэйаута в форме ответа
    7. отображение нужного лэйаута в окне приложения
    8. скрыть форму ответа
    9. связывание события "Нажатие на push-кнопку" с функцией-реакцией на это событие
    10. отображение главного окна и закрытие приложения при нажатии на крестик     

'''


class Question():
    def __init__(self, question, right_answ, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answ = right_answ
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


def ask(q):
    # меняем название самого вопроса
    label_name.setText(q.question)
    shuffle(answers)    # answers - это список радио-кнопок
    # меняем варианты ответов
    answers[0].setText(q.right_answ)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    # меняем лэйбл с правильным ответом
    label_answ.setText('Правильный ответ: ' + q.right_answ)

# check_answer - функция, которая скрывает форму вопроса и показывает форму ответа с проверкой

def check_answer():
    if answers[0].isChecked():
        label_check.setText('Правильно')
        main_win.score += 1

        print('Всего ответов:', main_win.total)
        print('Из них правильно:', main_win.score)

        print('Рейтинг:', main_win.score / main_win.total * 100, '%')
    else:
        label_check.setText('Неправильно')

    RadioGroupBox.hide()
    AnswGroupBox.show()
    button.setText('Следующий вопрос')

# show_question - функция, которая скрывает форму ответа и показывает форму вопроса с новым вопросом

def show_question():
    main_win.total += 1

    print('Всего ответов:', main_win.total)
    print('Из них правильно:', main_win.score)

    # в этой части программы мы выбираем, какой вопрос вывести в приложение
    cur_question = randint(0, len(question_list) - 1)

    # а здесь мы выводим выбранный вопрос
    ask(question_list[cur_question])

    RadioGroup.setExclusive(False)
    r1.setChecked(False)
    r2.setChecked(False)
    r3.setChecked(False)
    r4.setChecked(False)
    RadioGroup.setExclusive(True)

    AnswGroupBox.hide()
    RadioGroupBox.show()
    button.setText('Ответить')

def show_choice():
    if button.text() == 'Ответить':
        check_answer()
    else:
        show_question()

# создание списка вопросов

question_list = []

q1 = Question('Какой национальности не существует? вопрос 1', 'Смурфы', 'Энцы', 'Алеуты', 'Чулымцы')
q2 = Question('Сколько материков на Земле? вопрос 2', '6', '5', '7', '8')
q3 = Question('Сколько будет 2+2*2? вопрос 3', '6', '8', '5', '10')
q4 = Question('Зимой и летом одним цветом. вопрос 4', 'Ель', 'Картофель', 'Снеговик', 'Сок')

question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)

# создание приложения и главного окна

app = QApplication([])
main_win = QWidget()

# свойство окна: текущий вопрос

main_win.total = 0
main_win.score = 0

# создание элементов главного окна

# создание надписи вопроса
label_name = QLabel()

# создание первой группы виджетов для формы вопроса RadioGroupBox
RadioGroupBox = QGroupBox("Варианты ответа")

# создание радио-кнопок
r1 = QRadioButton()
r2 = QRadioButton()
r3 = QRadioButton()
r4 = QRadioButton()

# создание списка радио-кнопок
answers = [r1, r2, r3, r4]

# создание группы радио-кнопок
RadioGroup = QButtonGroup()
RadioGroup.addButton(r1)
RadioGroup.addButton(r2)
RadioGroup.addButton(r3)
RadioGroup.addButton(r4)

# создание push кнопки
button = QPushButton("Ответить")

# создание первого вертикального лэйаута с двумя ответами
layoutV1 = QVBoxLayout()
layoutV1.addWidget(r1)
layoutV1.addWidget(r2)

# создание второго вертикального лэйаута с двумя ответами
layoutV2 = QVBoxLayout()
layoutV2.addWidget(r3)
layoutV2.addWidget(r4)

# создание горизонтального лэйаута с четырьмя ответами
layoutH = QHBoxLayout()

layoutH.addLayout(layoutV1)
layoutH.addLayout(layoutV2)

# отображение горизонтального лэйаута в группе виджетов
RadioGroupBox.setLayout(layoutH) # RadioGroupBox - это форма вопроса

# создание второй группы виджетов для формы ответа AnswGroupBox

AnswGroupBox = QGroupBox("Результат теста")

label_check = QLabel('Правильно/Неправильно')
label_answ = QLabel('Правильный ответ')

layout_new = QVBoxLayout()

layout_new.addWidget(label_check)
layout_new.addWidget(label_answ)

AnswGroupBox.setLayout(layout_new)

# вызов функции для установки первого вопроса и вариантов ответа

show_question()

# последний лэйаут для расположения всех элементов в окне вместе с формой вопроса или ответа

layoutV_last = QVBoxLayout()
layoutV_last.addWidget(label_name)
layoutV_last.addWidget(RadioGroupBox)
layoutV_last.addWidget(AnswGroupBox)
layoutV_last.addWidget(button)

# скрываем форму ответа

AnswGroupBox.hide()

# связываем событие нажатия на кнопку с функцией show_choice

button.clicked.connect(show_choice)

# отображаем последний лэйаут и оставляем окно открытым

main_win.setLayout(layoutV_last)
main_win.show()
app.exec_()




