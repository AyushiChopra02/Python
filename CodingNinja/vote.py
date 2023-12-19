def voting_system():
    votes={'A':0 , 'B':0 , 'C':0}
    while True:
        print("veve")
        vote = input().upper()
        if vote == 'Q' :
            break
        elif vote in votes:
            votes[vote] += 1
        else:
            print("Invalid vote. ")
    total_votes = sum(votes.values())

    print("\nVoting Results:")
    for candidate, vote_count in votes.items():
        percentage = (vote_count / total_votes) * 100 if total_votes > 0 else 0
        print(f"{candidate}: {vote_count} votes ({percentage:.2f}%)")

    print(f"Total Votes: {total_votes}")

 

