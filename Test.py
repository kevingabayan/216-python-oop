from KnightErrant import KnightErrant
from Warrior import Warrior
from Fighter import Fighter
from Fight import Fight
from Person import Person

"""

All possibilities

Fighter vs. Fighter (Done)
Fighter vs. Warrior, Knight Errant W [Same as Fighter v. Knight Errant, diff. skill/wealth]
Fighter vs. Warrior, Fighter W [Same as Fighter v. Knight Errant, diff. skill/wealth]
Fighter vs. Knight Errant, Fighter W (Done)
Fighter vs. Knight Errant, Knight Errant W (Done)

Warrior vs. Warrior (Done)
Warrior vs. Fighter, Fighter W (Done)
Warrior vs. Fighter, Warrior W (Done)
Warrior vs. Knight Errant, Warrior W (Done)
Warrior vs. Knight Errant, Knight Errant W (Done)

Knight Errant vs. Knight Errant (Done)
Knight Errant vs Fighter, Fighter W [Same as all others, except positions are reversed... code is the same]
Knight Errant vs. Fighter, Knight Errant W [Same as all others, except positions are reversed... code is the same]
Knight Errant vs. Warrior, Knight Errant W [Same as all others, except positions are reversed... code is the same]
Knight Errant vs. Warrior, Warrior W [Same as all others, except positions are reversed... code is the same]

Error Cases
Traveling (Done)
Challenge Invitations (Done)
Initializations (Done)

"""


print("Error creation for when a Fighter is too young")
Xerath = KnightErrant("Xerath", 5, 8, 8, 8, 8, 8)

# Person initialization
Stella = Person("Stella", 18, 21)

# Fighter initializations
Saitama = Fighter("Saitama", 25, 100, 1, 9, 1, 1)
Boros = Fighter("Boros", 25, 5, 1,  1, 1, 1)
Bruce = Fighter("Bruce", 21, 10, 10, 10, 10, 10)
Brokeboy = Fighter("Brokeboy", 21, 0, 0, 0, 0, 0)
Darius = Fighter("Darius", 30, 400, 0, 0, 0, 9)
Garen = Fighter("Garen", 35, 500, 0, 0, 0, 9)
Helmet_Bro = Fighter("Helmet Bro", 25, 500, 0, 0, 0, 0)
Pantheon = Fighter("Pantheon", 25, 500, 8, 0, 0, 0)
Elise = Fighter("Elise", 25, 500, 5, 0, 0, 0)
Haise = Fighter("Haise", 25, 500, 5, 5, 5, 5)

# Warrior initializations
Lee_Sin = Warrior("Lee Sin", 25, 1000, 5, 8, 5, 5)
Mordekaiser = Warrior("Mordekaiser", 25, 1000, 5, 5, 8, 5)
Touka = Warrior("Touka", 21, 9, 9, 9, 9, 9)
Kaneki = Warrior("Kaneki", 200, 993, 9, 5, 9, 9)

# Knight-Errant initializations
Arthur = KnightErrant("Arthur", 20, 500, 0, 0, 0, 10)
Anakin = KnightErrant("Anakin", 20, 500, 0, 0, 0, 10)
Arima = KnightErrant("Arima", 21, 59, 9, 5, 9, 10)
# Error Cases

# Trying to fight yourself
Bruce.challenge(Bruce, "unarmed combat")
# Trying to fight a person
Bruce.challenge(Stella, "unarmed combat")
# Trying to fight a broke individual
Bruce.challenge(Brokeboy, "unarmed combat")
# Trying to fight as a broke individual
Brokeboy.challenge(Bruce, "spear")

# Fighter test cases, prints before and after values for whether or not a skill was increased, what their wealth was
# before and after, etc...
print('\n')
print("Fighter vs. Fighter Interactions")

print('\n')
print("1. Saitama vs. Boros, fist fight (Saitama is Victorious)")
print("Skill values: Boros and Saitama, respectively")
print(str(Boros.get_skill_value("unarmed combat")))
print(str(Saitama.get_skill_value("unarmed combat")))
print("Wealth values: Boros and Saitama, respectively")
print(str(Boros.wealth))
print(str(Saitama.wealth))
Boros.challenge(Saitama, "unarmed combat")
print("Skill values: Boros and Saitama, respectively")
print(str(Boros.get_skill_value("unarmed combat")))
print(str(Saitama.get_skill_value("unarmed combat")))
print("Wealth values: Boros and Saitama, respectively")
print(str(Boros.wealth))
print(str(Saitama.wealth))

print('\n')
print("2. Darius vs. Garen, equal footing!(Luck prevails!)")
print("Skill values: Darius and Garen, respectively")
print(str(Darius.get_skill_value("broadsword")))
print(str(Garen.get_skill_value("broadsword")))
print("Wealth values: Darius and Garen, respectively")
print(str(Darius.wealth))
print(str(Garen.wealth))
Darius.challenge(Garen, "broadsword")
print("Skill values: Darius and Garen, respectively")
print(str(Darius.get_skill_value("broadsword")))
print(str(Garen.get_skill_value("broadsword")))
print("Wealth values: Darius and Garen, respectively")
print(str(Darius.wealth))
print(str(Garen.wealth))

print('\n')
print("3. Helmet Bro vs. Pantheon (Pantheon prevails!)")
print("Skill values: HB and Pantheon, respectively")
print(str(Helmet_Bro.get_skill_value("spear")))
print(str(Pantheon.get_skill_value("spear")))
print("Wealth values: HB and Pantheon, respectively")
print(str(Helmet_Bro.wealth))
print(str(Pantheon.wealth))
Helmet_Bro.challenge(Pantheon, "spear")
print("Skill values: HB and Pantheon, respectively")
print(str(Helmet_Bro.get_skill_value("spear")))
print(str(Pantheon.get_skill_value("spear")))
print("Wealth values: HB and Pantheon, respectively")
print(str(Helmet_Bro.wealth))
print(str(Pantheon.wealth))

print('\n')
print("Fighter vs. Warrior Interactions")

print('\n')
print("4. Normal Warrior to Fighter Challenge (50/50)")
print("Skill values: Elise and Lee Sin, respectively")
print(str(Elise.get_skill_value("spear")))
print(str(Lee_Sin.get_skill_value("spear")))
print("Wealth values: Elise and Lee Sin, respectively")
print(str(Elise.wealth))
print(str(Lee_Sin.wealth))
Lee_Sin.challenge(Elise, "spear")
print("Skill values: Elise and Lee Sin, respectively")
print(str(Elise.get_skill_value("spear")))
print(str(Lee_Sin.get_skill_value("spear")))
print("Wealth values: Elise and Lee Sin, respectively")
print(str(Elise.wealth))
print(str(Lee_Sin.wealth))

print('\n')
print("5. Error checking for challenge invitations.")
fight = Fight(Elise, Lee_Sin, "unarmed combat")
Elise.withdraw(Lee_Sin, fight)
print("Issuing a normal challenge")
Elise.challenge(Lee_Sin, "unarmed combat")
print("Issuing a challenge more than once with the same skill")
Elise.challenge(Lee_Sin, "unarmed combat")
print("Trying to return a challenge when a challenge has already been sent")
Lee_Sin.challenge(Elise, "unarmed combat")

print('\n')
print("Issuing another challenge for the next part.")
Elise.challenge(Lee_Sin, "mace")

print('\n')
print("Declining a first challenge.")
print("Requests received and given to Lee:")
for x in Lee_Sin.requests_received:
    print(str(x))
print("Requests Sent from Elise:")
for x in Elise.requests_sent:
    print(str(x))
Lee_Sin.decline_first()
print("Requests received and given to Lee:")
for x in Lee_Sin.requests_received:
    print(str(x))
print("Requests Sent from Elise:")
for x in Elise.requests_sent:
    print(str(x))

print('\n')
print("Issuing another challenge for the next part.")
Elise.challenge(Lee_Sin, "broadsword")

print('\n')
print("Declining a random challenge.")
print("Requests received and given to Lee:")
for x in Lee_Sin.requests_received:
    print(str(x))
print("Requests Sent from Elise:")
for x in Elise.requests_sent:
    print(str(x))
Lee_Sin.decline_random()
print("Requests received and given to Lee:")
for x in Lee_Sin.requests_received:
    print(str(x))
print("Requests Sent from Elise:")
for x in Elise.requests_sent:
    print(str(x))

print('\n')
print("Emptying out the invitations.")
print("Requests received and given to Lee:")
for x in Lee_Sin.requests_received:
    print(str(x))
print("Requests Sent from Elise:")
for x in Elise.requests_sent:
    print(str(x))
Lee_Sin.decline_random()
print("Requests received and given to Lee:")
for x in Lee_Sin.requests_received:
    print(str(x))
print("Requests Sent from Elise:")
for x in Elise.requests_sent:
    print(str(x))

print('\n')
print("Configures test cases for the accept_random and accept_first methods in the Warrior class")
Lee_Sin.challenge(Mordekaiser, "mace")
Elise.challenge(Mordekaiser, "unarmed combat")
Elise.challenge(Mordekaiser, "mace")
Elise.challenge(Mordekaiser, "broadsword")
Elise.challenge(Mordekaiser, "spear")

print('\n')
print("Withdraws the fight between Lee Sin and Mordekaiser before resetting the challenge.")
withdraw = Fight(Lee_Sin, Mordekaiser, "mace")
Lee_Sin.withdraw(Mordekaiser, withdraw)
Lee_Sin.challenge(Mordekaiser, "mace")

print('\n')
print("6. Warrior vs. Warrior fight between Lee Sin and Modekaiser with a mace (Mordekaiser wins)")
print("Skill values: Lee Sin and Morde, respectively")
print(str(Lee_Sin.get_skill_value("mace")))
print(str(Mordekaiser.get_skill_value("mace")))
print("Wealth values: Lee Sin and Morde, respectively")
print(str(Lee_Sin.wealth))
print(str(Mordekaiser.wealth))
Mordekaiser.accept_first()
print("Skill values: Lee Sin and Morde, respectively")
print(str(Lee_Sin.get_skill_value("mace")))
print(str(Mordekaiser.get_skill_value("mace")))
print("Wealth values: Lee Sin and Morde, respectively")
print(str(Lee_Sin.wealth))
print(str(Mordekaiser.wealth))

print('\n')
print("Fighter vs. Warrior fight: Any weapon between Elise and Mordekaiser. I'm just going to have them fight it all.")
Mordekaiser.accept_random()
Mordekaiser.accept_random()
Mordekaiser.accept_random()
Mordekaiser.accept_random()

print('\n')
print("Knight Errant interactions")

print('\n')
print("7. Traveling check. If the Knight is traveling, they cannot accept a challenge. They also cannot challenge "
      "anyone.")
print("Also, the random travel attempt is tested here.")
Pantheon.challenge(Arthur, "broadsword")
Arthur.travel()
Arthur.accept_first()
Arthur.accept_random()
Arthur.challenge(Saitama, "broadsword")
Arthur.challenge(Mordekaiser, "broadsword")
Arthur.challenge(Anakin, "broadsword")
Arthur.return_from_travel()

print('\n')
print("8. Fighter vs. Knight Errant fight between Haise and Arima with unarmed combat (50/50)")
print("Skill values: Haise and Arima, respectively")
print(str(Haise.get_skill_value("unarmed combat")))
print(str(Arima.get_skill_value("unarmed combat")))
print("Wealth values: Haise and Arima, respectively")
print(str(Haise.wealth))
print(str(Arima.wealth))
Haise.challenge(Arima, "unarmed combat")
Arima.accept_first()
print("Skill values: Haise and Arima, respectively")
print(str(Haise.get_skill_value("unarmed combat")))
print(str(Arima.get_skill_value("unarmed combat")))
print("Wealth values: Haise and Arima, respectively")
print(str(Haise.wealth))
print(str(Arima.wealth))

print('\n')
print("9. Warrior vs. Knight Errant fight between Kaneki and Arima with unarmed combat (50/50)")
print("Skill values: Kaneki and Arima, respectively")
print(str(Kaneki.get_skill_value("unarmed combat")))
print(str(Arima.get_skill_value("unarmed combat")))
print("Wealth values: Kaneki and Arima, respectively")
print(str(Kaneki.wealth))
print(str(Arima.wealth))
Kaneki.challenge(Arima, "unarmed combat")
Arima.accept_first()
print("Skill values: Kaneki and Arima, respectively")
print(str(Kaneki.get_skill_value("unarmed combat")))
print(str(Arima.get_skill_value("unarmed combat")))
print("Wealth values: Kaneki and Arima, respectively")
print(str(Kaneki.wealth))
print(str(Arima.wealth))

print('\n')
print("10. Knight Errant vs. Knight Errant fight between Arthur and Anakin (50/50)")
print("Skill values: Arthur and Anakin, respectively")
print(str(Arthur.get_skill_value("broadsword")))
print(str(Anakin.get_skill_value("broadsword")))
print("Wealth values: Arima and Arthur, respectively")
print(str(Arthur.wealth))
print(str(Anakin.wealth))
Arthur.challenge(Anakin, "broadsword")
Anakin.accept_first()
print("Skill values: Arthur and Anakin, respectively")
print(str(Arthur.get_skill_value("broadsword")))
print(str(Anakin.get_skill_value("broadsword")))
print("Wealth values: Arima and Arthur, respectively")
print(str(Arthur.wealth))
print(str(Anakin.wealth))