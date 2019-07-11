# Title : My Medication Coach Alexa Skill
# Author : Tanan Kesornbua
# Date : 01-06-2019

from ask_sdk_core.skill_builder import SkillBuilder

sb = SkillBuilder()

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard

import sentences


# Default classes
class LaunchRequestHandler(AbstractRequestHandler):
     def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

     def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        speech_text = sentences.WELCOME_MESSAGE
        speech_text += sentences.MAIN_MENU
        speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
        ask_text = sentences.SPEECH_RESPONSE.format(sentences.MAIN_MENU)
        attr["main_topic"] = "MainMenu"
        attr["sub_topic"] = ""
        attr["time_count"] = 0
        handler_input.attributes_manager.session_attributes = attr
        # Response builder
        handler_input.response_builder.speak(speak_text).ask(ask_text).set_card(
            SimpleCard(sentences.SKILL_TITLE, sentences.MAIN_MENU)).set_should_end_session(False)
        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        if attr["sub_topic"] == "SetTime":
            speech_text = sentences.SETTIME_HELP
            speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
        elif attr["sub_topic"] == "Meditating":
            speech_text = sentences.MEDITATING_HELP
            speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
        elif attr["main_topic"] == "Summary":
            speech_text = sentences.SUMMARY_HELP
            speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
        else:
            speech_text = sentences.MAIN_MENU_HELP
            speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
        # Response builder
        handler_input.response_builder.speak(speak_text).ask(speak_text).set_card(
            SimpleCard(sentences.SKILL_TITLE, sentences.MAIN_MENU)).set_should_end_session(
            False)
        return handler_input.response_builder.response


class CancelAndStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.CancelIntent")(handler_input) or is_intent_name("AMAZON.StopIntent")(handler_input) or is_intent_name("AMAZON.NavigateHomeIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        if attr["main_topic"] == "MainMenu" or attr["main_topic"] == "Summary":
            handler_input.response_builder.set_should_end_session(True)
            return handler_input.response_builder.response
        elif attr["sub_topic"] == "Meditating":
            speech_text = sentences.SUMMARY_THOUGHT_QUESTION
            attr["main_topic"] = "Summary"
            attr["sub_topic"] = "Distracted"
        else:
            speech_text = sentences.MAIN_MENU
            attr["main_topic"] = "MainMenu"
            attr["sub_topic"] = ""
        speak_text = sentences.SPEECH_RESPONSE.format(speech_text)        
        handler_input.attributes_manager.session_attributes = attr
        # Response builder
        handler_input.response_builder.speak(speak_text).ask(speak_text).set_card(
            SimpleCard(sentences.SKILL_TITLE, sentences.MAIN_MENU)).set_should_end_session(
            False)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # any cleanup logic goes here
        speech_text = sentences.THANK_YOU
        speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
        handler_input.response_builder.speak(speak_text).ask(ask_text).set_card(
            SimpleCard(sentences.SKILL_TITLE, sentences.MAIN_MENU)).set_should_end_session(True)
        return handler_input.response_builder.response


# Exception Handler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler

class AllExceptionHandler(AbstractExceptionHandler):

    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        # Log the exception in CloudWatch Logs
        speak_text = sentences.SPEECH_RESPONSE.format(sentences.ERROR) 
        handler_input.response_builder.speak(speak_text).ask(speak_text)
        return handler_input.response_builder.response


# Meditation Benefit classes
## There are three sub topics
### Posture
### Focal Point
### Recitation

class MeditationBenefitIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("MeditationBenefit")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        attr["main_topic"] = "MeditationBenefit"
        speech_text = sentences.MEDITATION_BENEFIT
        speak_text = sentences.SPEECH_RESPONSE.format(speech_text)        
        handler_input.attributes_manager.session_attributes = attr
        # Response builder
        handler_input.response_builder.speak(speak_text).ask(speak_text).set_card(
            SimpleCard(sentences.SKILL_TITLE, sentences.MAIN_MENU)).set_should_end_session(
            False)
        return handler_input.response_builder.response


class BenefitPostureIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("Posture")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        attr["main_topic"] = "MeditationBenefit"
        attr["sub_topic"] = "Posture"
        handler_input.attributes_manager.session_attributes = attr
        speech_text = sentences.BENEFIT_POSTURE
        speech_text += sentences.NOTICE_SOUND
        speech_text += sentences.MEDITATION_BENEFIT
        speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
        ask_text =  sentences.SPEECH_RESPONSE.format(sentences.MEDITATION_BENEFIT)
        handler_input.response_builder.speak(speak_text).ask(ask_text).set_card(
            SimpleCard(sentences.SKILL_TITLE, sentences.MAIN_MENU)).set_should_end_session(
            False)
        return handler_input.response_builder.response


class BenefitFocalPointIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("FocalPoint")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        attr["main_topic"] = "MeditationBenefit"
        attr["sub_topic"] = "FocalPoint"
        handler_input.attributes_manager.session_attributes = attr
        speech_text = sentences.BENEFIT_FOCALPOINT
        speech_text += sentences.NOTICE_SOUND
        speech_text += sentences.MEDITATION_BENEFIT
        speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
        ask_text =  sentences.SPEECH_RESPONSE.format(sentences.MEDITATION_BENEFIT)
        handler_input.response_builder.speak(speak_text).ask(ask_text).set_card(
            SimpleCard(sentences.SKILL_TITLE, sentences.MAIN_MENU)).set_should_end_session(
            False)
        return handler_input.response_builder.response


class BenefitRecitationIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("Recitation")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        attr["main_topic"] = "MeditationBenefit"
        attr["sub_topic"] = "Recitation"
        handler_input.attributes_manager.session_attributes = attr
        speech_text = sentences.BENEFIT_RECITATION
        speech_text += sentences.NOTICE_SOUND
        speech_text += sentences.MEDITATION_BENEFIT
        speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
        ask_text =  sentences.SPEECH_RESPONSE.format(sentences.MEDITATION_BENEFIT)
        handler_input.response_builder.speak(speak_text).ask(ask_text).set_card(
            SimpleCard(sentences.SKILL_TITLE, sentences.MAIN_MENU)).set_should_end_session(
            False)
        return handler_input.response_builder.response


# Meditation Session Classes
## There are three sub topics
### Quick
### Five min
### Fifteen min
### Thirty min

class MeditationSessionIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("MeditationSessionIntent")(handler_input) 

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        speech_text = sentences.HOW_TO_OR_BEGIN
        speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
        ask_text = speech_text
        attr["main_topic"] = "MeditationSession"
        attr["sub_topic"] = "HowOrBeginQuestion"
        attr["time_count"] = 0
        handler_input.attributes_manager.session_attributes = attr
        handler_input.response_builder.speak(speak_text).ask(speak_text).set_card(
            SimpleCard(sentences.SKILL_TITLE, sentences.MAIN_MENU))
        return handler_input.response_builder.response


class FiveMinIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("FiveMinIntent")(handler_input) 

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        speech_text = sentences.BEGIN_MEDITATION.format("five")
        speech_text += sentences.BREAK
        speech_text += sentences.NOTICE_SOUND
        speech_text += sentences.CONTINUE
        attr["main_topic"] = "MeditationSession"
        attr["sub_topic"] = "Meditating"
        attr["time_count"] += 5
        speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
        ask_text = sentences.SPEECH_RESPONSE.format(sentences.CONTINUE)
        handler_input.attributes_manager.session_attributes = attr
        # Handler Builder
        handler_input.response_builder.speak(speak_text).ask(ask_text).set_card(
            SimpleCard(sentences.SKILL_TITLE, sentences.BEGIN_MEDITATION))
        return handler_input.response_builder.response


class FifteenMinIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("FifteenMinIntent")(handler_input) 

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        speech_text = sentences.BEGIN_MEDITATION.format("fifteen")
        speech_text += sentences.BREAK
        speech_text += sentences.BREAK
        speech_text += sentences.BREAK
        speech_text += sentences.NOTICE_SOUND
        speech_text += sentences.CONTINUE
        attr["main_topic"] = "MeditationSession"
        attr["sub_topic"] = "Meditating"
        attr["time_count"] += 15
        speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
        ask_text = sentences.SPEECH_RESPONSE.format(sentences.CONTINUE)
        handler_input.attributes_manager.session_attributes = attr
        # Handler Builder
        handler_input.response_builder.speak(speak_text).ask(ask_text).set_card(
            SimpleCard(sentences.SKILL_TITLE, sentences.BEGIN_MEDITATION))
        return handler_input.response_builder.response


class ThirtyMinIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("ThirtyMinIntent")(handler_input) 

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        speech_text = sentences.BEGIN_MEDITATION.format("thirty")
        speech_text += sentences.BREAK
        speech_text += sentences.BREAK
        speech_text += sentences.BREAK
        speech_text += sentences.BREAK
        speech_text += sentences.BREAK
        speech_text += sentences.BREAK
        speech_text += sentences.NOTICE_SOUND
        speech_text += sentences.CONTINUE
        attr["main_topic"] = "MeditationSession"
        attr["sub_topic"] = "Meditating"
        attr["time_count"] += 30
        speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
        ask_text = sentences.SPEECH_RESPONSE.format(sentences.CONTINUE)
        handler_input.attributes_manager.session_attributes = attr
        # Handler Builder
        handler_input.response_builder.speak(speak_text).ask(ask_text).set_card(
            SimpleCard(sentences.SKILL_TITLE, sentences.BEGIN_MEDITATION))
        return handler_input.response_builder.response


class QuickIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("QuickMeditationIntent")(handler_input) 

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        speech_text = "OK. Begin a five minute meditation. Starting now. "
        speech_text += sentences.NOTICE_SOUND
        speech_text += sentences.BREAK
        speech_text += sentences.NOTICE_SOUND
        speech_text += sentences.CONTINUE
        speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
        attr["main_topic"] = "MeditationSession"
        attr["sub_topic"] = "Meditating"
        attr["time_count"] += 5
        handler_input.attributes_manager.session_attributes = attr
        handler_input.response_builder.speak(speak_text).set_card(
            SimpleCard(sentences.SKILL_TITLE, sentences.MAIN_MENU))
        return handler_input.response_builder.response


# Yes Handler
class YesIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.YesIntent")(handler_input) 

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        # Meditation Session : Before Meditation
        if attr["main_topic"] == "MeditationSession":
            if attr["sub_topic"] == "HowOrBeginQuestion":
                speech_text = sentences.HOW_TO_MEDITATE
                speech_text += sentences.NOTICE_SOUND
                speech_text += sentences.HOW_TO_MORE
                speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
                ask_text = sentences.SPEECH_RESPONSE.format(sentences.HOW_TO_MORE)
                main_topic = "MeditationSession"
                sub_topic = "HowtoMeditate"
            elif attr["sub_topic"] == "HowtoMeditate":
                speech_text = sentences.HOW_TO_MEDITATE_POSTURE
                speech_text += sentences.NOTICE_SOUND
                speech_text += sentences.HOW_TO_MORE
                speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
                ask_text = sentences.SPEECH_RESPONSE.format(sentences.HOW_TO_MORE)
                main_topic = "MeditationSession"
                sub_topic = "HowtoPosture"
            elif attr["sub_topic"] == "HowtoPosture":
                speech_text = sentences.HOW_TO_MEDITATE_FOCAL_POINT
                speech_text += sentences.NOTICE_SOUND
                speech_text += sentences.HOW_TO_MORE
                speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
                ask_text = sentences.SPEECH_RESPONSE.format(sentences.HOW_TO_MORE)
                main_topic = "MeditationSession"
                sub_topic = "HowtoFocalPoint"
            elif attr["sub_topic"] == "HowtoFocalPoint":
                speech_text = sentences.HOW_TO_MEDITATE_RECITATION
                speech_text += sentences.NOTICE_SOUND
                speech_text += "You are now ready to meditate. "
                speech_text += sentences.TIME_OPTION
                speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
                ask_text = sentences.SPEECH_RESPONSE.format(sentences.TIME_OPTION)
                main_topic = "MeditationSession"
                sub_topic = "SetTime"
            elif attr["sub_topic"] == "Meditating":
                more_time = attr["time_count"]
                if more_time == 5:
                    speech_text = "Got it. Continue for another {} minute. ".format(more_time)
                    speech_text += sentences.NOTICE_SOUND
                    speech_text += sentences.BREAK
                    attr["time_count"] += more_time

                if more_time == 15:
                    speech_text = "Got it. Continue for another {} minute. ".format(more_time)
                    speech_text += sentences.NOTICE_SOUND
                    speech_text += sentences.BREAK
                    speech_text += sentences.BREAK
                    speech_text += sentences.BREAK
                    attr["time_count"] += more_time
                if more_time == 30:
                    speech_text = "Got it. Continue for another {} minute. ".format(more_time)
                    speech_text += sentences.NOTICE_SOUND
                    speech_text += sentences.BREAK
                    speech_text += sentences.BREAK
                    speech_text += sentences.BREAK
                    speech_text += sentences.BREAK
                    speech_text += sentences.BREAK
                    speech_text += sentences.BREAK
                    attr["time_count"] += more_time       
                speech_text += sentences.CONGRATULATION.format(attr["time_count"])
                speech_text += sentences.SUMMARY_THOUGHT_QUESTION
                speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
                ask_text = sentences.SPEECH_RESPONSE.format(sentences.SUMMARY_THOUGHT_QUESTION)
                main_topic = "Summary"
                sub_topic = "Distracted"
                handler_input.response_builder.speak(speak_text).set_card(
                    SimpleCard(sentences.SKILL_TITLE, sentences.MAIN_MENU))
                return handler_input.response_builder.response
            else:
                speech_text = sentences.TIME_OPTION
                speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
                ask_text = sentences.SPEECH_RESPONSE.format(speech_text)
                main_topic = "MeditationSession"
                sub_topic = "SetTime"
            attr["main_topic"] = main_topic
            attr["sub_topic"] = sub_topic
            handler_input.attributes_manager.session_attributes = attr
            handler_input.response_builder.speak(speak_text).ask(ask_text).set_card(
                SimpleCard(sentences.SKILL_TITLE, sentences.MAIN_MENU))
            return handler_input.response_builder.response

        # Meditation Summary
        elif attr["main_topic"] == "Summary":
            if attr["sub_topic"] == "Distracted":
                speech_text = sentences.SUMMARY_THOUGHT_ANSWER
                speech_text += sentences.NOTICE_SOUND
                speech_text += sentences.SUMMARY_NOISE_QUESTION
                speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
                ask_text = sentences.SPEECH_RESPONSE.format(sentences.SUMMARY_NOISE_QUESTION)
                sub_topic = "Noise"
            elif attr["sub_topic"] == "Noise":
                speech_text = sentences.SUMMARY_NOISE_ANSWER
                speech_text += sentences.NOTICE_SOUND
                speech_text += sentences.SUMMARY_PAIN_QUESTION
                speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
                ask_text = sentences.SPEECH_RESPONSE.format(sentences.SUMMARY_PAIN_QUESTION)
                sub_topic = "Pain"
            elif attr["sub_topic"] == "Pain":
                speech_text = sentences.SUMMARY_PAIN_ANSWER
                speech_text += sentences.NOTICE_SOUND
                speech_text += sentences.SUMMARY_SLEEPY_QUESTION
                speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
                ask_text = sentences.SPEECH_RESPONSE.format(sentences.SUMMARY_SLEEPY_QUESTION)
                sub_topic = "Sleepy"
            elif attr["sub_topic"] == "Sleepy":
                speech_text = sentences.SUMMARY_SLEEPY_ANSWER
                speech_text += sentences.NOTICE_SOUND
                speech_text += sentences.SUMMARY_DOUBT_QUESTION
                speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
                ask_text = sentences.SPEECH_RESPONSE.format(sentences.SUMMARY_DOUBT_QUESTION)
                sub_topic = "Doubt"
            elif attr["sub_topic"] == "Doubt":
                speech_text = sentences.SUMMARY_DOUBT_ANSWER
                speech_text += sentences.NOTICE_SOUND
                speech_text += sentences.THANK_YOU
                speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
                handler_input.response_builder.speak(speak_text).set_card(
                    SimpleCard(sentences.SKILL_TITLE, sentences.MAIN_MENU)).set_should_end_session(True)
                return handler_input.response_builder.response
            else:
                speech_text = sentences.THANK_YOU
                speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
                handler_input.response_builder.speak(speak_text).ask(ask_text).set_card(
                    SimpleCard(sentences.SKILL_TITLE, sentences.MAIN_MENU)).set_should_end_session(True)

            attr["main_topic"] == "Summary"
            attr["sub_topic"] = sub_topic
            handler_input.attributes_manager.session_attributes = attr
            handler_input.response_builder.speak(speak_text).ask(ask_text).set_card(
                SimpleCard(sentences.SKILL_TITLE, sentences.MAIN_MENU)).set_should_end_session(False)
            return handler_input.response_builder.response
                     
        else:
            speech_text = sentences.MAIN_MENU
            topic = "MainMenu"
            attr["main_topic"] = topic
            handler_input.attributes_manager.session_attributes = attr
            handler_input.response_builder.speak(speak_text).ask(ask_text).set_card(
                SimpleCard(sentences.SKILL_TITLE, sentences.MAIN_MENU)).set_should_end_session(False)
            return handler_input.response_builder.response


# No Handler
class NoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.NoIntent")(handler_input) 

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        if attr["main_topic"] == "MeditationSession":
            if attr["sub_topic"] == "HowtoRecitation":
                speech_text = sentences.MAIN_MENU
                speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
                ask_text = sentences.SPEECH_RESPONSE.format(speech_text)
                main_topic = "MainMenu"
                sub_topic = ""
            elif attr["sub_topic"] in ("HowOrBeginQuestion", "HowtoMeditate", "HowtoPosture", "HowtoFocalPoint"):
                speech_text = sentences.TIME_OPTION
                speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
                ask_text = sentences.SPEECH_RESPONSE.format(speech_text)
                main_topic = "MeditationSession"
                sub_topic = "SetTime"
            elif attr["sub_topic"] == "Meditating":
                speech_text = sentences.CONGRATULATION.format(attr["time_count"])
                speech_text += sentences.SUMMARY_THOUGHT_QUESTION
                speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
                ask_text = sentences.SPEECH_RESPONSE.format(speech_text)
                main_topic = "Summary"
                sub_topic = "Distracted"
            else:
                speech_text = sentences.MAIN_MENU
                speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
                ask_text = sentences.SPEECH_RESPONSE.format(speech_text)
                main_topic = "MainMenu"
                sub_topic = ""

            attr["main_topic"] = main_topic
            attr["sub_topic"] = sub_topic
            handler_input.attributes_manager.session_attributes = attr
            handler_input.response_builder.speak(speak_text).ask(ask_text).set_card(
                SimpleCard(sentences.SKILL_TITLE, sentences.MAIN_MENU)).set_should_end_session(False)
            return handler_input.response_builder.response
        
        elif attr["main_topic"] == "Summary":
            if attr["sub_topic"] == "Distracted":
                speech_text = sentences.SUMMARY_NOISE_QUESTION
                speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
                ask_text = sentences.SPEECH_RESPONSE.format(speech_text)
                main_topic = "Summary"
                sub_topic = "Noise"
            elif attr["sub_topic"] == "Noise":
                speech_text = sentences.SUMMARY_PAIN_QUESTION
                speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
                ask_text = sentences.SPEECH_RESPONSE.format(speech_text)
                main_topic = "Summary"
                sub_topic = "Pain"
            elif attr["sub_topic"] == "Pain":
                speech_text = sentences.SUMMARY_SLEEPY_QUESTION
                speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
                ask_text = sentences.SPEECH_RESPONSE.format(speech_text)
                main_topic = "Summary"
                sub_topic = "Sleepy"
            elif attr["sub_topic"] == "Sleepy":
                speech_text = sentences.SUMMARY_DOUBT_QUESTION
                speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
                ask_text = sentences.SPEECH_RESPONSE.format(speech_text)
                main_topic = "Summary"
                sub_topic = "Doubt"
            elif attr["sub_topic"] == "Doubt":
                speech_text = sentences.THANK_YOU
                speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
                handler_input.response_builder.speak(speak_text).set_card(
                    SimpleCard(sentences.SKILL_TITLE, sentences.MAIN_MENU)).set_should_end_session(True)
                return handler_input.response_builder.response
            else:
                speech_text = sentences.THANK_YOU
                speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
                handler_input.response_builder.speak(speak_text).set_card(
                    SimpleCard(sentences.SKILL_TITLE, sentences.MAIN_MENU)).set_should_end_session(True)
                return handler_input.response_builder.response

            attr["main_topic"] = main_topic
            attr["sub_topic"] = sub_topic
            handler_input.attributes_manager.session_attributes = attr
            handler_input.response_builder.speak(speak_text).ask(ask_text).set_card(
                SimpleCard(sentences.SKILL_TITLE, sentences.MAIN_MENU)).set_should_end_session(False)
            return handler_input.response_builder.response

        else:
            speech_text = sentences.MAIN_MENU
            speak_text = sentences.SPEECH_RESPONSE.format(speech_text)
            ask_text = sentences.SPEECH_RESPONSE.format(speech_text)
            main_topic = "MainMenu"
            sub_topic = ""
            attr["main_topic"] = main_topic
            attr["sub_topic"] = sub_topic
            handler_input.attributes_manager.session_attributes = attr
            handler_input.response_builder.speak(speak_text).ask(ask_text).set_card(
                SimpleCard(sentences.SKILL_TITLE, sentences.MAIN_MENU)).set_should_end_session(False)
            return handler_input.response_builder.response


# Amazon Default Handler
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelAndStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(YesIntentHandler())
sb.add_request_handler(NoIntentHandler())

# Exception Handler
sb.add_exception_handler(AllExceptionHandler())

# Main Menu Intents Handler
sb.add_request_handler(MeditationSessionIntentHandler())
sb.add_request_handler(MeditationBenefitIntentHandler())

# Meditation Benefit Handler
sb.add_request_handler(BenefitPostureIntentHandler())
sb.add_request_handler(BenefitFocalPointIntentHandler())
sb.add_request_handler(BenefitRecitationIntentHandler())

# Meditation Session Handler 
sb.add_request_handler(QuickIntentHandler())
sb.add_request_handler(FiveMinIntentHandler())
sb.add_request_handler(FifteenMinIntentHandler())
sb.add_request_handler(ThirtyMinIntentHandler())

handler = sb.lambda_handler()
