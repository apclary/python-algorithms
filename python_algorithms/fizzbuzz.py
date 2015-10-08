def fizzbuzz():
    for i in range(1,101):
        message = ''
        if i % 3 == 0:
            message += 'Fizz'
        if i % 5 == 0:
            message += 'Buzz'
            
        if message:
            print(message)
        else:
            print(i)
         
if __name__ == '__main__':
    fizzbuzz()