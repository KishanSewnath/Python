studentenCijfers = [[95, 92, 86], [66, 75, 54],
                     [89, 72, 100], [34, 0, 0]]
student_gemiddelde = []

def gemiddelde_per_student(studentencijfers):

    for lijst in studentenCijfers:
        cijfer_student = sum(lijst)/len(lijst)
        student_gemiddelde.append(cijfer_student)

    print(student_gemiddelde)

gemiddelde_per_student(studentenCijfers)

def gemiddelde(studentencijfers):
    gemidelde_totaal = (sum(student_gemiddelde)/len(studentenCijfers))
    print(gemidelde_totaal)

gemiddelde(studentenCijfers)
