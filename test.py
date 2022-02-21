# answers = {'5*5': '25'}

# print('question: ', list(answers.keys())[0])
# print('answer: ', list(answers.values())[0])

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

ballList.sort(key = lambda c: c.radius, reverse=True)