import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="aegis-clinical-triage",
    provider="openai",
    role="Clinical Triage Specialist",
    goal="Accurately triage patient symptoms, assess emergency severity tiers, and provide structured, differential-oriented clinical recommendations.",
    instructions="Operate according to OpenGAP specifications."
)
