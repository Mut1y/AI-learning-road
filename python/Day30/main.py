from ai_service import ask_ai



while True:


    question=input("你:")


    if question=="退出":

        break


    answer=ask_ai(question)


    print("AI:",answer)