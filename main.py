from core.brain import Brain
from core.commands import execute
from core.voice import Voice
from core.parser import CommandParser

brain = Brain()
voice = Voice()
parser = CommandParser()

print("=" * 40)
print("      ECHO AI ASSISTANT")
print("=" * 40)

while True:

    input("\nPress ENTER to talk...")

    user = voice.listen()

    if not user:
        continue

    if user.lower() in ["exit", "quit"]:
        voice.speak("Goodbye.")
        break

    parsed = parser.parse(user)

    print(f"[PARSER] {parsed}")

    result = execute(parsed)

    if result:
       voice.speak(result)
       continue

    reply = brain.ask(user)
    voice.speak(reply)