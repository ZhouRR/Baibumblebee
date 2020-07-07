import os

from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, pipeline, TFAutoModelForQuestionAnswering
import tensorflow as tf

app = FastAPI()
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased-finetuned-mrpc")
model = TFAutoModelForQuestionAnswering.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")

nlp = pipeline("question-answering")


class Message(BaseModel):
    message_id: str = None
    subject: str
    body: str
    structure: str = None


@app.get("/messages")
async def get_messages():
    text = r"""🤗 Transformers (formerly known as pytorch-transformers and pytorch-pretrained-bert)
     provides general-purpose architectures (BERT, GPT-2, RoBERTa, XLM, DistilBert, XLNet…) for Natural Language
      Understanding (NLU) and Natural Language Generation (NLG) with over 32+ pretrained models in 100+ languages
       and deep interoperability between TensorFlow 2.0 and PyTorch."""

    questions = ["How many pretrained models are available in 🤗 Transformers?",
                 "What does 🤗 Transformers provide?",
                 "🤗 Transformers provides interoperability between which frameworks?", ]

    results = []
    for question in questions:
        inputs = tokenizer(question, text, add_special_tokens=True, return_tensors="tf")
        input_ids = inputs["input_ids"].numpy()[0]

        tokenizer.convert_ids_to_tokens(input_ids)

        answer_start_scores, answer_end_scores = model(inputs)

        answer_start = tf.argmax(
            answer_start_scores, axis = 1
        ).numpy()[0]  # Get the most likely beginning of answer with the argmax of the score

        answer_end = (tf.argmax(answer_end_scores, axis=1) + 1).numpy()[0]  # Get the most likely end of answer with the argmax of the score
        answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))

        results += [f"Question: {question}", ]
        results += [f"Answer: {answer}", ]
    return results


@app.post("/messages")
async def post_message(message: Message):
    return "push message finished"


def execute_from_command_line(cmd=None):
    os.system(cmd)


def main():
    execute_from_command_line('uvicorn manage:app --reload')
    pass


if __name__ == '__main__':
    main()
