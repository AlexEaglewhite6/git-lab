print("v1.6")
print("Это ветка - master")
name = input("Назовите своего ассистента: ")
print(f"Привет, меня зовут {name}. Я твой личный ассистент.\n")
username = input("Давай познакомимся! Как тебя зовут?\nТвое имя: ")
print(f"\nОтлично, {username}! Чем могу помочь?")
user_answer = input()

print(f"\nПрости, я еще недоработанный ассистент. Я не могу понять твое сообщение\n\n{user_answer}")
print("Давай я просто начну собирать информацию о тебе?)))\n")
user_favorite_game = input("Какая у тебя любмая игра? Если ее нет, просто напиши НЕТ\nТвоя любимая игра: ")

if user_favorite_game.lower().strip() == "нет":
    print("\nЖаль, что у тебя нет любимой игры :(")
    user_favorite_game = ""
else:
    print(f"\nКруто! Мне тоже нравится {user_favorite_game}!")