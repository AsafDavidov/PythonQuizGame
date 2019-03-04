##Final Project Assignment
##Asaf Davidov
from graphics import *
from buttonclass import *
from random import *
from wavemod import *

class Quiz:

    """Creates a Quiz game in a window.
    Will give four options for answers to questions.
    Will have endgame() method, right() and wrong() method"""

    def __init__(self,win, Questions = []):
        """initializes Quiz class"""
        self.win = win
        #intializes all of the questions in the quiz
        self.questions = Questions
        self.questions = ["8*8", "13*13", "16*4+8", "(1/2)*64", "15+5*2", "939/3",
                     "32/(1/2)", "512/128", "5*8*5", ".75*36"]
        
    def getQ(self):
        """Returns a question from the list"""
        givenquestion = self.questions.pop()
        return givenquestion
        
    def checkanswer(self,answer,question):
        """Checks to make sure the users answer is correct or not"""

        #Creates a random color background to appear more friendly to the user
        self.win.setBackground(color_rgb(randrange(0,255),randrange(0,255),randrange(0,255)))
        
        if answer == question:
            wm = WavMod('correctanswersound.wav')##added a sound effect for more user interaction
            wm.test()
            return True
            
        else:
            return False

    def gameover(self):
        """Creates a window when the User answers a question incorrectly"""
        self.win.delete('all')
        self.win.setBackground('dark red')#Creates upsetting background
        im = Image(Point(325,370), "sadface.gif")#Added a sad face picture
        im.draw(self.win)
        #then some text to instruct the user further
        endtext = Text(Point(325,250), "You answered incorrectly. You Lose")
        endtext.setSize(24)
        closetext = Text(Point(325,290), "Click anywhere to close")
        closetext.draw(self.win)
        endtext.draw(self.win)
        #lastly I added a sound for when the user answers the question wrong
        wm = WavMod('gameoversound.wav')
        wm.test()
        self.win.getMouse()
        

    def wingame(self):
        """Creates a window after the user answers all of the questions correctly"""
        self.win.delete('all')
        im = Image(Point(325,250), "celebration.gif")#Creates a celebratory background
        im.draw(self.win)
        #some text to help the user
        wintext = Text(Point(325,250), "You answered all the questions correctly! You Win!")
        wintext.setSize(18)
        closetext = Text(Point(325,290), "Click anywhere to close")
        closetext.draw(self.win)
        wintext.draw(self.win)
        #Sound fore when the user wins the game
        wm= WavMod('wingamesound.wav')
        wm.test()
        self.win.getMouse()
        


        

def main():
    win = GraphWin("Quiz Game", 650,500)
    ##Created Intializing texts to make game more user friendly
    initialtext = Text(Point(325,230),"This is a child's quiz game")
    initialtext.draw(win)
    starttext = Text(Point(325,250), "Click start to begin!")
    starttext.draw(win)
    exittext = Text(Point(325,270), "or click exit to quit")
    exittext.draw(win)
    goodtext = Text(Point(325,290), "Good Luck!")
    goodtext.draw(win)
    #Created list for these object so that it will be easier to remove them
    TextList = [initialtext,starttext,exittext,goodtext]
    
    #start and exit buttons
    startb = Button(win,Point(325,340),75,50,"Start")
    exitb = Button(win,Point(620,470),60,50,"Exit")
    ##Start the quiz class
    quiz = Quiz(win)
    #creates a list of all of the Questions
    allQuestions = []
    
    for i in range(10):
        allQuestions.append(quiz.getQ())

    #then asks for user mouse click
    pt=win.getMouse()
    
    gameprogress = True #intializes gameprogress boolean variable. this is to see if the game is in progress
    
    while not exitb.clicked(pt):#while loop for when the exit button is not clicked

        #'if' loop for when the user begins to do the game
        if startb.clicked(pt):
            win.setBackground('green')#sets background to a positive color

            #for loop to delete all the text from the original text
            for text in TextList:
                text.undraw()
            #intializing text to setup the quiz in a more user friendly way
            entry = Entry(Point(325,250), 20)
            entry.setText("Insert answer here")
            entry.draw(win)
            startb.undraw()
            answerb = Button(win,Point(325,340),110,50,"Check Answer")
            answertext = Text(Point(325, 100), "Answer the following mathematical statement:")
            answertext.draw(win)
            #For loop so that each question will be asked
            for i in range(len(allQuestions)):
                #Presents the text in a way that is legible
                questiontext = Text(Point(325,200),"")
                questiontext.setText(allQuestions[i])
                questiontext.setStyle('bold')
                questiontext.setSize(14)
                questiontext.draw(win)
                #then asks for another mouse click
                pt=win.getMouse()
                if answerb.clicked(pt):#checks to see if the answer button is clicked

                    #The following checks to see if the answer that the user gives is correct
                    if quiz.checkanswer(eval(entry.getText()), eval(allQuestions[i])) is True:
                        correcttext = Text(Point(325,150),"Good Job! keep going...")
                        correcttext.draw(win)
                        questiontext.undraw()
                        if i == 9:#this states that if user answers the final question correct
                            quiz.wingame()#Then it will start the wingame method
                            gameprogress = False
                            break
                                                                      
                    else:
                        quiz.gameover()#this says that if the user answers incorrect that they lose and have to start over
                        gameprogress = False
                        break
                    
                    
                elif exitb.clicked(pt):#this says that if the exit button is clicked the window will close
                    gameprogress = False
                    break
                    
                
             
        if not gameprogress:
            break
        pt = win.getMouse()#asks user for user click that way there are no breaks in the code
    win.close()#closes window if exit button is clicked

if __name__ == "__main__":
    main()
