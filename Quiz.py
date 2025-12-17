print("=" * 50)
print("Welcome to the Valorant Quiz!")
print("=" * 50)
print("Test your knowledge with 50 questions!")
print("Easy (1-15) | Medium (16-35) | Hard (36-50)")
print("=" * 50)

playing = input("\nDo you want to play? (yes/no): ").lower()

if playing != "yes":
    print("Maybe next time! See you on the battlefield, Agent!")
    quit()

print("\n" + "=" * 50)
print("Let's begin! Good luck, Radiant!")
print("=" * 50)
score = 0

# EASY QUESTIONS (1-15)
print("\n--- EASY QUESTIONS ---\n")

# Q1
print("Q1: Which agent has the ability 'Tailwind'?")
answer = input("A. Jett\nB. Reyna\nC. Raze\nD. Phoenix\nYour answer: ").lower()
if answer == "a":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is A. Jett")
print(f"Score: {score}/1\n")

# Q2
print("Q2: What is the in-game currency used to buy weapons?")
answer = input("A. Gold\nB. Credits\nC. Coins\nD. Points\nYour answer: ").lower()
if answer == "b":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is B. Credits")
print(f"Score: {score}/2\n")

# Q3
print("Q3: Which map features the area called 'B Heaven'?")
answer = input("A. Bind\nB. Ascent\nC. Split\nD. Icebox\nYour answer: ").lower()
if answer == "b":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is B. Ascent")
print(f"Score: {score}/3\n")

# Q4
print("Q4: Sage's ultimate ability is called:")
answer = input("A. Resurrection\nB. Healing Orb\nC. Barrier Orb\nD. Slow Orb\nYour answer: ").lower()
if answer == "a":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is A. Resurrection")
print(f"Score: {score}/4\n")

# Q5
print("Q5: Which weapon is fully automatic and deals high damage at close range?")
answer = input("A. Sheriff\nB. Phantom\nC. Vandal\nD. Operator\nYour answer: ").lower()
if answer == "b":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is B. Phantom")
print(f"Score: {score}/5\n")

# Q6
print("Q6: Which agent uses a grenade called 'Boom Bot'?")
answer = input("A. Raze\nB. Killjoy\nC. Breach\nD. Skye\nYour answer: ").lower()
if answer == "a":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is A. Raze")
print(f"Score: {score}/6\n")

# Q7
print("Q7: How many rounds do you need to win a standard Valorant match?")
answer = input("A. 12\nB. 13\nC. 15\nD. 25\nYour answer: ").lower()
if answer == "b":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is B. 13")
print(f"Score: {score}/7\n")

# Q8
print("Q8: Which agent can heal teammates over time?")
answer = input("A. Breach\nB. Skye\nC. Phoenix\nD. Jett\nYour answer: ").lower()
if answer == "b":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is B. Skye")
print(f"Score: {score}/8\n")

# Q9
print("Q9: 'Spike' in Valorant is equivalent to what in Counter-Strike?")
answer = input("A. Bomb\nB. Health pack\nC. Armor\nD. Flag\nYour answer: ").lower()
if answer == "a":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is A. Bomb")
print(f"Score: {score}/9\n")

# Q10
print("Q10: Which map has a zipline connecting two sites?")
answer = input("A. Split\nB. Breeze\nC. Bind\nD. Fracture\nYour answer: ").lower()
if answer == "d":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is D. Fracture")
print(f"Score: {score}/10\n")

# Q11
print("Q11: What does Raze's ultimate 'Showstopper' do?")
answer = input("A. Deploys a turret\nB. Fires a rocket\nC. Revives teammates\nD. Creates a smoke\nYour answer: ").lower()
if answer == "b":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is B. Fires a rocket")
print(f"Score: {score}/11\n")

# Q12
print("Q12: Reyna can become invulnerable for a short time using:")
answer = input("A. Leer\nB. Dismiss\nC. Devour\nD. Empress\nYour answer: ").lower()
if answer == "b":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is B. Dismiss")
print(f"Score: {score}/12\n")

# Q13
print("Q13: Which agent can place traps that detect enemies?")
answer = input("A. Killjoy\nB. Sova\nC. Cypher\nD. Breach\nYour answer: ").lower()
if answer == "c":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is C. Cypher")
print(f"Score: {score}/13\n")

# Q14
print("Q14: How many agents are currently in Valorant (as of 2025)?")
answer = input("A. 18\nB. 21\nC. 23\nD. 25\nYour answer: ").lower()
if answer == "d":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is D. 25")
print(f"Score: {score}/14\n")

# Q15
print("Q15: Which weapon has the highest one-tap headshot potential?")
answer = input("A. Phantom\nB. Sheriff\nC. Vandal\nD. Operator\nYour answer: ").lower()
if answer == "d":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is D. Operator")
print(f"Score: {score}/15\n")

# MEDIUM QUESTIONS (16-35)
print("\n" + "=" * 50)
print("--- MEDIUM QUESTIONS ---")
print("=" * 50 + "\n")

# Q16
print("Q16: What does Sova's 'Recon Bolt' do?")
answer = input("A. Heals teammates\nB. Reveals enemy positions\nC. Creates a barrier\nD. Fires explosive projectiles\nYour answer: ").lower()
if answer == "b":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is B. Reveals enemy positions")
print(f"Score: {score}/16\n")

# Q17
print("Q17: Which agent can teleport a short distance using 'Gatecrash'?")
answer = input("A. Omen\nB. Jett\nC. Astra\nD. Phoenix\nYour answer: ").lower()
if answer == "a":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is A. Omen")
print(f"Score: {score}/17\n")

# Q18
print("Q18: What is the default economy reward for winning a round?")
answer = input("A. 1000 credits\nB. 1500 credits\nC. 2000 credits\nD. 3000 credits\nYour answer: ").lower()
if answer == "d":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is D. 3000 credits")
print(f"Score: {score}/18\n")

# Q19
print("Q19: Which map was removed from competitive rotation in 2023?")
answer = input("A. Icebox\nB. Bind\nC. Split\nD. Haven\nYour answer: ").lower()
if answer == "c":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is C. Split")
print(f"Score: {score}/19\n")

# Q20
print("Q20: What is the maximum number of players per team?")
answer = input("A. 4\nB. 5\nC. 6\nD. 7\nYour answer: ").lower()
if answer == "b":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is B. 5")
print(f"Score: {score}/20\n")

# Q21
print("Q21: Which agent's ability is called 'Rolling Thunder'?")
answer = input("A. Brimstone\nB. Breach\nC. Phoenix\nD. Killjoy\nYour answer: ").lower()
if answer == "b":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is B. Breach")
print(f"Score: {score}/21\n")

# Q22
print("Q22: Viper's 'Toxic Screen' creates:")
answer = input("A. A healing zone\nB. A long poison wall\nC. Smoke for vision block\nD. A flashbang\nYour answer: ").lower()
if answer == "b":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is B. A long poison wall")
print(f"Score: {score}/22\n")

# Q23
print("Q23: Which agent can revive a teammate with their ultimate?")
answer = input("A. Sage\nB. Skye\nC. Breach\nD. KAY/O\nYour answer: ").lower()
if answer == "a":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is A. Sage")
print(f"Score: {score}/23\n")

# Q24
print("Q24: What type of grenade is Raze's 'Paint Shells'?")
answer = input("A. Flash\nB. Molotov\nC. Fragmentation\nD. Smoke\nYour answer: ").lower()
if answer == "c":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is C. Fragmentation")
print(f"Score: {score}/24\n")

# Q25
print("Q25: Which agent is known for using 'Shrouded Step'?")
answer = input("A. Omen\nB. Cypher\nC. Yoru\nD. Neon\nYour answer: ").lower()
if answer == "a":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is A. Omen")
print(f"Score: {score}/25\n")

# Q26
print("Q26: How much damage does a headshot with the Operator usually deal?")
answer = input("A. 150\nB. 200\nC. 255\nD. 180\nYour answer: ").lower()
if answer == "c":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is C. 255")
print(f"Score: {score}/26\n")

# Q27
print("Q27: Which agent's ultimate can temporarily reveal all enemies on the map?")
answer = input("A. Sova\nB. KAY/O\nC. Skye\nD. Breach\nYour answer: ").lower()
if answer == "a":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is A. Sova")
print(f"Score: {score}/27\n")

# Q28
print("Q28: In ranked play, what is the lowest rank?")
answer = input("A. Bronze 1\nB. Iron 1\nC. Silver 1\nD. Radiant\nYour answer: ").lower()
if answer == "b":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is B. Iron 1")
print(f"Score: {score}/28\n")

# Q29
print("Q29: Which agent can shoot through walls with an ability?")
answer = input("A. Sova\nB. Breach\nC. Skye\nD. Raze\nYour answer: ").lower()
if answer == "b":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is B. Breach")
print(f"Score: {score}/29\n")

# Q30
print("Q30: KAY/O's ultimate is called:")
answer = input("A. Null/Cmd\nB. Overdrive\nC. Hunter's Fury\nD. Mode Switch\nYour answer: ").lower()
if answer == "a":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is A. Null/Cmd")
print(f"Score: {score}/30\n")

# Q31
print("Q31: On Bind, which site has a teleport pad connecting it to the other?")
answer = input("A. A\nB. B\nC. Both\nD. None\nYour answer: ").lower()
if answer == "c":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is C. Both")
print(f"Score: {score}/31\n")

# Q32
print("Q32: Neon's abilities focus on:")
answer = input("A. Traps and slowing enemies\nB. Speed and electricity\nC. Healing and barriers\nD. Vision denial\nYour answer: ").lower()
if answer == "b":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is B. Speed and electricity")
print(f"Score: {score}/32\n")

# Q33
print("Q33: What does Cypher's 'Spycam' do?")
answer = input("A. Heals allies\nB. Provides vision\nC. Explodes for damage\nD. Blocks movement\nYour answer: ").lower()
if answer == "b":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is B. Provides vision")
print(f"Score: {score}/33\n")

# Q34
print("Q34: Which weapon is most effective for spraying at close range?")
answer = input("A. Operator\nB. Sheriff\nC. Spectre\nD. Marshal\nYour answer: ").lower()
if answer == "c":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is C. Spectre")
print(f"Score: {score}/34\n")

# Q35
print("Q35: Which agent uses the ability 'Guiding Light'?")
answer = input("A. Phoenix\nB. Skye\nC. Sage\nD. Jett\nYour answer: ").lower()
if answer == "b":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is B. Skye")
print(f"Score: {score}/35\n")

# HARD QUESTIONS (36-50)
print("\n" + "=" * 50)
print("--- HARD QUESTIONS ---")
print("=" * 50 + "\n")

# Q36
print("Q36: Brimstone's ultimate 'Orbital Strike' does what type of damage?")
answer = input("A. Instant lethal\nB. Damage over time\nC. Teleports enemies\nD. Blind effect\nYour answer: ").lower()
if answer == "b":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is B. Damage over time")
print(f"Score: {score}/36\n")

# Q37
print("Q37: What is the cost of a Vandal rifle?")
answer = input("A. 2900 credits\nB. 3000 credits\nC. 3100 credits\nD. 3200 credits\nYour answer: ").lower()
if answer == "a":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is A. 2900 credits")
print(f"Score: {score}/37\n")

# Q38
print("Q38: Which agent has the ability to teleport across the map using 'Dimensional Drift'?")
answer = input("A. Omen\nB. Yoru\nC. Astra\nD. KAY/O\nYour answer: ").lower()
if answer == "b":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is B. Yoru")
print(f"Score: {score}/38\n")

# Q39
print("Q39: What is the fastest movement speed in Valorant (excluding abilities)?")
answer = input("A. 3.5 m/s\nB. 4.1 m/s\nC. 4.7 m/s\nD. 5.0 m/s\nYour answer: ").lower()
if answer == "d":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is D. 5.0 m/s")
print(f"Score: {score}/39\n")

# Q40
print("Q40: Which agent's ultimate can disable enemy abilities in a radius?")
answer = input("A. KAY/O\nB. Breach\nC. Omen\nD. Sage\nYour answer: ").lower()
if answer == "a":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is A. KAY/O")
print(f"Score: {score}/40\n")

# Q41
print("Q41: What is the damage of Raze's Showstopper rocket?")
answer = input("A. 150\nB. 200\nC. 180\nD. 160\nYour answer: ").lower()
if answer == "a":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is A. 150")
print(f"Score: {score}/41\n")

# Q42
print("Q42: Which agent is from Brazil?")
answer = input("A. Raze\nB. Jett\nC. Phoenix\nD. Neon\nYour answer: ").lower()
if answer == "a":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is A. Raze")
print(f"Score: {score}/42\n")

# Q43
print("Q43: On which map is the site called 'Mid Courtyard'?")
answer = input("A. Split\nB. Ascent\nC. Breeze\nD. Icebox\nYour answer: ").lower()
if answer == "b":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is B. Ascent")
print(f"Score: {score}/43\n")

# Q44
print("Q44: What happens if the spike is defused with 0.1 seconds left?")
answer = input("A. It explodes\nB. Defuse counts as success\nC. Round goes into overtime\nD. Spike resets\nYour answer: ").lower()
if answer == "b":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is B. Defuse counts as success")
print(f"Score: {score}/44\n")

# Q45
print("Q45: Which agent can blind multiple enemies using 'Flashpoint'?")
answer = input("A. Phoenix\nB. Breach\nC. Reyna\nD. Skye\nYour answer: ").lower()
if answer == "b":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is B. Breach")
print(f"Score: {score}/45\n")

# Q46
print("Q46: Which agent's ability is 'Neural Theft'?")
answer = input("A. KAY/O\nB. Cypher\nC. Omen\nD. Killjoy\nYour answer: ").lower()
if answer == "b":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is B. Cypher")
print(f"Score: {score}/46\n")

# Q47
print("Q47: How many grenades can Killjoy deploy simultaneously?")
answer = input("A. 2\nB. 3\nC. 4\nD. 5\nYour answer: ").lower()
if answer == "a":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is A. 2")
print(f"Score: {score}/47\n")

# Q48
print("Q48: Which map has a 'B Green' area?")
answer = input("A. Icebox\nB. Split\nC. Breeze\nD. Bind\nYour answer: ").lower()
if answer == "a":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is A. Icebox")
print(f"Score: {score}/48\n")

# Q49
print("Q49: Which agent can dash multiple times using their ultimate?")
answer = input("A. Jett\nB. Neon\nC. Reyna\nD. Raze\nYour answer: ").lower()
if answer == "a":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is A. Jett")
print(f"Score: {score}/49\n")

# Q50
print("Q50: What is the cooldown of Sage's Resurrection ultimate?")
answer = input("A. 120 seconds\nB. 160 seconds\nC. 180 seconds\nD. 200 seconds\nYour answer: ").lower()
if answer == "d":
    print("✓ Correct!")
    score += 1
else:
    print("✗ Incorrect! The answer is D. 200 seconds")
print(f"Score: {score}/50\n")

# FINAL RESULTS
print("\n" + "=" * 50)
print("QUIZ COMPLETE!")
print("=" * 50)
print(f"Your final score: {score}/50")
percentage = (score / 50) * 100
print(f"Percentage: {percentage:.1f}%")
print()

if percentage >= 90:
    print("🏆 RADIANT! You're a Valorant expert!")
elif percentage >= 75:
    print("💎 IMMORTAL! Impressive knowledge!")
elif percentage >= 60:
    print("💜 DIAMOND! Great job!")
elif percentage >= 45:
    print("💙 PLATINUM! Good effort!")
elif percentage >= 30:
    print("🩵 GOLD! Keep learning!")
else:
    print("🤎 Keep practicing! You'll get better!")

print("\nThanks for playing! GG!")
print("=" * 50)