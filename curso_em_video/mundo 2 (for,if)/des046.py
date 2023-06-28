from time import sleep
import emoji
for c in range(10, 0, -1):
    sleep(1)
    print(c)
print(emoji.emojize('\033[31;1m:tada::tada:\033[33;1m:confetti_ball:', use_aliases=True))
