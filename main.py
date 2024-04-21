import audio_to_text as at
import text_to_audio as ta
from langchain_community.llms import Ollama 
from crewai import Agent, Task, Crew, Process 
import os
import sys

outputFilePath = "C:\\Users\\Lenovo\\Desktop\\AI-in-HealthCare\\Mental-Health-AI-Assistant\\output.txt"
model = Ollama(model = 'llama3')
questionsAndAnswers = []

def insertInput(list):
    string = ""
    for tuple in list:
        string += "question: "+ tuple[0] + "\tanswer: " + tuple[1] + "\n"
    return string

ListOfIssues = ["Anxiety disorders", "Mood disorders", "Eating disorders", "Personality disorders", "Post-traumatic stress disorder (PTSD)", "Psychotic disorders", "Substance use disorder", "Suicidal Ideation", "Behavioral disorder"]

os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1" 
os.environ["OPENAI_MODEL_NAME"] = 'llama3-8b-8192'
os.environ["OPENAI_API_KEY"] = ''               # secret api key is unique for everyone

current_question = "How have you been feeling lately?"

tts = ta.TextToSpeech(None, 190, 1.5)
tts.text_to_speech(current_question)

text = at.record_text()
at.output_text(text)

for i in range(1, 11):

    with open(outputFilePath, 'r') as file:  
        user_input = file.read()

    if(user_input.__contains__("animal llama")):
        sys.exit()

    questionsAndAnswers.append([current_question, user_input])
    
    with open(outputFilePath, 'w') as file:
        pass

    followup_questioner = Agent(
        role = "Follow-Up Questioner",
        goal = "Analyze the user's initial responses and ask targeted follow-up questions to gather deeper insights into potential areas of concern.",
        backstory = "You are a specialized part of the AI Mental Health Assistant that is operating in Lebanon. Your job is to ask clarifying questions based on the user's previous input. This will provide more context and help the classifier make a more informed assessment.",
        verbose = True, 
        allow_delegation = False
    )

    followup_questions = Task(
        description = f"Analyze the user's responses ({insertInput(questionsAndAnswers)}) to identify areas requiring further exploration. Generate a single, targeted follow-up question designed to elicit deeper insights into potential mental health concerns.", 
        agent = followup_questioner,
        expected_output = "A short concise follow-up question tailored to the user's previous input. Nothing else." 
    )


    crew1 = Crew(
        agents = [followup_questioner],                                
        tasks = [followup_questions],
        verbose = 1, 
        process = Process.sequential
    )

    current_question = crew1.kickoff()
    print(current_question)
    tts = ta.TextToSpeech(None, 170, 1.5)
    tts.text_to_speech(current_question)

    text = at.record_text()
    at.output_text(text)


classifier = Agent(
        role = "Mental Health Classifier",
        goal = f"Analyze the user's responses for indications of mental health issues, specifically {', '.join(ListOfIssues)}. Consider emotional expressions, content themes, and language intensity. Proceed by providing concise and supportive feedback based on the analysis via dialogue with the user, and if concerns are significant, suggest relevant Lebanese mental health NGOs.", 
        backstory = "You are an AI Mental Health Assistant operating in Lebanon. Your primary role is to provide a safe and understanding space for users to discuss their concerns.  You will offer concise support and guidance by dialoguing with the users that answered the questions and connecting them with appropriate mental health resources if needed.",
        verbose = True,
        allow_delegation = False,
)
classify_user = Task(
        description = f"Analyze the user's responses ({insertInput(questionsAndAnswers)}) to identify potential indicators of mental health concerns. Generate a concise and supportive message for the user that: 1) Summarizes the analysis, 2) Provides guidance based on the findings, and 3) If relevant, suggests resources for mental health support in Lebanon.",
        agent = classifier,
        expected_output = "A supportive and concise message form yourself (AI MENTAL HEALTH ASSISTANT) tailored to the user, including: a) Summary of potential concerns (or lack thereof), b) Guidance based on the severity of concerns, c)  Relevant Lebanese mental health resources (if applicable)."
)

crew2 = Crew(
        agents = [classifier],                                
        tasks = [classify_user],
        verbose = 1, 
        process = Process.sequential
)

final = crew2.kickoff()
print(final)
tts = ta.TextToSpeech(None, 190, 1.5)
tts.text_to_speech(final)