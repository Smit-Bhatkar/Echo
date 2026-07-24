from core.router import SkillRouter

router = SkillRouter()


def execute(parsed):

    print(f"[DEBUG] Parsed: {parsed}")

    return router.execute(parsed)