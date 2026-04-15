import uuid

def generate_random_message():
    return f"echo_{uuid.uuid4().hex[:8]}"