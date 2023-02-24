import pyttsx3 as tts


def speaker(names):
    engine = tts.init()
    for i in names:
        engine.say(f"Shoutout to {i}!")
        engine.runAndWait()


if __name__ == "__main__":

    # with open('Shoutouts/names.txt', 'w+') as f:
    #     names = list(input('\n Enter the names : ').split(','))
    #     for name in names:
    #         f.write(name+'\n')
    #     speaker(names)

    with open('Shoutouts/names.txt') as f:
        names = f.readlines()
        names = list(map(lambda x: x[:-1], names))
        print(names)
        speaker(names)
