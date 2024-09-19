from openai import OpenAI, OpenAIError
from src.conf.config import settings

try:
    client = OpenAI(api_key=settings.openai_api_key)
except Exception as e:
    print(f"GPT recommendation system initialization failed: {e}")


async def generate_suggestion(input_data: str, predictions: str):
    gpt_input = f"Input: {input_data}, Predictions: {predictions}"
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": """You are a helpful assistant. You receive information about a customer in the form of: 
                                                Input: 
                                                is_tv_subscriber=0/1 (true/false)
                                                is_movie_package_subscriber=0/1 (true/false)
                                                subscription_age=value [Years]
                                                bill_avg=value [$]
                                                remaining_contract=value [Years]
                                                service_failure_count=value
                                                download_avg=value [kbps]
                                                upload_avg=value [kbps]
                                                download_over_limit=value,
                                                Predictions:
                                                {
                                                    'model1': value,
                                                    'model2': value,
                                                    ...
                                                } - convert value to percentage
                                                Take that data and suggest what I should do. Models values is percentage of chance to customer cancel service if percentages are high suggest to offer some promotion to customer or some more favorable contract.
                                                Don't mention about variables use human words: is_tv_subscriber -> costumer is not subscribed to TV.
                                                Return data in html response.
                                                Split for 3 section - Customer Overview, Risk values, Reccomendation (for headers use h4)""",
                },
                {"role": "user", "content": f"{gpt_input}"},
            ],
        )
        reply = response.choices[0].message.content
        return reply[7:-3]

    except OpenAIError as e:
        # Obsługa błędów specyficznych dla OpenAI
        return f"OpenAI error: {e}"
    except Exception as e:
        # Obsługa innych błędów
        if not settings.openai_api_key:
            return "To use the recommendation system, you have to configure your API KEY in the .env file."
        else:
            return f"Something went wrong while generating recommendations: {e}"
