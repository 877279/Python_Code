def State_Quiz():

  print('Welcome to the States Quiz!')

  Question1 = input('What is the capitol of England?')

  Question1 = str.lower(Question1)

  if Question1 == 'london':

   print('Correct')

  else:

    print('Try again and Remember to have correct PUNCTUATION')

  Question2 = input('What is the capitol of the USA?')

  Question2 = str.lower(Question2)

  if Question2 == 'washington dc' and 'washington d.c' and 'washington d.c.':
    print('Correct')

  else:
 
    print('Try again and Remember to have correct PUNCTUATION')

  Question3 = input('What is the capitol of France?')

  Question3 = str.lower(Question3)

  if Question3 == 'paris':

    print('Correct')

  else:

    print('Try again and Remember to have correct PUNCTUATION')

  if Question1 == 'london' and Question2 == 'washington dc' and 'washington d.c' and 'washington d.c.'and Question3 == 'paris':

    print ('Great Job! You got them all correct')

  else:
 
    print('Try harder next time!')
 
  
State_Quiz()
