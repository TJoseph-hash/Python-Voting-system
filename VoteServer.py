from socket import *

serverName = "127.0.0.1"
serverPort = 12004
serversocket = socket(AF_INET, SOCK_DGRAM)
serversocket.bind(("", serverPort))

## I decided to learn functions during this assignment because I wanted to improve my code organization and reusability.
def display_vote_counts(top_candidate, top_votes, vote_counts):
    # Print all candidates and their votes
    for candidate, count in vote_counts.items():
        print(f"{candidate}: {count} votes")

    print()  # Blank line for readability
    # Create a list of tied candidates (simple version)
    tied = []
    for candidate, count in vote_counts.items():
        if count == top_votes:
            tied.append(candidate)

    # Check if there's a tie
    if len(tied) > 1:
        print(f"Tie between {', '.join(tied)} with {top_votes} votes each!\n")
    else:
        print(f"Current Leader: {top_candidate} with {top_votes} votes\n")

        


def display_winner(top_candidate,top_votes):
        if top_votes > vote_counts[top_candidate ] -1 and top_votes > 5:
            print(f"{top_candidate} is the winner with {top_votes} votes!")

            
print("Tishawn Joseph voting server is ready.........")
# Dictionary to store vote counts
# Each index respresent a candidate
vote_counts = {"Anna": 0,"Barry": 0,"Carla": 0,"Devika": 0,"Ernest": 0}


while True:
    message, clientaddr = serversocket.recvfrom(2048)
    name = message.decode().strip()  # Decode message from bytes
    print("Received from client:", name)

    # Check if the name is a valid candidate
    if name in vote_counts:
        vote_counts[name] += 1
        modifiedMessage = f"Vote successful for candidate {name}"
    else:
        modifiedMessage = f"Invalid candidate: {name}"

    # Send response back to the client
    serversocket.sendto(bytes(modifiedMessage, "utf-8"), clientaddr)

    # Determine the current top candidate
    if any(vote_counts.values()):
        top_candidate = max(vote_counts, key=vote_counts.get)
        top_votes = vote_counts[top_candidate]
    else:
        top_candidate = "No votes yet"
        top_votes = 0

    
    display_vote_counts(top_candidate,top_votes,vote_counts)

    display_winner(top_candidate,top_votes)
        
