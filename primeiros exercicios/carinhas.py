import emoji
print(emoji.emojize('\033[30;1mEae :chicken:\033[m', use_aliases=True))
# O use_aliases=True serve para validar o emoji
print(emoji.emojize('\033[34mHello\033[m,\033[34m:earth_americas:\033[m\n\033[31mtú éres um \033[m'
                    ':computer: \033[31mmeu :boy:', use_aliases=True))