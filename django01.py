print('Hello World')


if 3 > 2:
    print('It works')


volume = 10
if volume < 20 or volume > 80:
    volume = 50
    print("That's better!")


def hi():
    print('Hi there!')
    print('How are you?')

hi()


def greet(name):
    print('Hi %s!' % name)

greet('Reka')


girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    greet(name)


for i in range(1,6):
    print(i)