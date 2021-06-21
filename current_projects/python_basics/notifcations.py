def yell(text):
    text = text.upper()
    number_of_characters = len(text)
    result = text + "!" * (number_of_characters //2)
    print(result)




advice = "Don't forget to ask for help"



advice2 = "Don't. Repeat. Yourself. Keep things DRY"

yell(advice)
yell(advice2)
