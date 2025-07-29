from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.groq import Groq
from agno.playground import Playground, serve_playground_app

from dotenv import load_dotenv

load_dotenv()

def celsius_to_fh(temperature_celsius: float):
    """
    Converte uma temperatura de graus Celsius para Fahrenheit.

    Args:
        temperature_celsius (float): Temperatura em graus Celsius.

    Returns:
        float: Temperatura convertida em graus Fahrenheit.
    """
    return (temperature_celsius * 9/5) + 32


agent = Agent(
    name="Agente do tempo",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        TavilyTools(),
        celsius_to_fh,
    ],
    debug_mode=True
)

app = Playground(agents=[
    agent
]).get_app()

if __name__ == "__main__":
    serve_playground_app("13_own_tools:app", reload=True)

#agent.print_response("Use suas ferramentas para pesquisar temperatura de hoje em João Pessoa em Fahrenheit")