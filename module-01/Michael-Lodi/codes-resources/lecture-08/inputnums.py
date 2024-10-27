# reply = input('Enter text (or "stop"): ')
# while reply != 'stop':
#     if not reply.isdigit():
#         print('Bad!' * 8)
#     else:
#         print(int(reply) ** 2)
#     reply = input('Enter text (or "stop"): ')
# print('Bye')

## Now formulated with try/except
reply = input('Enter text (or "stop"): ')
while reply != 'stop':
    try:
        print(int(reply) ** 2)
    except ValueError:
        print('Bad!' * 8)
    reply = input('Enter text (or "stop"): ')
print('Bye')
