num_matches = int(input())

alice_score = 0
bob_score = 0

for i in range(num_matches):
    round_games = input().split()
    alice_round_score = 0
    bob_round_score = 0

    for game in round_games:
        if game in ["RP", "PS", "SR"]: bob_round_score += 1
        elif game in ["RS", "PR", "SP"]: alice_round_score += 1
    
    if alice_round_score > bob_round_score:
        alice_score += 1
    elif bob_round_score > alice_round_score:
        bob_score += 1

if alice_score >= bob_score:
    print("Alice {}".format(alice_score))
else:
    print("Bob {}".format(bob_score))


    

# print here whoever is the overall winner of all the matches and
# how many matches the winner won
