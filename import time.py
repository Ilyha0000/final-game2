import tkinter as tk
from tkinter import messagebox
import random
from PIL import image

class TextAdventureGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Текстова пригода")
        self.master.geometry("600x400")
        self.master.configure(bg="#2C3E50")

        self.story_text = tk.Label(master, text="Ви знаходитеся в темному лісі. Що ви будете робити?", font=("Helvetica", 14), bg="#2C3E50", fg="white")
        self.story_text.pack(pady=10)

        self.status_frame = tk.Frame(master, bg="#2C3E50")
        self.status_frame.pack()

        self.health_label = tk.Label(self.status_frame, text="Здоров'я: 100", font=("Helvetica", 12), bg="#2C3E50", fg="white")
        self.health_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.hunger_label = tk.Label(self.status_frame, text="Голод: 50", font=("Helvetica", 12), bg="#2C3E50", fg="white")
        self.hunger_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.thirst_label = tk.Label(self.status_frame, text="Спрага: 50", font=("Helvetica", 12), bg="#2C3E50", fg="white")
        self.thirst_label.grid(row=0, column=2, padx=10, pady=5, sticky="w")

        self.fatigue_label = tk.Label(self.status_frame, text="Втома: 50", font=("Helvetica", 12), bg="#2C3E50", fg="white")
        self.fatigue_label.grid(row=0, column=3, padx=10, pady=5, sticky="w")

        self.money_label = tk.Label(self.status_frame, text="Гроші: 100", font=("Helvetica", 12), bg="#2C3E50", fg="white")
        self.money_label.grid(row=0, column=4, padx=10, pady=5, sticky="w")

        self.choice_frame = tk.Frame(master, bg="#2C3E50")
        self.choice_frame.pack()

        self.choice_buttons = []
        choices = ["Піти ліворуч", "Піти праворуч", "Піти прямо", "Провести обряд", "Дослідити місцевість", "Подивитися на зірки", "Зібрати ресурси", "Піти на полювання", "Відвідати торговця", "Випити зелье"]
        button_images = [tk.PhotoImage(file=f"button_{i+1}.png") for i in range(len(choices))]
        for i, choice in enumerate(choices):
            button = tk.Button(self.choice_frame, text=choice, font=("Helvetica", 12), image=button_images[i], compound="left", bg="#34495E", fg="white", command=lambda i=i: self.choice_selected(i))
            button.image = button_images[i]
            button.grid(row=i // 2, column=i % 2, padx=5, pady=5, sticky="ew")
            self.choice_buttons.append(button)

        self.quit_button = tk.Button(master, text="Вийти з гри", font=("Helvetica", 12), bg="#E74C3C", fg="white", command=master.quit)
        self.quit_button.pack(pady=10)

        self.player_state = {
            "health": 100,
            "hunger": 50,
            "thirst": 50,
            "fatigue": 50,
            "money": 100
        }

    def choice_selected(self, choice_index):
        result = ""
        if choice_index == 0:
            result = self.go_left()
        elif choice_index == 1:
            result = self.go_right()
        elif choice_index == 2:
            result = self.go_straight()
        elif choice_index == 3:
            result = self.perform_ritual()
        elif choice_index == 4:
            result = self.explore_area()
        elif choice_index == 5:
            result = self.observe_stars()
        elif choice_index == 6:
            result = self.gather_resources()
        elif choice_index == 7:
            result = self.go_hunting()
        elif choice_index == 8:
            result = self.visit_trader()
        elif choice_index == 9:
            result = self.drink_potion()

        messagebox.showinfo("Результат", result)
        self.update_interface()

    def go_left(self):
        result = random.choice([
            "Ви знайшли скарби в сундуку!",
            "Ви впали в яму і зламали ногу.",
            "На вас напала стая вовків.",
            "Ви зустріли древнього мудреця, який дав вам загадку.",
            "Ви знайшли притулок від дощу й відпочили.",
            "Ви натрапили на стародавнє святине."
        ])
        return result

    def go_right(self):
        result = random.choice([
            "Ви знайшли вихід з лісу!",
            "Ви загубилися й не можете знайти дорогу назад.",
            "Ви знайшли залишений будинок.",
            "На вас напала дика звіряча тварина, але вам вдалося втекти.",
            "Ви помітили дивну фігуру вдалині.",
            "Ви знайшли джерело води й напилися."
        ])
        return result

    def go_straight(self):
        result = random.choice([
            "Ви натрапили на дику річку і не можете її перейти.",
            "Ви знайшли старовинний храм.",
            "Ви побачили світло здалеку.",
            "Ви помітили дивні світяться гриби.",
            "Ви натрапили на сліди диких тварин.",
            "Ви почули дивні звуки з лісу."
        ])
        return result

    def perform_ritual(self):
        result = random.choice([
            "Ваш обряд успішний. Ви почуваєте себе сильнішим.",
            "Вам не вдалося виконати обряд. Нічого не сталося.",
            "Ви виявили, що обряд був пасткою!",
            "Вам вдалося встановити зв'язок з духами лісу."
        ])
        return result

    def explore_area(self):
        result = random.choice([
            "Ви знайшли секретні стежки в лісі.",
            "Ви виявили стародавні письмена на деревах.",
            "Вам вдалося уникнути небезпечних монстрів.",
            "Ви натрапили на підземну печеру.",
            "Ви загубилися в лабіринті."
        ])
        return result

    def observe_stars(self):
        result = random.choice([
            "Зірки передбачають вам удачу.",
            "Ви відчуваєте натхнення, дивлячись на зірки.",
            "Ви бачите дивні світяться об'єкти на небі.",
            "Ви відчуваєте, що зірки спостерігають за вами."
        ])
        return result

    def gather_resources(self):
        result = random.choice([
            "Ви знайшли ягоди і з'їли їх, заспокоївши голод.",
            "Вам вдалося зібрати дрова для вогнища.",
            "Ви знайшли гриби, але не знаєте, чи є вони їстівні.",
            "Ви виявили рідкісну квітку.",
            "Ви натрапили на корисну рослину, яка може допомогти в лікуванні."
        ])
        return result

    def go_hunting(self):
        result = random.choice([
            "Ви вбили кролика й приготували його на вечерю.",
            "На вас напав ведмідь, але вам вдалося втекти.",
            "Ви знайшли стадо оленів, але вони були занадто швидкими для вас.",
            "Вам вдалося впіймати рибу в річці.",
            "Ви не змогли знайти жодної тварини для полювання."
        ])
        return result

    def visit_trader(self):
        result = random.choice([
            "Торговець запропонував вам вигідну угоду.",
            "Ви купили карту лісу у торговця.",
            "Торговець виявився шахраєм і обманув вас.",
            "Ви продали непотрібні предмети й заробили трохи грошей.",
            "Ви купили нову зброю у торговця."
        ])
        return result

    def drink_potion(self):
        result = random.choice([
            "Зелье відновило ваше здоров'я.",
            "Ви почували себе сильніше після випитого зелья.",
            "Зелье виявилося отруйним! Ваше здоров'я знизилося.",
            "Ви стали невидимим на короткий час після випитого зелья.",
            "Зелье викликало дивні галюцинації."
        ])
        return result

    def update_interface(self):
        self.health_label.config(text=f"Здоров'я: {self.player_state['health']}")
        self.hunger_label.config(text=f"Голод: {self.player_state['hunger']}")
        self.thirst_label.config(text=f"Спрага: {self.player_state['thirst']}")
        self.fatigue_label.config(text=f"Втома: {self.player_state['fatigue']}")
        self.money_label.config(text=f"Гроші: {self.player_state['money']}")

root = tk.Tk()
game = TextAdventureGame(root)
root.mainloop()
