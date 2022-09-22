

sentence  = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")
words = {word: len(word) for word in sentence.split()}
print(words)

print("-" * 40)
squares = {x: x ** 2 for x in range(1, 11)}
print(squares)

players = {
    'sachin': [300, 345, 225, 205, 285],
    'sourav': [200, 305, 330, 405, 150],
    'rahul': [145, 230, 298, 360, 215],
    'sehwag': [120, 150, 405, 380, 450],
    'yuvraj': [185, 205, 230, 120, 160],
    'laxman': [105, 185, 250, 385, 180]
}
print("-" * 40)
print(f"players :{players}")

print("-" * 40)
scores = {"Sachin" :players['sachin']}
print(scores)

print("-" * 40)
scores = {k: v for k, v in players.items()}
print(scores)

print("-" * 40)
scores = {"Sachin" :sum(players['sachin'])}
print(scores)

print("-" * 40)
scores = {k: sum(v) for k, v in players.items()}
print(scores)

print("-" * 40)
scores = {k: (lambda score: sum(score) / len(score))(v) for k, v in players.items()}
print(scores)

print("-" * 40)
scores = [score for score in players.values()]
print(scores)

print("-" * 40)
scores = [scr for score in players.values() for scr in score if scr >= 200]
print(scores)

print("-" * 40)
slctPlayers = {name: [score for score in scores if score >= 200] for name, scores in players.items()}
print(slctPlayers)