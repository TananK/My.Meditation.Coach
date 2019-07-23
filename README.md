# Welcome to My Meditation Coach Alexa skill

My Meditation Coach Alexa skill is creted to help Alexa users meditate effectively by having a deeper understanding of the root and concept behind the practice. The vision is to create an AI-powered meditation coach for people who are starting out in meditation.

This is an open-source project. We welcome mindful contributor to make improvement by adding features and contents to the skill.

There are two important components of the skill

1) intents json
2) Lambda function

The intents json is used to build an Alexa intents.

Lambda function from AWS is used to power the responses after the intents are invoked.

## How to make your own meditation coach skill

1. Sign up an Alexa developer account at https://developer.amazon.com
2. Create a custom Alexa skill on the Alexa developer console. More detail at https://developer.amazon.com/docs/custom-skills/steps-to-build-a-custom-skill.html
3. Copy the content of intents.json into Intents JSON 
4. Sign up AWS service at https://aws.amazon.com/
5. Zip the Lambda function from this repo and upload it to your Lambda function to create the engine for the skill
6. Connect your skill to the lambda function. More detail at https://developer.amazon.com/docs/custom-skills/host-a-custom-skill-as-an-aws-lambda-function.html
7. Once the Alexa skill and Lambda function are connected, feel free to poke around and modify the intents and response for your pleasure.
8. Submit your skill to Amazon and wait for approval
9. Once approved, your skill will be on live. Let us know so we can use it too!
