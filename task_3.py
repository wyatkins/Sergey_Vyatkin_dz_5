tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей','Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б']


def chek_gen():

    len_klasses = len(klasses)

    return ((tut, klasses[i])
            if i < len_klasses else (tut, None)
            for i, tut in enumerate(tutors))


if __name__ == '__main__':

    gen = chek_gen()
    print(type(gen))
    print(*gen)