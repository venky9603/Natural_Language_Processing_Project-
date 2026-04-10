from nltk.chat.util import Chat, reflections

pairs = [
    [r"(.*)my name is (.*)", ["Hello %2, How are you today ?"]],
    [r"(.*)help(.*)", ["I can help you"]],
    [r"(.*) your name ?", ["My name is robot"]],
    [r"how are you (.*) ?", ["I'm doing very well", "I am great!"]],
    [r"(hi|hey|hello)(.*)", ["Hello", "Hey there"]],
    [r"(.*)", ["Our customer service will reach you"]]
]

# 🔥 Create chatbot ONLY ONCE (global object)
chat = Chat(pairs, reflections)

def get_response(user_input):
    return chat.respond(user_input)