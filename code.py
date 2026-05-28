import tkinter as tk
import json
import random

default_app_data = {
    "streaks": {
        "study": 0,
        "workout": 0,
        "motivation": 0,
        "progress": 0,
        "gym": 0,
        "diet": 0,
        "strech": 0,
        "sleep": 0,
        "academics": 0,
        "code": 0,
        "language": 0,
        "water": 0,
    },
    "goals": [],
    "journal": ""
}

def load_data():
    try:
        with open("streaks.json", "r") as file:
            return json.load(file)
    except:
        return default_app_data.copy()

def save_data():
    with open("streaks.json", "w") as file:
        json.dump(app_data, file, indent=4)

app_data = load_data()

if "streaks" not in app_data:
    app_data["streaks"] = default_app_data["streaks"]

if "goals" not in app_data:
    app_data["goals"] = []

if "journal" not in app_data:
    app_data["journal"] = ""

streaks = app_data["streaks"]
goals = app_data["goals"]

def reset_buttons():
    home_btn.config(bg=BUTTON_COLOR)
    gym_btn.config(bg=BUTTON_COLOR)
    study_btn.config(bg=BUTTON_COLOR)
    motivation_btn.config(bg=BUTTON_COLOR)

def show_home():
    home_page.tkraise()
    reset_buttons()
    home_btn.config(bg=ACTIVE_BUTTON)

def show_gym():
    gym_page.tkraise()
    reset_buttons()
    gym_btn.config(bg=ACTIVE_BUTTON)

def show_study():
    study_page.tkraise()
    reset_buttons()
    study_btn.config(bg=ACTIVE_BUTTON)

def show_quotes():
    motivational_page.tkraise()
    reset_buttons()
    motivation_btn.config(bg=ACTIVE_BUTTON)

root = tk.Tk()

root.title("My First App 😎")
root.geometry("500x700")
root.config(bg="white")

root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

BG_COLOR = "#1E1E1E"
TEXT_COLOR = "#D4D4D4"

BUTTON_COLOR = "#1E1E1E"
BUTTON_ACTIVE = "#3A3A3A"

ACTIVE_BUTTON = "#3A3A3A"

FONT_LARGE = ("Arial", 18)
FONT_MEDIUM = ("Arial", 12)
FONT_BUTTON = ("Arial", 10)

header_frame = tk.Frame(
    root,
    bg=BG_COLOR,
    height=80
)

header_frame.grid(
    row=0,
    column=0,
    sticky="ew"
)

header_label = tk.Label(
    header_frame,
    text="Streak Recorder",
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    font=("Arial", 22)
)

header_label.pack(pady=10)

main_frame = tk.Frame(root)

main_frame.grid(
    row=1,
    column=0,
    sticky="nsew"
)

main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(0, weight=1)

sidebar_frame = tk.Frame(
    main_frame,
    bg=BG_COLOR,
    width=140
)

sidebar_frame.grid(
    row=0,
    column=0,
    sticky="ns"
)

sidebar_frame.columnconfigure(0, weight=1)

sidebar_label = tk.Label(
    sidebar_frame,
    text="Navigate",
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    font=("Arial", 14)
)

sidebar_label.grid(
    row=0,
    column=0,
    pady=15,
    padx=10,
    sticky="ew"
)

content_frame = tk.Frame(
    main_frame,
    bg=BG_COLOR
)

content_frame.grid(
    row=0,
    column=1,
    sticky="nsew"
)

content_frame.rowconfigure(0, weight=1)
content_frame.columnconfigure(0, weight=1)

def create_page(text):

    page = tk.Frame(
        content_frame,
        bg=BG_COLOR
    )

    page.grid(
        row=0,
        column=0,
        sticky="nsew"
    )

    page.rowconfigure(0, weight=1)
    page.columnconfigure(0, weight=1)

    page_label = tk.Label(
        page,
        text=text,
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=FONT_MEDIUM
    )

    page_label.grid(
        row=0,
        column=0
    )

    return page

home_page = create_page("")

home_page.columnconfigure(0, weight=1)
home_page.columnconfigure(1, weight=1)

home_page.rowconfigure(0, weight=1)
home_page.rowconfigure(1, weight=1)

gym_page = create_page("")

gym_page.columnconfigure(0, weight=1)
gym_page.columnconfigure(1, weight=1)

gym_page.rowconfigure(0, weight=1)
gym_page.rowconfigure(1, weight=1)

study_page = create_page("")

study_page.columnconfigure(0, weight=1)
study_page.columnconfigure(1, weight=1)

study_page.rowconfigure(0, weight=1)
study_page.rowconfigure(1, weight=1)

motivational_page = create_page("")

motivational_page.columnconfigure(0, weight=1)
motivational_page.columnconfigure(1, weight=1)

motivational_page.rowconfigure(0, weight=1)
motivational_page.rowconfigure(1, weight=1)

def increase_streak(card_name, label):

    streaks[card_name] += 1

    label.config(
        text=f"Streak Count: {streaks[card_name]}"
    )

    save_data()

def create_card(page, text, row, column):

    card = tk.Frame(
        page,
        bg="#2A2A2A",
        bd=0,
        relief="flat"
    )

    card.grid(
        row=row,
        column=column,
        padx=8,
        pady=8,
        sticky="nsew"
    )

    card.columnconfigure(0, weight=1)

    card.rowconfigure(0, weight=1)
    card.rowconfigure(1, weight=1)
    card.rowconfigure(2, weight=1)

    title_label = tk.Label(
        card,
        text=text,
        bg="#2A2A2A",
        fg=TEXT_COLOR,
        font=FONT_BUTTON
    )

    title_label.grid(
        row=0,
        column=0,
        padx=8,
        pady=8,
        sticky="w"
    )

    info_label = tk.Label(
        card,
        text=f"Streak Count: {streaks[text.lower()]}",
        bg="#2A2A2A",
        fg=TEXT_COLOR,
        font=FONT_MEDIUM
    )

    info_label.grid(
        row=1,
        column=0,
        padx=8,
        pady=8,
        sticky="w"
    )

    confirm_btn = tk.Button(
        card,
        text=f"Start {text}",
        command=lambda: increase_streak(
            text.lower(),
            info_label
        ),
        bg=BUTTON_COLOR,
        fg=TEXT_COLOR,
        activebackground=BUTTON_ACTIVE,
        activeforeground="white",
        font=FONT_BUTTON,
        bd=0,
        relief="flat",
        highlightthickness=0,
        padx=5,
        pady=5
    )

    confirm_btn.grid(
        row=2,
        column=0,
        padx=8,
        pady=8,
        sticky="ew"
    )

    return card

create_card(home_page, "Workout", 0, 0)
create_card(home_page, "Study", 0, 1)
create_card(home_page, "Motivation", 1, 0)
create_card(home_page, "Progress", 1, 1)

create_card(gym_page, "Gym", 0, 0)
create_card(gym_page, "Strech", 0, 1)
create_card(gym_page, "Water", 1, 0)
create_card(gym_page, "Diet", 1, 1)

create_card(study_page, "Academics", 0, 0)
create_card(study_page, "Code", 1, 0)
create_card(study_page, "Language", 0, 1)
create_card(study_page, "Sleep", 1, 1)

quotes = [ "The only way to do great work is to love what you do. - Steve Jobs", "Life is what happens when you're busy making other plans. - John Lennon", "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt", "It is during our darkest moments that we must focus to see the light. - Aristotle", "Do not go where the path may lead, go instead where there is no path and leave a trail. - Ralph Waldo Emerson", "Be yourself; everyone else is already taken. - Oscar Wilde", "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln", "Many of life's failures are people who did not realize how close they were to success when they gave up. - Thomas Edison", "You never really learn much from hearing yourself speak. - George Clooney", "Life is a succession of lessons which must be lived to be understood. - Helen Keller", "You will face many defeats in life, but never let yourself be defeated. - Maya Angelou", "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela", "Spread love everywhere you go. Let no one ever come to you without leaving happier. - Mother Teresa", "When you reach the end of your rope, tie a knot in it and hang on. - Franklin D. Roosevelt", "Always remember that you are absolutely unique. Just like everyone else. - Margaret Mead", "Don't judge each day by the harvest you reap but by the seeds that you plant. - Robert Louis Stevenson", "Tell me and I forget. Teach me and I remember. Involve me and I learn. - Benjamin Franklin", "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart. - Helen Keller", "It is during our darkest moments that we must focus to see the light. - Aristotle", "Whoever is happy will make others happy too. - Anne Frank", "Do not go where the path may lead, go instead where there is no path and leave a trail. - Ralph Waldo Emerson", "You must be the change you wish to see in the world. - Mahatma Gandhi", "A journey of a thousand miles must begin with a single step. - Lao Tzu", "It is during our darkest moments that we must focus to see the light. - Aristotle", "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. - James Cameron", "Life is either a daring adventure or nothing at all. - Helen Keller", "Believe you can and you're halfway there. - Theodore Roosevelt", "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt", "The purpose of our lives is to be happy. - Dalai Lama", "Life is what happens when you're busy making other plans. - John Lennon", "Get busy living or get busy dying. - Stephen King", "You only live once, but if you do it right, once is enough. - Mae West", "Many of life's failures are people who did not realize how close they were to success when they gave up. - Thomas A. Edison", "If you want to live a happy life, tie it to a goal, not to people or things. - Albert Einstein", "Never let the fear of striking out keep you from playing the game. - Babe Ruth", "Money and success don't change people; they merely are what they are. - Bob Marley", "Your time is limited, so don't waste it living someone else's life. - Steve Jobs", "Not all of us can do great things. But we can do small things with great love. - Mother Teresa", "I have learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel. - Maya Angelou", "If you look at what you have in life, you'll always have more. - Oprah Winfrey", "If you look at what you don't have in life, you'll never have enough. - Oprah Winfrey", "If you want your children to be intelligent, read them fairy tales. - Albert Einstein", "If you want your children to be more intelligent, read them more fairy tales. - Albert Einstein", "Genius is one percent inspiration and ninety-nine percent perspiration. - Thomas Edison", "A friend is someone who knows all about you and still loves you. - Elbert Hubbard", "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson", "Darkness cannot drive out darkness: only light can do that. Hate cannot drive out hate: only love can do that. - Martin Luther King Jr.", "Do what you can, with what you have, where you are. - Theodore Roosevelt", "It is never too late to be what you might have been. - George Eliot", "Everything you've ever wanted is on the other side of fear. - George Addair", "To live is the rarest thing in the world. Most people exist, that is all. - Oscar Wilde", "I can't change the direction of the wind, but I can adjust my sails to always reach my destination. - Jimmy Dean", "Believe you can and you're halfway there. - Theodore Roosevelt", "Keep your face always toward the sunshine—and shadows will fall behind you. - Walt Whitman", "The time is always right to do what is right. - Martin Luther King Jr.", "The only true wisdom is in knowing you know nothing. - Socrates", "If you can't explain it simply, you don't understand it well enough. - Albert Einstein", "Blessed are those who can give without remembering and take without forgetting. - Elizabeth Bibesco", "With the new day comes new strength and new thoughts. - Eleanor Roosevelt", "I have not failed. I've just found 10,000 ways that won't work. - Thomas A. Edison", "No one can make you feel inferior without your consent. - Eleanor Roosevelt", "To handle yourself, use your head; to handle others, use your heart. - Eleanor Roosevelt", "It is better to fail in originality than to succeed in imitation. - Herman Melville", "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar", "Success is not final; failure is not fatal: It is the courage to continue that counts. - Winston S. Churchill", "You can't please everyone, and you can't make everyone like you. - Katie Couric", "I would rather die of passion than of boredom. - Vincent van Gogh", "There are no shortcuts to any place worth going. - Beverly Sills", "The only person you are destined to become is the person you decide to become. - Ralph Waldo Emerson", "We can't help everyone, but everyone can help someone. - Ronald Reagan", "Embrace the glorious mess that you are. - Elizabeth Gilbert", "You miss 100% of the shots you don't take. - Wayne Gretzky", "I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character. - Martin Luther King Jr.", "It is our choices, Harry, that show what we truly are, far more than our abilities. - J.K. Rowling", "If you judge people, you have no time to love them. - Mother Teresa", "The best way to predict the future is to invent it. - Alan Kay", "No act of kindness, no matter how small, is ever wasted. - Aesop", "I'm not a product of my circumstances. I am a product of my decisions. - Stephen Covey", "You have to learn the rules of the game. And then you have to play better than anyone else. - Albert Einstein", "We become what we think about. - Earl Nightingale", "The mind is everything. What you think you become. - Buddha", "The best revenge is massive success. - Frank Sinatra", "I am enough of an artist to draw freely upon my imagination. - Albert Einstein", "The two most important days in your life are the day you are born and the day you find out why. - Mark Twain", "I attribute my success to this: I never gave or took any excuse. - Florence Nightingale", "I've learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel. - Maya Angelou", "Life is 10% what happens to me and 90% of how I react to it. - Charles R. Swindoll", "I am thankful for all of those who said NO to me. It's because of them I'm doing it myself. - Albert Einstein", "The only way out is through. - Robert Frost", "The only thing we have to fear is fear itself. - Franklin D. Roosevelt", "Dream big and dare to fail. - Norman Vaughan", "The secret of success is to do the common thing uncommonly well. - John D. Rockefeller Jr.", "I can accept failure, everyone fails at something. But I can't accept not trying. - Michael Jordan", "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau", "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty. - Winston Churchill", "Don't let yesterday take up too much of today. - Will Rogers", "You learn more from failure than from success. Don't let it stop you. Failure builds character. - Unknown", "It’s not whether you get knocked down, it’s whether you get up. - Vince Lombardi", "If you are working on something that you really care about, you don't have to be pushed. The vision pulls you. - Steve Jobs", "People who are crazy enough to think they can change the world, usually do. - Steve Jobs", "Failure is simply the opportunity to begin again, this time more intelligently. - Henry Ford", "Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time. - Thomas Edison", "We are all in the gutter, but some of us are looking at the stars. - Oscar Wilde", "If you want to go fast, go alone. If you want to go far, go together. - African Proverb",]

def create_sections(page, title, row, column):

    section = tk.Frame(
        page,
        bg="#2A2A2A",
        bd=0,
        relief="flat"
    )

    section.grid(
        row=row,
        column=column,
        padx=8,
        pady=8,
        sticky="nsew"
    )

    section.columnconfigure(0, weight=1)
    section.rowconfigure(1, weight=1)

    title_label = tk.Label(
        section,
        text=title,
        bg="#2A2A2A",
        fg=TEXT_COLOR,
        font=FONT_MEDIUM
    )

    title_label.grid(
        row=0,
        column=0,
        padx=8,
        pady=8,
        sticky="w"
    )

    return section

quote_frame = create_sections(
    motivational_page,
    "Quotes",
    0,
    0
)

quote_frame.columnconfigure(0, weight=1)

quote_label = tk.Label(
    quote_frame,
    text=random.choice(quotes),
    bg="#2A2A2A",
    fg=TEXT_COLOR,
    font=("Arial", 10),
    wraplength=320,
    justify="center",
    padx=10,
    pady=10,
)

quote_label.grid(
    row=1,
    column=0,
    padx=5,
    pady=5,
    sticky="nsew"
)

def new_quote():
    quote = random.choice(quotes)
    quote_label.config(text=quote)

next_quote_btn = tk.Button(
    quote_frame,
    text="Next Quote",
    bg=BUTTON_COLOR,
    fg=TEXT_COLOR,
    activebackground=BUTTON_ACTIVE,
    activeforeground="white",
    font=FONT_BUTTON,
    bd=0,
    relief="flat",
    highlightthickness=0,
    padx=10,
    pady=8,
    command=new_quote
)

next_quote_btn.grid(
    row=2,
    column=0,
    padx=10,
    pady=10,
    sticky="ew"
)

goals_frame = create_sections(
    motivational_page,
    "Goals",
    0,
    1
)

goals_frame.columnconfigure(0, weight=1)

goals_listbox = tk.Listbox(
    goals_frame,
    bg="#2A2A2A",
    fg=TEXT_COLOR,
    font=("Arial", 10),
    selectbackground="#3A3A3A",
    selectforeground="white",
    bd=0,
    highlightthickness=0
)

goals_listbox.grid(
    row=1,
    column=0,
    padx=10,
    pady=10,
    sticky="nsew"
)

for goal in app_data["goals"]:
    goals_listbox.insert(tk.END, goal)

goal_entry = tk.Entry(
    goals_frame,
    bg="#2A2A2A",
    fg="white",
    font=("Arial", 12),
    insertbackground="white",
    bd=0,
    relief="flat",
    justify="center",
    width=25
)

goal_entry.grid(
    row=2,
    column=0,
    padx=10,
    pady=5,
    sticky="ew"
)

def add_goal():

    goal = goal_entry.get().strip()

    if goal == "":
        return

    app_data["goals"].append(goal)

    goals_listbox.insert(
        tk.END,
        goal
    )

    save_data()

    goal_entry.delete(0, tk.END)

def create_goal_btn(text, command, row, column):

    goal_btn = tk.Button(
        goals_frame,
        text=text,
        bg=BUTTON_COLOR,
        fg=TEXT_COLOR,
        activebackground=BUTTON_ACTIVE,
        activeforeground="white",
        font=FONT_BUTTON,
        bd=0,
        relief="flat",
        highlightthickness=0,
        padx=10,
        pady=8,
        command=command
    )

    goal_btn.grid(
        row=row,
        column=column,
        pady=10,
        padx=10,
        sticky="ew"
    )

    return goal_btn

add_goal_btn = create_goal_btn(
    "Add Goal",
    add_goal,
    3,
    0
)

journal_frame = create_sections(
    motivational_page,
    "Daily Journal",
    1,
    0
)

journal_frame.grid(
    row=1,
    column=0,
    columnspan=2,
    padx=8,
    pady=8,
    sticky="nsew"
)

journal_frame.columnconfigure(0, weight=1)
journal_frame.rowconfigure(1, weight=1)

journal_text = tk.Text(
    journal_frame,
    bg="#2A2A2A",
    fg=TEXT_COLOR,
    insertbackground="white",
    font=("Arial", 11),
    bd=0,
    relief="flat",
    wrap="word",
    padx=10,
    pady=10
)

journal_text.grid(
    row=1,
    column=0,
    padx=7,
    pady=7,
    sticky="nsew"
)

journal_text.insert(
    "1.0",
    app_data["journal"]
)

def save_journal():

    journal = journal_text.get(
        "1.0",
        tk.END
    ).strip()

    app_data["journal"] = journal

    save_data()

save_journal_btn = tk.Button(
    journal_frame,
    text="Save Journal",
    bg=BUTTON_COLOR,
    fg=TEXT_COLOR,
    activebackground=BUTTON_ACTIVE,
    activeforeground="white",
    font=FONT_BUTTON,
    bd=0,
    relief="flat",
    highlightthickness=0,
    padx=10,
    pady=8,
    command=save_journal
)

save_journal_btn.grid(
    row=2,
    column=0,
    padx=10,
    pady=10,
    sticky="ew"
)

def create_nav_button(text, command, row):

    button = tk.Button(
        sidebar_frame,
        text=text,
        bg=BUTTON_COLOR,
        fg=TEXT_COLOR,
        activebackground=BUTTON_ACTIVE,
        activeforeground="white",
        font=FONT_BUTTON,
        bd=0,
        relief="flat",
        highlightthickness=0,
        anchor="w",
        padx=12,
        pady=8,
        command=command
    )

    button.grid(
        row=row,
        column=0,
        padx=8,
        pady=10,
        sticky="ew"
    )

    def on_enter(event):
        event.widget.config(bg=BUTTON_ACTIVE)

    def on_leave(event):
        event.widget.config(bg=BUTTON_COLOR)

    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    return button

home_btn = create_nav_button(
    "Home",
    show_home,
    1
)

gym_btn = create_nav_button(
    "Gym",
    show_gym,
    2
)

study_btn = create_nav_button(
    "Study",
    show_study,
    3
)

motivation_btn = create_nav_button(
    "Motivation",
    show_quotes,
    4
)

footer_frame = tk.Frame(
    root,
    bg=BG_COLOR,
    height=50
)

footer_frame.grid(
    row=2,
    column=0,
    sticky="ew"
)

footer_label = tk.Label(
    footer_frame,
    text="Track Habits",
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    font=("Arial", 20)
)

footer_label.grid(
    row=0,
    column=0,
    pady=10
)

show_home()

root.mainloop()