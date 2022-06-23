from Question import Question

Spanish_Questions = ['Como','Mientras','Con','Cual','Donde','y','Que','Por que','Cuando','Pero','Para','El or La','En','Mas','Muy','Tambien','Nuevo','Nada','Menos','Ahora','Bien','Nestro','Tanto','Entre','Dia','Año ']

prompts = [Question(Spanish_Questions[0], 'How'),
            Question(Spanish_Questions[1], 'While'),
            Question(Spanish_Questions[2], 'Wtih'),
            Question(Spanish_Questions[3], 'Which'),
            Question(Spanish_Questions[4], 'Where'),
            Question(Spanish_Questions[5], 'And'),
            Question(Spanish_Questions[6], 'What'),
            Question(Spanish_Questions[7], 'Why'),
            Question(Spanish_Questions[8], 'When'),
            Question(Spanish_Questions[9], 'But'),
            Question(Spanish_Questions[10], 'For'),
            Question(Spanish_Questions[11], 'The'),
            Question(Spanish_Questions[12], 'In'),
            Question(Spanish_Questions[13], 'More'),
            Question(Spanish_Questions[14], 'Very'),
            Question(Spanish_Questions[15], 'Also'),
            Question(Spanish_Questions[16], 'New'),
            Question(Spanish_Questions[17], 'Nothing'),
            Question(Spanish_Questions[18], 'Less'),
            Question(Spanish_Questions[19], 'Now'),
            Question(Spanish_Questions[20], 'Well'),
            Question(Spanish_Questions[21], 'Our'),
            Question(Spanish_Questions[22], 'Much'),
            Question(Spanish_Questions[23], 'Between'),
            Question(Spanish_Questions[24], 'Day'),
            Question(Spanish_Questions[25], 'Year')]



def run_test(prompts):
  score = 0
  for question in prompts:
    answer = input(question.prompt)
    if answer == question.answer:
      score += 1
    print('You got ' + str(score) + '/' +str(len(prompts)) + 'correct')

run_test(prompts)