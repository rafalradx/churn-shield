from openai import OpenAI
import openai
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv('API'))

def generate_description(input):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """You are a helpful assistant. You receive information about a customer in the form of: 
                                                {
                                                "is_tv_subscriber": [data.is_tv_subscriber],
                                                "is_movie_package_subscriber": [data.is_movie_package_subscriber],
                                                "subscription_age": [data.subscription_age],
                                                "bill_avg": [data.bill_avg],
                                                "remaining_contract": [data.remaining_contract],
                                                "service_failure_count": [data.service_failure_count],
                                                "download_avg": [data.download_avg],
                                                "upload_avg": [data.upload_avg],
                                                "download_over_limit": [data.download_over_limit]
                                                }
                                                and model predictions that suggest the likelihood (as a percentage) that the customer will cancel the service, focus only on the Neural Network model prediction, take a look at service failures if it is more than 4 you should offer discount for customer for this failures as compensation.
                                                If the percentage is high, suggest to the user that they offer the customer a discount, promotion, or some cheaper package, etc.. if percentage is less than 35 percentage the recommendation is not to contact the customer yet"""},
                {"role": "user", "content": f"{input}"}
            ]
        )
        reply = response.choices[0].message.content
        return reply

    except:
        print(f"")





def generate_recommendation(input_data, predictions):
    input_text = f"Input: {input_data}, Predictions: {predictions}"
    return generate_description(input_text)
