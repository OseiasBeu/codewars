def pig_it(text):
    #your code here
    text_array = text.split()
    new_text = ''
    for word in text_array:       
        new_word = word[1:]
        new_word = new_word+word[0]+'ay'
        new_text = new_text +' '+ new_word
    
    if new_text.find('!') != -1 or new_text.find('?') != -1:
        new_text = new_text[:-2]
    return new_text.lstrip()


print(pig_it('Pig latin is cool')) # Return: 'igPay atinlay siay oolcay'
print(pig_it('This is my string')) #Return: 'hisTay siay ymay tringsay'
print(pig_it( "O tempora o mores !")) #return: 'Oay emporatay oay oresmay !'
print(pig_it( "Nunc est bibendum"))  #return:  'uncNay steay ibendumbay'
print(pig_it( "Quis custodiet ipsos custodes ?"))  #return:  'uisQay ustodietcay psosiay ustodescay ?'
print(pig_it('Barba non facit philosophum')) #return: 'arbaBay onnay acitfay hilosophumpay'
