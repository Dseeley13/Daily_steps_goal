#define a function
def main():

#define set_steps_goal():
    def set_steps_goal():
#I added this... just incase the person inputting it doesn't have a valid integer. I got this from one of the homeworks
        while True:
            try:
                goal = int(input(f'Please enter your daily steps goal:'))
                break
            except:
                print(f'Please enter a valid integer')

        return goal
    step_goal = set_steps_goal()

#define record_daily_steps
    def record_daily_steps():
        steps = 0
        for x in range(1,8):
            while True:
                    try:
                        daily_steps = int(input(f'Please enter your daily steps for day {x}:'))
                        steps = steps + daily_steps
                        break
                    except:
                        print(f'Please enter a valid integer')

        return steps


    steps = record_daily_steps()
#define evaluate_weekly_performance
    def evaluate_weekly_performance(step_goal, steps):
        average_steps = steps / 7
        print(f'Average daily steps for this week: {average_steps:.2f}')

        if average_steps > step_goal:
            print(f'Congratulations! You exceeded your daily step goal average!')
        elif average_steps == step_goal:
            print(f'Congratulations! You met your daily step goal average!')
        else:
            print(f'You did not meet your daily step goal average :(')

    evaluate_weekly_performance(step_goal,steps)


#Need this for the main def function to run
main()