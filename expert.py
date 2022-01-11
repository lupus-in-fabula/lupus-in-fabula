from human import Human

# create Expert class, inherited from Human -- most experts are indeed humans

class Expert(Human):

    def tellMotivation(self):
        print("Oh, I'm motivated allright.")

    def help(self):
        print("Why don't you ask me to...")
