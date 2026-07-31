import json
import os


STATE_FILE = "agent_state.json"



def save_state(state):


    data = {

        "status":state.status,

        "question":state.question,

        "tool":state.tool,

        "arguments":state.arguments,

        "observation":state.observation

    }


    with open(
        STATE_FILE,
        "w",
        encoding="utf-8"
    ) as f:


        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )





def load_state():


    if not os.path.exists(STATE_FILE):

        return None


    with open(
        STATE_FILE,
        "r",
        encoding="utf-8"
    ) as f:


        return json.load(f)