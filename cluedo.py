#Alwin Wezenbeek 99060433

print('welkom bij de castingbureau, ik stel u een aantal vragen of u geschikt bent voor een auditie.')
naam = input('wat is je naam?: ')
man_of_vrouw = input('wat is je geslacht? (man of vrouw): ')
leeftijd = int (input('wat is je leeftijd?: '))
gewicht = int (input('hoeveel weeg je in kg?: '))
lengte = int (input('hoelang ben je in cm?: '))
haar_kleur = input('wat voor kleur is je haar?: ')
diploma = input('beschikt u over een diploma in acteren? (ja of nee): ')
bril = input('draagt u een bril? (ja of nee): ')


dominee_groenewoud = 'Je mag op auditie voor de rol van Dominee Groenewoud'
kolonel_van_geelen = 'Je mag op auditie voor de rol van Kolonel van Geelen'
mevrouw_de_wit = 'Je mag op auditie voor de rol van Mevrouw de Wit'
rosa_roodhart = 'Je mag op auditie voor de rol van Rosa Roodhart'
prof_pimpel = 'Je mag op auditie voor de rol van Professor Pimpel'
mevrouw_blaauw_van_draet = 'Je mag op auditie voor de rol van Mevrouw Blaauw van Draet'
geen_auditie = 'je mag helaas niet op auditie.'

if leeftijd < 18 or diploma == 'nee':
    print(geen_auditie)

if man_of_vrouw == 'man' and diploma == 'ja' and leeftijd >= int(50) and gewicht >= int(90) and lengte <= int(170) and bril == 'nee' and haar_kleur == 'wit':
    print(dominee_groenewoud)

if man_of_vrouw == 'man' and diploma == 'ja' and leeftijd >= int(50) and gewicht >= int(70) and lengte >= int(180) and bril == 'ja' and haar_kleur == 'grijs':
    print(prof_pimpel)

if man_of_vrouw == 'man' and diploma == 'ja' and leeftijd >= int(30) and gewicht >= int(70) and lengte >= int(180) and bril == 'nee' and haar_kleur == 'grijs':
    print(kolonel_van_geelen)

if man_of_vrouw == 'vrouw' and diploma == 'ja' and leeftijd >= int(60) and gewicht >= int(90) and lengte >= int(160) and bril == 'nee' and (haar_kleur == 'grijs' or haar_kleur == 'wit'):
    print(mevrouw_de_wit)

if man_of_vrouw == 'vrouw' and diploma == 'ja' and leeftijd >= int(18) and gewicht >= int(60) and lengte >= int(160) and bril == 'nee' and haar_kleur == 'zwart':
    print(rosa_roodhart)

if man_of_vrouw == 'vrouw' and diploma == 'ja' and leeftijd >= int(30) and gewicht >= int(60) and lengte >= int(170) and bril == 'ja' and haar_kleur == 'blond':
    print(mevrouw_blaauw_van_draet)














