#Says hi to you when you say hi and introduce yourself

def talkback(sentence):
  x = (sentence.find('is'))
  name_starts = x + 3
  y = sentence.find(' ',name_starts)
  name_ends = y
  if name_ends == -1:
	  name = sentence[name_starts:]
	  print('Hello %s' %name)
  elif name_ends != -1 and x ==-1:
    print('Sorry I can not talk right now')
  else:
    name = sentence[name_starts:name_ends]
    print('Hello %s' %name)
    
sentence1 = 'Hi my name is Name'
talkback(sentence1)
