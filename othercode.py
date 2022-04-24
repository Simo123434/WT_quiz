     
        
            
        
        
        
        
        # load the image data from usa in data
        # question_length = len(usa)
        # for i in usa:
        #     questions_answered = 0
        #     asked_questions = []
        #     # pick a random question
        #     if questions_answered == question_length:
        #         self.finish()
        #     random_question = random.randint(0, question_length - 1)
        #     answer = usa[random_question]["answers"]
        #     image = usa[random_question]["image"]
        #     if image in asked_questions:
        #         break
        #     else:
        #         # show image onscreen
        #         self.img = ImageTk.PhotoImage(Image.open(image))
        #         self.canvas.create_image(500, 600, anchor = S ,image=self.img)
        #         asked_questions.append(image)
        #         questions_answered += 1
        #         # create entry box to get input
        #         self.user_input = Entry(self.window, width=30)
        #         self.user_input.place(x=400, y=600)
        #         # when enter is pressed check if answer is correct
        #         self.user_input.bind("<Return>", lambda event: self.check_answer(self.user_input, answer, random_question))

















    def next_question(self, question_length):
        # clear screen
        for widget in self.window.winfo_children():
            widget.destroy() 
        # Text at top
        self.canvas = Canvas(self.window, width=1000, height=800)
        self.canvas.create_text(500, 100, text="What is this tank?", font=("Arial", 30))
        self.canvas.pack()
        # load the image data from usa in data
        for i in usa:
            asked_questions = []
            # pick a random question
            random_question = random.randint(0, question_length - 1)
            answer = usa[random_question]["answers"]
            image = usa[random_question]["image"]
            if image in asked_questions:
                break
            else:
                # show image onscreen
                self.img = ImageTk.PhotoImage(Image.open(image))
                self.canvas.create_image(500, 600, anchor = S ,image=self.img)
                asked_questions.append(image)
                # create entry box to get input
                self.user_input = Entry(self.window, width=30)
                self.user_input.place(x=400, y=600)
                # when enter is pressed check if answer is correct
                self.user_input.bind("<Return>", lambda event: self.check_answer(self.user_input, answer, random_question))
                
                
    def check_answer(self, user_answer, answer, random_question):
        self.user_answer = user_answer.get()
        self.answer = answer
        self.random_question = random_question
        if self.user_answer.lower() in self.answer:
            self.canvas.create_text(500, 650, text="Correct!", font=("Arial", 20))
            self.canvas.create_text(500, 700, text="Press enter to continue", font=("Arial", 20))
            self.user_input.bind("<Return>", lambda event: self.next_question(self.random_question))
        else:
            self.canvas.create_text(500, 650, text="Incorrect!", font=("Arial", 20))
            self.canvas.create_text(500, 700, text="The correct answer is: " + self.answer[0], font=("Arial", 20))