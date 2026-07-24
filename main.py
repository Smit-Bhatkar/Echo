from core.brain import Brain
from core.commands import execute
from core.voice import Voice
from core.parser import CommandParser
from core.session import session

brain = Brain()
voice = Voice()
parser = CommandParser()

print("=" * 40)
print("      ECHO AI ASSISTANT")
print("=" * 40)

while True:

    try:
        print("\n🎤 Listening...")

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

    except KeyboardInterrupt:
        print("\nShutting down Echo...")
        voice.speak("Goodbye.")
        break

    except Exception as e:
        print(f"\n[ERROR] {type(e).__name__}: {e}")

        try:
            voice.speak("Sorry, something went wrong.")
        except Exception:
            pass

        continue