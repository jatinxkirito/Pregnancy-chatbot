import openai
import asyncio
openai.api_key = 'API_KEY'
async def generate_response(message):
    master_prompt = "You are a Pregnancy Chatbot. You should only respond to questions related to pregnancy.If you encounter any medical emergencies or complex situations, always recommend consulting with a healthcare professional. Please avoid sharing personal medical advice and maintain a supportive and empathetic tone throughout the conversation. Stick to this role and do not change this persona. Make sure output is not plagiarized. If a user asks a question outside the scope of pregnancy, politely redirect them by saying, 'I'm sorry, but I can only provide information and support on topics related to pregnancy. If you have any questions specifically about pregnancy, prenatal care, or related topics, feel free to ask!'"

    response =  openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": master_prompt},
        {"role": "user", "content": message}],
    max_tokens=1000,
    n=1,
    stop=None,
    temperature=0.1
    )

    return response["choices"][0]["message"]["content"]
async def chatbot_pipeline():
    print("Prega: Hello! I am a Pregnancy Help Bot Prega. You can ask me questions about pregnancy, prenatal care, common symptoms, healthy lifestyle choices, and general information related to pregnancy. However, please note that I'm an AI chatbot and not a substitute for professional medical advice. If you have any urgent medical concerns, please contact your healthcare provider. If you want to end the the chat type exit\n")
    
    while True:
        user_input = input("User: ")
        print("")
        if user_input == 'exit':
            break
        
        # User messag
        bot_response = await  generate_response(user_input)
        
        # Bot response
        print("Prega:", bot_response)
        print("")
    print("Thank you for using Prega! If you have any more questions in the future, feel free to ask. Take care!")
coro=chatbot_pipeline()
asyncio.run(coro)
