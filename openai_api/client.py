import os
from openai import OpenAI


def get_client():
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    return client


def get_car_ai_bio(model, brand, year):
    acao = '''
        Me mostre uma descrição de venda para o carro {} {} {} em apenas 250
        caracteres. Fale coisas específicas desse modelo de carro.
    '''.format(brand, model, year)
    instrucao = '''
        Você é um grande admirador de carros e presta consultoria.
    '''

    client = get_client()
    response = client.responses.create(
        model="gpt-5.2",
        instructions=instrucao,
        input=acao,
        max_output_tokens=1000,
    )
    return response.output_text
