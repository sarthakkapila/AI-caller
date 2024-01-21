# Plan (till now)

Making an ai caller 

### App will contains 3 parts
1.) Speech to text something like OpenAI whisper (probably) which listens to what the user says and then converts it to text.
2.) Then the text is put into a ML model (salesGPT) to get an answer.
3.) The answer/output is then put into a TTS syntesizer and is heard by the user as output.

I am planning to do all this by using crewAI agents or hitting endpoint of API of eleven labs and assembly and using a local model on my system

The crewAI - 
Will make agents and hit api and run stuff (ig). 