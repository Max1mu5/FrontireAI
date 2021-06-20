import neuro
import parse

print("------FrontAI------\n")

print("Введите поисковый запрос: ", end='')
req = input()
parse.create_dataset(req)

print("Полученные фронтиры: ", end='')
res = [i.split('_')[0] for i in neuro.main()]
for i in res:
  print(i, end=', ')


print("\n------FrontAI------\n\n\n")