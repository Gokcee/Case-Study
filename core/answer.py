def generate_answer(question, context):
    if not context.strip():
        return "Bilmiyorum, belgede bu bilgi yok."

    return f"""
Soru: {question}

Cevap (belgeye göre):
{context[:500]}
"""