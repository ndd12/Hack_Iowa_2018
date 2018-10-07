from sklearn.externals import joblib
from preprocessLyrics import process

classifier = joblib.load('pipeline.joblib')

def predict(lyrics):
    return classifier.predict([lyrics])

test = "I hurt myself today To see if I still feel I focus on the pain The only thing that's real The needle tears a hole The old familiar sting Try to kill it all away But I remember everything What have I become My sweetest friend Everyone I know Goes away in the end And you could have it all My empire of dirt I will let you down I will make you hurt I wear this crown of shit Upon my liars chair Full of broken thoughts I cannot repair Beneath the stains of time The feelings disappear You are someone else I am still right here What have I become My sweetest friend Everyone I know Goes away in the end And you could have it all My empire of dirt I will let you down I will make you hurt If I could start again A million miles away I will keep myself I would find a way"
test = process([test])
print(predict(test))

