from nltk.chat.util import Chat, reflections

pairs = [
    [r"(.*)my name is (.*)", ["Hello %2, How are you today ?"]],
    [r"(.*)help(.*)", ["I can help you"]],
    [r"(.*) your name ?", ["My name is robot, I'm a chatbot."]],
    [r"how are you (.*) ?", ["I'm doing very well", "I am great!"]],
    [r"sorry (.*)", ["Its alright", "Its OK, never mind that"]],
    [r"i'm (.*) (good|well|okay|ok)", ["Nice to hear that", "Alright, great!"]],
    [r"(hi|hey|hello|hola)(.*)", ["Hello", "Hey there"]],
    [r"(.*)created(.*)", ["Prakash created me using Python"]],
    [r"(.*)(location|city)", ["Hyderabad, India"]],
    [r"(.*)", ["Our customer service will reach you"]]
]

chat = Chat(pairs, reflections)