
#imports
import Casa_de_Hogwarts as casas_hogwarts
import Pregunta_1_a_10 as primer_quiz
import Pregunta_11_a_20 as segundo_quiz
import Pregunta_21_a_30 as tercer_quiz
import Pregunta_31_a_40 as cuarto_quiz
import random as rd

#🧙‍♂️📚🏰 Bienvenido al Quiz magico del universo de Harry Potter 🧙‍♂️📚🏰
while True:
    print("""
╔═════════════════════════════════════════════════════════════════╗
║                                                                 ║
║        🧙‍♂️📚🏰 Bienvenido joven hechicero/a al 🧙‍♂️📚🏰          ║
║    🧙‍♂️📚🏰 Quiz mágico del universo de Harry Potter 🧙‍♂️📚🏰     ║
║                                                                 ║
║    🧙‍♂️🔮 Escoge con sabiduría, joven aprendiz de mago. 🧙‍♂️🔮    ║
║                                                                 ║
╚═════════════════════════════════════════════════════════════════╝

1) 10 Preguntas sobre el universo de Hp⚡.
2) El Sombrero Seleccionador🎩.
3) Sellar el Grimorio🔒📕.
""")
    op = int(input("¿Por donde quieres comenzar? :"))
    if op == 1:
        preguntas = [primer_quiz, segundo_quiz, tercer_quiz, cuarto_quiz]
        azar = rd.choice(preguntas)
        azar.main()
    elif op == 2:
        casas_hogwarts.main()
    elif op == 3:
        print("""
Hasta que nos volvamos a encontrar en el andén 9¾.
       🧙‍♂️🧙‍♀️✨ Finite Incantatem ✨🧙‍♀️🧙‍♂️
""")
        break
    else:
        print("""
🤔📚 No comprendo lo que quieres pequeño aspirante a mago 📚🤔
""")