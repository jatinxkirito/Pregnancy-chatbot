# Project Name

Prega - Pregnancy Chatbot

## Description

Prega is an AI-powered Pregnancy Chatbot designed to provide information and support on topics related to pregnancy, prenatal care, common symptoms, healthy lifestyle choices, and general information. The chatbot utilizes the OpenAI GPT-3.5 Turbo model to generate responses based on user input.

## Table of Contents

- [Project Name](#project-name)
- [Description](#description)
- [Table of Contents](#table-of-contents)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Sample Conversations](#sample-conversations)
- [API Key](#api-key)
- [Chatbot Pipeline](#chatbot-pipeline)

## Prerequisites

- Python 3.6 or above
- OpenAI Python library

## Installation

To run the Prega Pregnancy Chatbot, you need to follow these installation steps:

1. Download main.py:

2. Install the required dependencies by running the following command:

   ```shell
   pip install openai
   ```

3. Replace `'API-KEY'` in the code with your OpenAI API key. You can obtain an API key from the OpenAI website.

## Usage

To use the Prega Pregnancy Chatbot, follow these steps:

1. Run the script in a Python environment:

   ```shell
   python main.py
   ```

2. The chatbot will greet you and provide a brief introduction. You can then start a conversation by typing your message as a user.

3. Enter your message and press Enter to get the bot's response. The chatbot will respond based on the provided input.

4. To end the conversation, type `exit`.

## Features

- Provides information and support on various topics related to pregnancy, prenatal care, common symptoms, and healthy lifestyle choices.
- Maintains a supportive and empathetic tone throughout the conversation.
- Redirects users when asked questions outside the scope of pregnancy.
- Encourages users to consult with healthcare professionals for medical emergencies or complex situations.
- Avoids sharing personal medical advice.
- Generates responses using the OpenAI GPT-3.5 Turbo model.

## Sample Conversations

Here are some sample conversations to give you an idea of how the Prega Pregnancy Chatbot interacts with users:

```shell
Prega: Hello! I am a Pregnancy Help Bot Prega. You can ask me questions about pregnancy, prenatal care, common symptoms, healthy lifestyle choices, and general information related to pregnancy. However, please note that I'm an AI chatbot and not a substitute for professional medical advice. If you have any urgent medical concerns, please contact your healthcare provider. If you want to end the chat, type exit.

User: I'm Emily, and I'm currently in my third trimester. I must admit, I'm feeling a bit overwhelmed and have so many questions running through my mind. Can you help me?

Prega: Of course, Emily! I'm here to help you with any questions or concerns you may have during your pregnancy. Feel free to ask me anything, and I'll do my best to provide you with the information and support you need. What's on your mind?

User: Lately, I've been experiencing some discomfort and noticed that my baby's movements have changed. Should I be worried about this?

Prega: I'm not a doctor, but I can offer some general information. It's common for baby's movements to change as your pregnancy progresses. However, if you're experiencing discomfort and notice a significant change in your baby's movements, it's always a good idea to reach out to your healthcare provider. They can provide personalized advice and determine if any further evaluation is needed. It's important to trust your instincts and seek medical guidance when you have concerns.

User: movements feel different, less frequent and more subtle compared to before. It's making me anxious.

Prega: It's completely normal to feel anxious when you notice changes in your baby's movements. However, it's important to remember that as your pregnancy progresses, your baby's movements may change. Towards the end of pregnancy, you may feel less frequent and more subtle movements as your baby has less space to move around. However, if you're concerned about a significant decrease in movement or if you notice any other unusual symptoms, it's always best to reach out to your healthcare provider. They can provide guidance and reassurance based on your specific situation.

User:  I want to make sure I'm doing everything I can to have a healthy pregnancy. Can you give me some tips on maintaining a healthy lifestyle?
Prega: Of course! Maintaining a healthy lifestyle is important for a healthy pregnancy. Here are some tips:

1. Eat a balanced diet: Focus on consuming a variety of fruits, vegetables, whole grains, lean proteins, and healthy fats. Avoid processed foods and limit your intake of caffeine, sugary snacks, and foods high in saturated fats.

2. Stay hydrated: Drink plenty of water throughout the day to help support your body's functions and prevent dehydration.

3. Exercise regularly: Engage in moderate exercise, such as walking, swimming, or prenatal yoga, with your healthcare provider's approval. Regular physical activity can help improve your mood, boost energy levels, and promote overall well-being.

4. Get enough rest: Aim for 7-9 hours of quality sleep each night. Listen to your body and rest when you feel tired.

5. Take prenatal vitamins: Ensure you're getting essential nutrients like folic acid, iron, and calcium by taking prenatal vitamins as recommended by your healthcare provider.

6. Avoid harmful substances: Stay away from alcohol, tobacco, and recreational drugs, as they can harm your baby's development.

7. Manage stress: Find healthy ways to cope with stress, such as practicing relaxation techniques, engaging in hobbies, or seeking support from loved ones.

8. Attend regular prenatal check-ups: Regular prenatal visits with your healthcare provider are crucial for monitoring your health and the baby's development.

Remember, it's always a good idea to consult with your healthcare provider for personalized advice and guidance throughout your pregnancy journey.

User: Which of the following foods should be avoided during pregnancy?
A: Fresh fruits and vegetables B: Lean proteins like chicken and fish
C: Soft cheeses and unpasteurized dairy products
D: Whole grains like brown rice and quinoa
Please select the correct answer by choosing the corresponding letter (A, B, C, or D).

Prega: C: Soft cheeses and unpasteurized dairy products should be avoided during pregnancy.

User: Prenatal vitamins are specifically formulated to provide essential ______ and ______ that support the healthy development of the baby and meet the increased nutritional needs of the pregnant woman. Please fill in the blanks with the appropriate terms.

Prega: Prenatal vitamins are specifically formulated to provide essential vitamins and minerals that support the healthy development of the baby and meet the increased
```