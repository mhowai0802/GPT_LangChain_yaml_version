Sentence_testing = {
    "Example_currency" : "Please convert $500 USD to AED",
    "Example_email" : "I am Daniel send an annual leave email to tony.c.lin@pccw.com from 25/6 to 28/6"
}
agent_openai = object.openai()
print(agent_openai.run(Sentence_testing['Example_currency']))
