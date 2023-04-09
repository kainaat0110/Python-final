from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('chatbot',read_only=False,
                logic_adapters=[
                    {
                        'import_path':'chatterbot.logic.BestMatch',
                        'default_response':'Sorry, I dont know what that means',
                        'maximum_similarity_threashold':0.90

                    }])

list_to_train =[
    "hii",#question
    "hii , there",#answer
    "Whats your name?",
    "I'm just a chatbot",
    "What is your fav food?",
    "I like cheese",
]

list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

def index(request):
    return render(request,'chatbot/index.html')

def getResponse(request):
   userMessage = request.GET.get('userMessage')
   chatResponse = str(bot.get_response(userMessage))
   return HttpResponse(chatResponse)