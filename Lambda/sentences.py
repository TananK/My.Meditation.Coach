# Title : My Medication Coach Alexa Skill Speeches
# Author : Tanan Kesornbua
# Date : 01-06-2019

SPEECH_RESPONSE = "<prosody rate='slow'><voice name='Matthew'>{}</voice></prosody>"

SKILL_TITLE = ("My Medication Coach")

WELCOME_MESSAGE = ("<audio src='soundbank://soundlibrary/nature/amzn_sfx_ocean_wave_1x_01'/>"
                    "Welcome to My Meditation Coach! "
                    "Here, you can practice meditation with me, "
                    "Or learn the mechanism of meditation, ")

MAIN_MENU = ("Would you like to meditate, "
              "or learn today? ")

ERROR = ("Sorry, I didn't get it. Can you please say it again?")

MAIN_MENU_HELP = ("You can say meditate, "
                  "learn, or exit to get out of here. ")

MEDITATING_HELP = ("You can say stop to go to the summary, "
                  "cancel, to go back to main menu, "
                  "or exit, to get out of the skill. ")

SUMMARY_HELP = ("You can say stop or cancel, to go back to main menu, "
                  "or exit, to get out of the skill. ")

SETTIME_HELP = ("You can say five, fifteen, or thirty minute. ")

BENEFIT_HELP = ("You can say posture, focal point, or recitation. "
                  "If you want to go back to main menu, "
                  "You may say cancel. ")

MORE_BENEFIT = ("Would you like to learn more? ")

MEDITATION_BENEFIT = ("There are three mechanisms of meditation. "
                      "Posture, focal point, and Recitation. "
                      "What topic would you like to learn today. "
                      "You may say, cancel, to return to main menu. ")

BENEFIT_POSTURE = ("Having the right posture will help you concentrate on the meditation, "
                    "Taking a comfortable seat will alleviate your discomfort during the session. "
                    "Closing your eyes will reduce the amount of distraction from your surrounding, "
                    "Sitting up straight without leaning your back on the chair brings rigor and focus to your mind, "
                    "Putting your right palm on the left palm because when upward palms are used in meditation, "
                    "they position both the mind and the body in an open posture that enhances listening. "
                    "Breathing in and out deeply and slowly. "
                    "When the posture is done right, "
                    "we can feel the subtle differences in our body posture and breathing. "
                    "And the mind responds in kind. "
                    )

BENEFIT_FOCALPOINT = ("The Focal Point is like a home for the mind to stay focus. "
                      "Whenever you realize that your mind is wandering, "
                      "you will direct it to come back home to your Focal Point. "
                      "As you practice, "
                      "you will find your mind gets better at noticing when it is wandering, "
                      "and it will come back home by itself. "
                      "You will be more conscious of your thoughts, "
                      "and able to see a wider point of view that will give you more clarity throughout your day. "
                      "Sometimes focusing on a singular point is not enough. "
                      "Your mind will still wander. "
                      "The Focal Point gives your mind a location to be. "
                      "From here, "
                      "we have a second action that gives your mind something to do. ")

BENEFIT_RECITATION = ("Instead of letting the mind wander, "
                      "you can calm the busy mind by reciting a two syllable word. "
                      "We call this, buddho. "
                      "buddho works like a filter on your thoughts. "
                      "Thinking leads to various kinds of good and bad emotions, "
                      "so we want to minimize our thinking and mind-wandering. "
                      "Whenever you realize your mind is wandering, "
                      "just direct your mind to come back to recite Buddho, "
                      "or the two syllable word you chose. "
                      "Buddho means knowing, awakening, and joyfulness in Pali. "
                      "When you recite Buddho as you practice, "
                      "you will find your mind gets better at noticing when it is wandering, "
                      "and it will come back to Buddho by itself. "
                      "Buddho is used to train our minds to calm down, "
                      "by eliminating thoughts."
                      "When our mind is calm, "
                      "and we are not influenced by emotions, "
                      "we are more conscious and mindful. "
                      "The result is that we will maximize our productive ability. ")

HOW_TO_OR_BEGIN = ("Before we meditate, would you like to learn the three elements of meditation?")

HOW_TO_MEDITATE = ("There are three elements for an effective meditation session. "
                    "Your posture. "
                    "Focal point. "
                    "and recitation of a two syllable word. ")

HOW_TO_MEDITATE_POSTURE = ("Start with your posture, "
                            "Take a comfortable seat on a cushion, "
                            "a chair, "
                            "or even on the floor. "
                            "Close your eyes, "
                            "sit up straight without leaning your back on the chair, "
                            "and relax your body. "
                            "Put your right palm on the left palm. "
                            "Breathe in and out deeply,"
                            "and slowly. ")

HOW_TO_MEDITATE_FOCAL_POINT = ("In order to stop your mind from wandering, "
                                "focus on one point,"
                                "that might be your forehead, "
                                "the tip of your nose, "
                                "your chest, "
                                "or your navel. "
                                "This will be your Focal Point. "
                                "Focus your attention lightly on this point. "
                                "Breathe in and out deeply and slowly. ")

HOW_TO_MEDITATE_RECITATION = ("Another strategy to limit your thoughts is to "
                              "repeat any two syllable word as you meditate. "
                              "We use the word, "
                              "buddho. ")

HOW_TO_MORE = ("Would you like to know more? ")

TIME_OPTION = ("How long would you like to meditate today? "
                "You can choose, five, fifteen, or thirty minutes. ")

BEGIN_MEDITATION = ("For the next {} minutes, "
                    "I will stay with you. "
                    "you can stop the session at any point by saying stop or cancel. "
                    "<audio src='soundbank://soundlibrary/foley/amzn_sfx_glasses_clink_01'/>"
                    "<prosody volume='soft' rate='x-slow'>"
                    "Relax, inhale, and exhale slowly and deeply. "
                    "At the beginning, you will repeat buddho. "
                    "As you progress, you will find that your mind can repeat buddho on its own, "
                    "and you will still be concentrating on the focal point. "
                    "</prosody>"
                    "<audio src='soundbank://soundlibrary/foley/amzn_sfx_glasses_clink_01'/>"
                    "<prosody volume='x-soft' rate='x-slow'>"
                    "Begin your meditation. "
                    "</prosody>")
 
BREAK = ( "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> "
          "<break time='10s'/> ")

NOTICE_SOUND =  ("<audio src='soundbank://soundlibrary/foley/amzn_sfx_glasses_clink_01'/>")

CONTINUE = ("<prosody volume='x-soft' rate='x-slow'>"
            "Would you like to continue?"
            "</prosody>")

CONGRATULATION = ("Congratulation. You have meditated for {} minute today. "
                  "Let's recap your experience from the meditation today. ")
                    
SUMMARY_THOUGHT_QUESTION = ("Are you getting distracted by your thoughts? ")

SUMMARY_THOUGHT_ANSWER = ("If so, "
                          "continue to repeat the two syllable words faster, "
                          "to encourage your mind to focus on buddho. "
                          "If repeating the two syllable word faster does not work, "
                          "congratulate yourself when you notice your mind is getting lost in thought. "
                          "It takes only one momentary lapse of concentration to create a thought. "
                          "From this one thought, your mind will naturally create more stories. "
                          "The trick is to locate the original source of the thought. "
                          "Like a spider building a spider web, "
                          "follow the web to the source, "
                          "and find the spider. "
                          "Once you find the spider, "
                          "which is the source of the thought, "
                          "you will regain control of your distracted mind. ")

SUMMARY_NOISE_QUESTION = ("Are there any noise surrounding you that annoy you? " )

SUMMARY_NOISE_ANSWER = ("If the noise in your surrounding bugs you, "
                        "acceptance is the key to deal with the noise. "
                        "If you accept the surrounding noise no matter where you are, "
                        "then, you can meditate anywhere,"
                        "no matter how busy or loud the setting is. "
                        "Remind yourself that the purpose of meditation is mind control. "
                        "despite any external conditions that may be present.")

SUMMARY_SLEEPY_QUESTION = ("Are you feeling sleepy? " )

SUMMARY_SLEEPY_ANSWER = ( "It is natural. The nature of mind is to wander. "
                            "As you try to control your mind to stay on the Focal Point and to concentrate on Buddho, "
                            "the mind will probably get bored and sleepy. "
                            "Rouse your body by breathing deeply, "
                            "straightening your back, "
                            "raising your chin up, "
                            "and opening your eyes while repeating Buddho rapidly. ")

SUMMARY_PAIN_QUESTION = ("Do you feel numb, or sore on your back, legs, or shoulder? ")

SUMMARY_PAIN_ANSWER = ("When you feel numb or sore, "
                      "look at your mind and find where it is at. "
                      "Is it focusing on the pain? "
                      "It is not necessary to torture your body by not changing your posture for the duration of meditation. "
                      "But before you make any adjustment to your posture, "
                      "be aware that this is a good opportunity to learn how to deal with discomfort, "
                      "or other health problems. "
                      "Learning how to deal with discomfort not only help you during the meditation, "
                      "but it will also help you in daily life. "
                      "Bring your mind back from the feeling of pain to the Focal Point, "
                      "recite, Budd, while breathing in, "
                      "and tho, while breathing out. "
                      "Release the tension on your shoulders, "
                      "and relax your body. "
                      "When you attention is back on focal point and buddho"
                      "Your pain will disappear. " )

SUMMARY_DOUBT_QUESTION = ("Are you questioning or doubting your meditation technique? ")

SUMMARY_DOUBT_ANSWER = ("If you have questions like the following, "
                        "How do I know what I am doing this right? "
                        "How do I know if this thing really works? "
                        "Am I wasting my time? "
                        "How do I know if I am benefiting from meditating? "
                        "Some kinds of these questions or doubts are valid. "
                        "Discipline yourself to meditate consistently. "
                        "Precise investigation without bias counteracts doubt and hesitation. ")

THANK_YOU = ("Thank you for meditating with me today. "
              "The more you meditate, "
              "the better you can handle the feelings such as, "
              "tireness, soreness, or distraction in your daily life. "
              "Whatever the result of the meditation is, "
              "be proud that you have strengthened your mind today. "
              "If you like this skill, please rate me on Amazon skills store. "
              "You can also follow me on instragram at, "
              "<emphasis level='strong'>my meditation coach</emphasis> "
              "for daily meditation quote. "
              "I look forward to meditate with you again" )
