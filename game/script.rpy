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

transform items:
    xalign 0.0
    yalign 0.05

label start: # TESTER
    $ score = 0
    scene bg black
    "BFF" "Who would you like to date?"
    $ ypos_c = True
    transform items:
        xalign 0.0
        yalign 0.05
    menu:
        "Brad":
            $ ypos_c = False
            call screen brad_dressup
        "Gold":
            $ ypos_c = False
            call screen gold_dressup
        "Owen":
            $ ypos_c = False
            call screen owen_dressup
        "Irving":
            $ ypos_c = False
            call screen irving_dressup
        "Taylor":
            $ ypos_c = False
            call screen taylor_dressup

    # scene bg restaurant
    # with fade
    # Bradley "Hey, uh, you look interesting…" # "can you change into something else? Please?"
    # Gold "blub..."
    # # show gold happy GOLD TOO LARGER
    # Owen "Now that's outfit's a hit!"

# label dressup:
#     transform items:
#         xalign 0.0
#         yalign 0.05
#
#     # call screen dressup
#     call screen dressup




label characters:
    # BRADLEY CHARACTER ARC
    label brad:


        # Bradley Outfit Eval
        # If outfit == Bad:
        label brad_outfit_bad:
            scene bg restaurant
            show bradley sad
            Bradley "Hey, uh, you look interesting…" # "can you change into something else? Please?"
            $ score += 1
            jump brad_food
        # else if outfit == Good:
        label brad_outfit_good:
            scene bg restaurant
            show bradley happy
            Bradley "Hello! You certainly look lovely tonight…" # "Oh my god, you look absolutely gorgeous!"
            $ score += 3
            jump brad_food

        # Bradley Food
        label brad_food:
            show bradley neutral
            Bradley "What do you want to order?"
            menu:
                "Cheeseburger":
                    $ score -= 1
                    jump brad_food_bad
                "Lobster":
                    $ score += 1
                    jump brad_food_good
                "Chicken Alfredo":
                    jump brad_food_ok
            # Post choice response
            label brad_food_bad: # Cheeseburger
                show bradley sad
                Bradley "Might as well go to McDonald's"# "Really, a cheeseburger in a fancy restaurant?" # "Might as well go to McDonald's"
                jump brad_work
            label brad_food_good: # Lobster
                show bradley happy
                Bradley "This place is famous for its lobster, I'm glad you knew that!"#"Wow, someone with good taste!" # "This place is famous fro its lobster."
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
                    $ score -= 1
                    jump brad_job_bad
                "I'm a freelancer":
                    $ score += 1
                    jump brad_job_good
                "Taking a break for now":
                    jump brad_job_ok
            # Post choice response
            label brad_job_bad: # I'm in between jobs right now
                show bradley sad
                Bradley "I think I have to reconsider this date..."#"So... you're unemployed is what I'm hearing."
                jump brad_dessert
            label brad_job_good: # I'm a freelancer
                show bradley happy
                Bradley "Excellent, working on your own is one step away from starting your own business!" #"Nice, I respect being your own boss!"
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
                    $ score -= 1
                    jump brad_dessert_bad
                "Macarons":
                    $ score += 1
                    jump brad_dessert_good
                "Ice cream":
                    jump brad_dessert_ok
            # Post choice resposne
            label brad_dessert_bad: # No dessert
                show bradley sad
                Bradley "Absolutely disappointing."#"Sigh... Suit yourself."
                jump brad_end
            label brad_dessert_good: # Macarons
                show bradley happy
                Bradley "Alors toi aussi tu aimes les desserts français!"
                jump brad_end
            label brad_dessert_ok: # Ice cream
                show bradley neutral
                Bradley "I guess you can never go wrong with ice cream!"
                jump brad_end

        label brad_end:
            if score == 6:
                jump ending_perfect
            elif score >= 4:
                jump ending_good
            else:
                jump ending_bad


    # GOLD CHARACTER ARC
    label gold:

        # Gold Outfit Eval
        # If outfit == Bad:
        label gold_outfit_bad:
            scene bg underwater
            show gold sad
            Gold "blub..."
            $ score += 1
            jump gold_food
        # else if outfit == Good:
        label gold_outfit_good:
            scene bg underwater
            show gold happy
            Gold "BLUB BLUB!!"
            $ score += 3
            jump gold_food

        # Gold Food
        label gold_food:
            show gold neutral
            Gold "Blub blub blub?"
            menu:
                "Fish sticks":
                    $ score -= 1
                    jump gold_food_bad
                "Steak":
                    $ score += 1
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
                    $ score -= 1
                    jump gold_query_bad
                "Oh my god, you're so funny!":
                    $ score += 1
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
                    $ score -= 1
                    jump gold_dessert_bad
                "Tiramisu":
                    $ score += 1
                    jump gold_dessert_good
                "Jello":
                    jump gold_dessert_ok
            # Post choice response
            label gold_dessert_bad: # Taiyaki
                show gold sad
                Gold "Blub..."
                jump gold_end
            label gold_dessert_good: # Tiramisu
                show gold happy
                Gold "BLUB BLUB!!"
                jump gold_end
            label gold_dessert_ok: # Jello
                show gold neutral
                Gold "blub blub blub"
                jump gold_end

            label gold_end:
                if score == 6:
                    jump ending_perfect
                elif score >= 4:
                    jump ending_good
                else:
                    jump ending_bad


    # OWEN CHARACTER ARC
    label owen:

        # Owen Outfit Eval
        # If outfit == Bad:
        label owen_outfit_bad:
            scene bg shakeys
            show owen sad
            Owen "Hm, not sure how game I am for your outfit..."
            $ score += 1
            jump owen_food
        # else if outfit == Good:
        label owen_outfit_good:
            scene bg shakeys
            show owen happy
            Owen "Now that's outfit's a hit!"
            $ score += 3
            jump owen_food

        # Owen Food
        label owen_food:
            show owen neutral
            Owen "What d'ya wanna eat?"
            menu:
                "Pizza":
                    $ score -= 1
                    jump owen_food_bad
                "Salad and Vegetable Smoothie":
                    $ score += 1
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
                    $ score -= 1
                    jump owen_sports_bad
                "Football":
                    $ score += 1
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
                Owen "Oh that sport from the Lord of the Rings? That's cool!"
                jump owen_dessert

        # Owen dessert
        label owen_dessert:
            show owen neutral
            Owen "You up for dessert?"
            menu:
                "Cheesecake":
                    $ score -= 1
                    jump owen_dessert_bad
                "I think I'll pass on dessert.":
                    $ score += 1
                    jump owen_dessert_good
                "Fruit salad":
                    jump owen_dessert_ok
            # Post choice resposne
            label owen_dessert_bad: # Cheesecake
                show owen sad
                Owen "Yikes..."
                jump owen_end
            label owen_dessert_good: # I think I'll pass on dessert.
                show owen happy
                Owen "Now that's thinkin' healthy!"
                jump owen_end
            label owen_dessert_ok: # Fruit salad
                show owen neutral
                Owen "Those are kinda sugary, but at least it's all-natural!"
                jump owen_end

            label owen_end:
                if score == 6:
                    jump ending_perfect
                elif score >= 4:
                    jump ending_good
                else:
                    jump ending_bad


    # IRVING CHARACTER ARC
    label irving:
        # irving Outfit Eval
        # If outfit == Bad:
        label irving_outfit_bad:
            scene bg french
            show irving sad
            Irving "Were you in a bit of a rush getting here?"
            $ score += 1
            jump irving_food
        # else if outfit == Good:
        label irving_outfit_good:
            scene bg french
            show irving happy
            Irving "My, don’t you look dashing! Truly elegant…"
            $ score += 3
            jump irving_food

        # irving Food
        label irving_food:
            show irving neutral
            Irving "What are we craving tonight, darling?"
            menu:
                "Pasta salad":
                    $ score -= 1
                    jump irving_food_bad
                "Shrimp Ceviche":
                    $ score += 1
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
                    $ score -= 1
                    jump irving_study_bad
                "Architecture":
                    $ score += 1
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
                    $ score -= 1
                    jump irving_dessert_bad
                "Creme Brulee":
                    $ score += 1
                    jump irving_dessert_good
                "Nope, no dessert for me!":
                    jump irving_dessert_ok
            # Post choice response
            label irving_dessert_bad: # Brownie Sunday
                show irving sad
                Irving "Immaturity is the incapacity to use one’s intelligence without the guidance of another."
                jump irving_end
            label irving_dessert_good: # I think I'll pass on dessert.
                show irving happy
                Irving "Decisions are the frequent fabric of our daily design."
                jump irving_end
            label irving_dessert_ok: # I think I'll pass on dessert.
                show irving neutral
                Irving "The content of your character is your choice"
                jump irving_end

            label irving_end:
                if score == 6:
                    jump ending_perfect
                elif score >= 4:
                    jump ending_good
                else:
                    jump ending_bad


    # TAYLOR CHARACTER ARC
    label taylor:
        # taylor Outfit Eval
        # If outfit == Bad:
        label taylor_outfit_bad:
            scene bg midtier
            show taylor sad
            Taylor "Oh, uh hey! Almost didn’t recognize you there…"
            $ score += 1
            jump taylor_food
        # else if outfit == Good:
        label taylor_outfit_good:
            scene bg midtier
            show taylor happy
            Taylor "Wow, it’s been so long but you look so good!"
            $ score += 3
            jump taylor_food

        # taylor Food
        label taylor_food:
            show taylor neutral
            Taylor "All right, what's on the menu tonight?"
            menu:
                "Onion Rings":
                    $ score -= 1
                    jump taylor_food_bad
                "Veggie Burger":
                    $ score += 1
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
                    $ score -= 1
                    jump taylor_past_bad
                "It’s been a tough week, but things are looking up!":
                    $ score += 1
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
                    $ score -= 1
                    jump taylor_dessert_bad
                "Chocolate milkshake":
                    $ score += 1
                    jump taylor_dessert_good
                "Cheesecake":
                    jump taylor_dessert_ok
            # Post choice response
            label taylor_dessert_bad: # I think I'll pass...
                show taylor sad
                Taylor "That desperate to leave, huh?"
                jump taylor_end
            label taylor_dessert_good: # Chocolate milkshake
                show taylor happy
                Taylor "Oh my god, just like when we were kids!"
                jump taylor_end
            label taylor_dessert_ok: # Cheesecake.
                show taylor neutral
                Taylor "A true classic."
                jump taylor_end

            label taylor_end:
                if score == 6:
                    jump ending_perfect
                elif score >= 4:
                    jump ending_good
                else:
                    jump ending_bad



    # PERFECT ENDING
    label ending_perfect:
        scene bg perfect ending
        "Is this true love? You've matched perfectly with your date!"
        menu:
            "Start again":
                jump start



    # GOOD ENDING
    label ending_good:
        scene bg good ending
        "Congrats! You've finally found someone to help you move over your ex..."
        menu:
            "Start again":
                jump start



    # BAD ENDING
    label ending_bad:
        scene bg bad ending
        "Unfortunately, this date didn't go as well as you hoped... But that's ok! Keep trying!"
        menu:
            "Start again":
                jump start



    return

label bgm:

label choices:
