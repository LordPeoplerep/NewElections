
# Election logic based on Authentic Votes (AV), not percentage

candidates = {
    "Alice": 320,
    "Bob": 450,
    "Charlie": 450
}

# Determine winner(s) by highest AV
max_av = max(candidates.values())
winners = [name for name, av in candidates.items() if av == max_av]

print("Election Results:")
for name, av in candidates.items():
    total = sum(candidates.values())
    percent = (av / total) * 100
    print(f"{name}: {av} AV ({percent:.2f}%)")

if len(winners) == 1:
    print(f"Winner: {winners[0]}")
else:
    print(f"Tie between: {', '.join(winners)}")
