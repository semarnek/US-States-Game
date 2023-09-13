import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
screen.bgpic("blank_states_img.gif")
foundlist = []
states_foundlist = []

def state_show(states_found):
    state_turte = turtle.Turtle()
    state_turte.shape("circle")
    state_turte.hideturtle()
    state_turte.shapesize(stretch_wid=0.15, stretch_len=0.15)
    state_turte.color("black")
    x = states_found[1]
    y = states_found[2]
    state_turte.penup()
    state_turte.showturtle()
    state_turte.goto(x, y)
    state_turte.write(f"{states_found[0]}", align="center")



try:

    states_foundlist = pandas.read_csv("states_learnt.csv").values.tolist()
    for state in states_foundlist:
        foundlist.append(state[0])




except FileNotFoundError:
    states = pandas.read_csv("50_states.csv").values
    states_foundlist = []
    foundlist = []

else:
    states = pandas.read_csv("50_states.csv").values

    if len(foundlist) < 50 :
        input = screen.textinput(title="Saved Game Found", prompt="Do you want to continue from the saved game?")

        if input == None or input.lower() == "no":
            states_foundlist = []
            foundlist = []

        else:
            for state in states_foundlist:
                state_show(state)
    else:
        states_foundlist = []
        foundlist = []




total = 50
game_is_on = True


while len(foundlist) < 50:
    guess = screen.textinput(title=f"{len(states_foundlist)}/{total} States Correct", prompt="What's another state name?\nType 'Exit' and click OK to save the game")
    for state in states:
        if state[0] == guess.title() and foundlist.count(guess.title()) == 0:
            foundlist.append(state[0])
            states_foundlist.append(state)
            state_show(state)

    if guess.title() == "Exit":

        # missing_states = [state[0] for state in states if state[0] not in foundlist]
        # #for state in states:
        # #    if state[0] not in states_foundlist:
        # #       missing_states.append(state[0])
        # new_data = pandas.DataFrame(missing_states)
        # new_data.to_csv("states_to_learn.csv")
        break


    if len(states_foundlist) == 50:
        turtle.hideturtle()
        turtle.write("Well done! You have found all states in US!", align="center", font=("Courier", 20, "bold"))
        states_learn = pandas.DataFrame(states_foundlist)
        states_learn.columns = ['state', 'x', 'y']
        states_learn.to_csv("states_learnt.csv", index=False)
        break

    states_learn = pandas.DataFrame(states_foundlist)
    states_learn.columns = ['state', 'x', 'y']
    states_learn.to_csv("states_learnt.csv", index=False)


screen.exitonclick()