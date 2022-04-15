# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Bradley = Character("Bradley")
define Gold = Character("Gold")
define Owen = Character("Owen")
define Irving = Character("Irving")
define Taylor = Character("Taylor")


# The game starts here.
# NOTE: CAN ADD WEIGHTS TO PLAYER CHOICES TO DETERMINE IF FINAL ENDING IS GOOD, BAD, OR NETURAL
# NOTE: RANDOMIZE MCQ OPTIONS BC THEY ARE CURRENTLY ORDERED BAD, GOOD, OK

label start: # TESTER
    "BFF" "Who would you like to date?"
    scene bg black
    menu:
        "Brad":
            jump brad
        "Gold":
            jump gold
        "Owen":
            jump owen
        "Irving":
            jump irving
        "Taylor":
            jump taylor

    # scene bg restaurant
    # with fade
    # Bradley "Hey, uh, you look interesting…" # "can you change into something else? Please?"
    # Gold "blub..."
    # # show gold happy GOLD TOO LARGER
    # Owen "Now that's outfit's a hit!"

label characters:
    # BRADLEY CHARACTER ARC
    label brad:
        scene bg restaurant
        # Bradley Outfit Eval
        # If outfit == Bad:
        show bradley sad
        Bradley "Hey, uh, you look interesting…" # "can you change into something else? Please?"
        # else if outfit == Good:
        show bradley happy
        Bradley "Hello! You certainly look lovely tonight…" # "Oh my god, you look absolutely gorgeous!"

        # Bradley Food
        label brad_food:
            show bradley neutral
            Bradley "What do you want to order?"
            menu:
                "Cheeseburger":
                    jump brad_food_bad
                "Lobster":
                    jump brad_food_good
                "Chicken Alfredo":
                    jump brad_food_ok

            # Post choice response
            label brad_food_bad: # Cheeseburger
                show bradley sad
                Bradley "Really, a cheeseburger in a fancy restaurant?" # "Might as well go to McDonald's"
                jump brad_work
            label brad_food_good: # Lobster
                show bradley happy
                Bradley "Wow, someone with good taste!" # "This place is famous fro its lobster."
                jump brad_work
            label brad_food_ok: # Chicken Alfredo
                show bradley neutral
                Bradley "Interesting choice!"
                jump brad_work

        # Bradley work
        label brad_work:
            show bradley neutral
            Bradley "So what do you do for work?"
            menu:
                "I'm in between jobs right now":
                    jump brad_job_bad
                "I'm a freelancer":
                    jump brad_job_good
                "Taking a break for now":
                    jump brad_job_ok

            # Post choice response
            label brad_job_bad: # I'm in between jobs right now
                show bradley sad
                Bradley "So... you're unemployed is what I'm hearing."
                jump brad_dessert
            label brad_job_good: # I'm a freelancer
                show bradley happy
                Bradley "Nice, I respect being your own boss!"
                jump brad_dessert
            label brad_job_ok: # Taking a break for now
                show bradley neutral
                Bradley "I see... Nothing wrong with a work break now and then."
                jump brad_dessert

        # Bradley dessert
        label brad_dessert:
            show bradley neutral
            Bradley "So what do you want to get for dessert?"
            menu:
                "No dessert":
                    jump brad_dessert_bad
                "Macarons":
                    jump brad_dessert_good
                "Ice cream":
                    jump brad_dessert_ok
            # Post choice resposne
            label brad_dessert_bad: # No dessert
                show bradley sad
                Bradley "Sigh... Suit yourself."
                jump start
            label brad_dessert_good: # Macarons
                show bradley happy
                Bradley "Ah, someone with a taste for French cuisine!"
                jump start
            label brad_dessert_ok: # Ice cream
                show bradley neutral
                Bradley "I guess you can never go wrong with ice cream!"
                jump start



    # GOLD CHARACTER ARC
    label gold:
        scene bg underwater
        # Gold Outfit Eval
        # If outfit == Bad:
        show gold sad
        Gold "blub..."
        # else if outfit == Good:
        show gold happy
        Gold "BLUB BLUB!!"

        # Gold Food
        label gold_food:
            show gold neutral
            Gold "Blub blub blub?"
            menu:
                "Fish sticks":
                    jump gold_food_bad
                "Steak":
                    jump gold_food_good
                "Pasta":
                    jump gold_food_ok
            # Post choice response
            label gold_food_bad: # Fish sticks
                show gold sad
                Gold "blub..."
                jump gold_query
            label gold_food_good: # Steak
                show gold happy
                Gold "BLUB BLUB!!"
                jump gold_query
            label gold_food_ok: # Pasta
                show gold neutral
                Gold "blub blub blub"
                jump gold_query

        # Gold question response
        label gold_query:
            show gold neutral
            Gold "blub blub blub. blub blub blub!"
            menu:
                "Um, blub blub?":
                    jump gold_query_bad
                "Oh my god, you're so funny!":
                    jump gold_query_good
                "Sorry, I can't really speak fish":
                    jump gold_query_ok
            # Post choice response
            label gold_query_bad: # respond in fish
                show gold sad
                Gold "blub..."
                jump gold_dessert
            label gold_query_good: # Oh my god, you're so funny!
                show gold happy
                Gold "BLUB BLUB!!"
                jump gold_dessert
            label gold_query_ok: # Sorry I can't really speak fish
                show gold neutral
                Gold "blub blub blub"
                jump gold_dessert

        # Gold dessert
        label gold_dessert:
            show gold neutral
            Gold "Blub?"
            menu:
                "Taiyaki":
                    jump gold_dessert_bad
                "Tiramisu":
                    jump gold_dessert_good
                "Jello":
                    jump gold_dessert_ok
            # Post choice response
            label gold_dessert_bad: # Taiyaki
                show gold sad
                Gold "Blub..."
                jump start
            label gold_dessert_good: # Tiramisu
                show gold happy
                Gold "BLUB BLUB!!"
                jump start
            label gold_dessert_ok: # Jello
                show gold neutral
                Gold "blub blub blub"
                jump start



    # OWEN CHARACTER ARC
    label owen:
        scene bg shakeys
        # Owen Outfit Eval
        # If outfit == Bad:
        show owen sad
        Owen "Hm, not sure how game I am for your outfit..."
        # else if outfit == Good:
        show owen happy
        Owen "Now that's outfit's a hit!"

        # Owen Food
        label owen_food:
            show owen neutral
            Owen "What d'ya wanna eat?"
            menu:
                "Pizza":
                    jump owen_food_bad
                "Salad and Vegetable Smoothie":
                    jump owen_food_good
                "Burger, Fries, and a Milkshake":
                    jump owen_food_ok
            # Post choice response
            label owen_food_bad: # Pizza
                show owen sad
                Owen "Pizza? I can't imagine having the calories to spare to eat something like that..."
                jump owen_sports
            label owen_food_good: # Salad and Vegetable Smoothie
                show owen happy
                Owen "Eating healthy? Good choice!"
                jump owen_sports
            label owen_food_ok: # Burger, Fries, and a Milkshake
                show owen neutral
                Owen "Well, nothing wrong with a cheat day from time to time."
                jump owen_sports

        # Owen Sports
        label owen_sports:
            show owen neutral
            Owen "What's your favorite sport?"
            menu:
                "I'm not really into sports...":
                    jump owen_sports_bad
                "Football":
                    jump owen_sports_good
                "Quidditch":
                    jump owen_sports_ok
            # Post choice response
            label owen_sports_bad: # I'm not really into sports...
                show owen sad
                Owen "Uh, well that's ok I guess?"
                jump owen_dessert
            label owen_sports_good: # Football
                show owen happy
                Owen "Now that's my kind of sport!"
                jump owen_dessert
            label owen_sports_ok: # Quidditch
                show owen neutral
                Owen "Oh that sport from the Lord of the RIngs? That's cool!"
                jump owen_dessert

        # Owen dessert
        label owen_dessert:
            show owen neutral
            Owen "You up for dessert?"
            menu:
                "Cheesecake":
                    jump owen_dessert_bad
                "I think I'll pass on dessert.":
                    jump owen_dessert_good
                "Fruit salad":
                    jump owen_dessert_ok
            # Post choice resposne
            label owen_dessert_bad: # Cheesecake
                show owen sad
                Owen "Yikes..."
                jump start
            label owen_dessert_good: # I think I'll pass on dessert.
                show owen happy
                Owen "Now that's thinkin' healthy!"
                jump start
            label owen_dessert_ok: # Fruit salad
                show owen neutral
                Owen "Those are kinda sugary, but at least it's all-natural!"
                jump start



    # IRVING CHARACTER ARC
    label irving:
        scene bg french
        # irving Outfit Eval
        # If outfit == Bad:
        show irving sad
        Irving "Were you in a bit of a rush getting here?"
        # else if outfit == Good:
        show irving happy
        Irving "My, don’t you look dashing! Truly elegant…"

        # irving Food
        label irving_food:
            show irving neutral
            Irving "What are we craving tonight, darling?"
            menu:
                "Pasta salad":
                    jump irving_food_bad
                "Shrimp Ceviche":
                    jump irving_food_good
                "Ravioli":
                    jump irving_food_ok
            # Post choice response
            label irving_food_bad: # Pasta salad
                show irving sad
                Irving "Experience comes from bad decisions…"
                jump irving_study
            label irving_food_good: # Shrimp Ceviche
                show irving happy
                Irving "Let food be thy medicine and medicine be thy food!"
                jump irving_study
            label irving_food_ok: # Ravioli
                show irving neutral
                Irving "One cannot think well if one has not dined well."
                jump irving_study

        # irving Sports
        label irving_study:
            show irving neutral
            Irving "So, what academic horizons are you pursuing?"
            menu:
                "I don't really think school is a right fit for me...":
                    jump irving_study_bad
                "Architecture":
                    jump irving_study_good
                "Computer Science":
                    jump irving_study_ok
            # Post choice response
            label irving_study_bad: # I don't really think school is a right fit for me...
                show irving sad
                Irving "Pity the fool who thinks themselves above education..."
                jump irving_dessert
            label irving_study_good: # Architecture
                show irving happy
                Irving "Ah, Architecture! What an intersection of art and engineering!"
                jump irving_dessert
            label irving_study_ok: # Comp Sci
                show irving neutral
                Irving "Well, technology is what drives our world!"
                jump irving_dessert

        # irving dessert
        label irving_dessert:
            show irving neutral
            Irving "Saved some room for dessert, I hope?"
            menu:
                "Brownie Sunday":
                    jump irving_dessert_bad
                "Creme Brulee":
                    jump irving_dessert_good
                "Nope, no dessert for me!":
                    jump irving_dessert_ok
            # Post choice response
            label irving_dessert_bad: # Brownie Sunday
                show irving sad
                Irving "Immaturity is the incapacity to use one’s intelligence without the guidance of another."
                jump start
            label irving_dessert_good: # I think I'll pass on dessert.
                show irving happy
                Irving "Decisions are the frequent fabric of our daily design."
                jump start
            label irving_dessert_ok: # I think I'll pass on dessert.
                show irving neutral
                Irving "The content of your character is your choice"
                jump start



    # TAYLOR CHARACTER ARC
    label taylor:
        scene bg midtier
        # taylor Outfit Eval
        # If outfit == Bad:
        show taylor sad
        Taylor "Oh, uh hey! Almost didn’t recognize you there…"
        # else if outfit == Good:
        show taylor happy
        Taylor "Wow, it’s been so long but you look so good!"

        # taylor Food
        label taylor_food:
            show taylor neutral
            Taylor "All right, what's on the menu tonight?"
            menu:
                "Onion Rings":
                    jump taylor_food_bad
                "Veggie Burger":
                    jump taylor_food_good
                "Crab Cakes":
                    jump taylor_food_ok
            # Post choice response
            label taylor_food_bad: # Onion Rings
                show taylor sad
                Taylor "Isn’t that more of an appetizer?"
                jump taylor_past
            label taylor_food_good: # Veggie Burger
                show taylor happy
                Taylor "That's right, you're a vegetarian too!"
                jump taylor_past
            label taylor_food_ok: # Crab Cakes
                show taylor neutral
                Taylor "I guess you can’t really go wrong with those."
                jump taylor_past

        # taylor past
        label taylor_past:
            show taylor neutral
            Taylor "So, how's it going?"
            menu:
                "Fine.":
                    jump taylor_past_bad
                "It’s been a tough week, but things are looking up!":
                    jump taylor_past_good
                "I didn't have such a great week.":
                    jump taylor_past_ok
            # Post choice response
            label taylor_past_bad: # Fine.
                show taylor sad
                Taylor "What, you still can't be honest with me?"
                jump taylor_dessert
            label taylor_past_good: # Architecture
                show taylor happy
                Taylor "Hey, that's great! Maybe I can help with your week too..."
                jump taylor_dessert
            label taylor_past_ok: # Comp Sci
                show taylor neutral
                Taylor "I’m sorry, I hope it takes a turn for the better soon…"
                jump taylor_dessert

        # taylor dessert
        label taylor_dessert:
            show taylor neutral
            Taylor "Dessert! The best meal, for sure! Whatcha thinkin'?"
            menu:
                "I think I’ll pass…":
                    jump taylor_dessert_bad
                "Chocolate milkshake":
                    jump taylor_dessert_good
                "Cheesecake":
                    jump taylor_dessert_ok
            # Post choice response
            label taylor_dessert_bad: # I think I'll pass...
                show taylor sad
                Taylor "That desperate to leave, huh?"
                jump start
            label taylor_dessert_good: # Chocolate milkshake
                show taylor happy
                Taylor "Oh my god, just like when we were kids!"
                jump start
            label taylor_dessert_ok: # Cheesecake.
                show taylor neutral
                Taylor "A true classic."
                jump start



    return

label bgm:

label choices:
