class Day :
    def __init__(self, x) :
        self.name = x
        self.lessons = []

    def add(self, inp):
        self.lessons.append(inp)

class Week :
    def __init__(self) :
        self.days = [Day(name) for name in ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']]

    def add(self, name, lesson) :
        for day in self.days :
            if day.name == name :
                day.add(lesson)
                break

week = Week()
'''week.add('Пн', 'Каникулы')
week.add('Вт', 'Выходной')
week.add('Ср', 'Физкультура')
week.add('Ср', 'Четверг')
week.add('Ср', 'обществознания')
week.add('Чт', 'Отпуск')'''

week.add('Пн', 'Kanikuli')
week.add('Вт', 'Vyhodnoi')
week.add('Ср', 'FiZra')
week.add('Ср', 'Chetverg')
week.add('Ср', 'Obschestvosnaniya')
week.add('Чт', 'Otpusk')

for day in week.days:
    print(f'Raspisaniye {day.name}:')
    for lesson in day.lessons:
        print(f'Lesson: {lesson}')
