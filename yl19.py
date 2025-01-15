import json
kl10 = 0
kl11 = 0
kl12 = 0
with open('haridustulemused.json', 'r', encoding='utf-8') as file:
    opilased = json.load(file)

for opilane in opilased:
    if opilane ['klass'] == '10':
        kl10+=1 
        print (opilane['klass'])
        for tegvus in opilane['tegevused']:
            print(tegvus)
        for aine, punktid in opilane ['hinded'].items():
	        print(f"{aine}: {punktid}")

        print (['-------------------'])

    if opilane ['klass'] == '11':
        kl11+=1  
    if opilane ['klass'] == '12':
        kl12+=1 
print(f"10 klassis õpib {kl10} õpilast")
print(f"11 klassis õpib {kl11} õpilast")
print(f"12 klassis õpib {kl12} õpilast")

