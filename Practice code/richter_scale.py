n = float(input("Richter Scale Number: "))
if n < 5.0:
    print("little or no damage")
elif n >= 5.0 and n < 5.5:
    print("some damage")
elif n >= 5.5 and n < 6.5:
    print("serious damage: walls may crack or fall")
elif n >= 6.5 and n < 7.5:
    print("disaster: houses and buildings may collapse")
elif n >= 7.5:
    print("catastrophe: most buildings destroyed")
    
