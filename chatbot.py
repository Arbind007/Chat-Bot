# 0 Import libraries
import random
from textblob import TextBlob

# 1. Name and nickname conversation
print('Hello, may I know your name please?')
name = input()
print('Do you have nickname?')
ans = input()
if 'yes' in ans.lower():
    nickname = input('what is your nickname: ')
    print('Good to meet you ' + nickname)
elif 'y' in ans.lower():
    nickname = input('what is your nickname: ')
    print('Good to meet you ' + nickname)
elif 'ya' in ans.lower():
    nickname = input('what is your nickname: ')
    print('Good to meet you ' + nickname)
else:
    nickname = name
    print('Good to meet you ' + nickname )

# 2. Greeting selection
greetings = [
    'How are you today ' + nickname + '?',
    'Howdy ' + nickname + ' how are you feeling?',
    "What's up " + nickname + '?',
    'Greetings ' + nickname + ', are you well?',
    'How are things going ' + nickname + '?'
]
print(random.choice(greetings))
ans = input()
blob = TextBlob(ans)

if blob.polarity > 0:
    print('Glad you are doing well')
else:
    print('Sorry to hear that')

# 3. Several random opinions on topic
topics = 'farm solutions'


questions = [
    'What is your take on ',
    'What do you think about ',
    'How do you feel about ',
    'What do you reckon about ',
    'I would like your opinion on '
]
for i in range(0, random.randint(1, 2)):
    question = random.choice(questions)
    topic = topics
    print(question + topic + '?')
    ans = input()
    blob = TextBlob(ans)

    if blob.polarity > 0.5:
        print('OMG we are happy to know that you really love ' + topic)
    elif blob.polarity > 0.1:
        print('Well, you clearly like ' + topic)
    elif blob.polarity < -0.5:
        print('So, you totally hate ' + topic)
    elif blob.polarity < -0.5:
        print("So you don't like " + topic)
    else:
        print('That is a very neutral view on ' + topic)

# 4. Question
print('1.Do you want to review / or submit a feedback')
print('2.Do you want to file a complain')
print('3.Do you want to exit')
answer = int(input())
if answer == 1:
    print('Here is the link for feedback' + '' + nickname)
elif answer == 2:
    print('One of our executive will be in touch with you, please click the link'+''+ nickname)
elif answer == 3:
    print()

# 5. Random goodbye
goodbyes = [
    'Good talking to you ' + nickname + ' Have a nice day ahead!',
    'OK I am glad I could help you today ' + nickname,
    'Bye bye ' + nickname + 'I am out' ,
    'Yaaawn . . . I gotta go now',
    'Catch ya later, ' + nickname
]
print(random.choice(goodbyes))