import os
import gradio as gr
import torch
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

MODEL = 'gyupro/Koalpaca-Translation-KR2EN'



model = AutoModelForCausalLM.from_pretrained(
    MODEL,
    torch_dtype=torch.float16,
    device_map='cuda:0'
  
)

model.eval()

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=AutoTokenizer.from_pretrained(MODEL),
)


def answer(state, state_chatbot, text):


    ans = pipe(
        f"### source: {text}\n\n### target:",
        do_sample=False,
        max_new_tokens=2048,
        temperature=0.7,
        top_p=0.9,
        return_full_text=False,
        eos_token_id=2,
    )

    msg = ans[0]["generated_text"]

    if "###" in msg:
        msg = msg.split("###")[0]

    new_state = [{"role": "이전 질문", "content": text}, {"role": "이전 답변", "content": msg}]

    state = state + new_state
    state_chatbot = state_chatbot + [(text, msg)]

    print(state)
    print(state_chatbot)

    return state, state_chatbot, state_chatbot


with gr.Blocks(css="#chatbot .overflow-y-auto{height:750px}") as demo:
    state = gr.State(
        [
            {
                "role": "맥락",
                "content": "영어번역 모델.",
            },
            {"role": "명령어", "content": "친절한 AI 챗봇인 ChatKoAlpaca 로서 답변을 합니다."},
            {
                "role": "명령어",
                "content": "인사에는 짧고 간단한 친절한 인사로 답하고, 아래 대화에 간단하고 짧게 답해주세요.",
            },
        ]
    )
    state_chatbot = gr.State([])

    with gr.Row():
        gr.HTML(
            """<div style="text-align: center; max-width: 500px; margin: 0 auto;">
            <div>
                <h1>Koalpaca-Translation-KR2EN</h1>
            </div>
            <div>
                Enter korean sentence to be translated
            </div>
        </div>"""
        )

    with gr.Row():
        chatbot = gr.Chatbot(elem_id="chatbot")

    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder="Send a message...").style(
            container=False
        )

    txt.submit(answer, [state, state_chatbot, txt], [state, state_chatbot, chatbot])
    txt.submit(lambda: "", None, txt)

demo.launch(debug=True, server_name="0.0.0.0")