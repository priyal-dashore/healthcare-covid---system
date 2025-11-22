def covid_risk_checker():
    print("=== covid-19 symptom checker ===")
    score = 0
    fever = input("do you have fever?(yes/no:)").lower()
    cough=input("do you have cough?(yes/no:)").lower()
    breath=input("do you have difficulty in breathing?(yes/no:)").lower()
    sore=input("do you have sour throat?(yes/no:)").lower()
    tired=input("are you feeling tired or weak").lower()
    contact=input("have you meet a covid patient recently?(yes/no)").lower()
    travel=input("have you travel in last 14 days?(yes/no)").lower()
    vaccine=input("are you fully vaccinated(yes/no)").lower()

    if fever == "yes": score+=2
    if cough == "yes": score+=2
    if breath == "yes": score+=3
    if sore=="yes": score+=1
    if tired=="yes": score+=1
    if contact=="yes": score+=3
    if travel=="yes": score+=2
    if vaccine=="no":score+=2

    if score<=3:
        risk = "low risk"
        advice = "Monitor symptoms and follow covid precautions"
    elif score <=7:
        risk="Moderate risk"
        advice="take rest and consider consulting doctor"
    else:
        risk = "high risk"
        advice="seek medical attension immediately and get tested"
    print("\n---covid risk report---")
    print("your total score:", score)
    print("risk level:",risk)
    print("advice:",advice)

covid_risk_checker()
