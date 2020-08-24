import os
import firebase_admin
import datetime
import time
from firebase_admin import credentials, messaging

filedir = os.path.dirname(os.path.realpath('__file__'))
filekey = os.path.join(filedir, 'serviceAccountKey.json')

cred = credentials.Certificate(filekey)
firebase_admin.initialize_app(cred)


def subscribe(tokens, topic):
    response = messaging.subscribe_to_topic(tokens, topic)
    print(response.success_count, 'tokens were subscribed successfully')


def unsubscribe(tokens, topic):
    response = messaging.unsubscribe_from_topic(tokens, topic)
    print(response.success_count, 'tokens were unsubscribed successfully')


def sendPush(title, msg, image, registration_token, dataObject=None):
    date = datetime.datetime.fromtimestamp(int(time.time()))
    # See documentation on defining a message payload.
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=msg,
            image=image
        ),
        data={
            "date": date.strftime('%Y-%m-%d %H:%M:%S'),
            "station_id": "2",
            "title": title,
            "body": msg,
            "image": image,
            "icon": "",
            "click_action": "https://capital.pe/"
        },
        tokens=registration_token,
        fcm_options=messaging.FCMOptions(analytics_label="tokens_label")
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send_multicast(message)
    # Response is a message ID string.
    print('{0} messages were sent successfully'.format(response.success_count))


def sendPushTopic(title, msg, image, topic):
    date = datetime.datetime.fromtimestamp(int(time.time()))
    # See documentation on defining a message payload.
    message = messaging.Message(
        data={
            "date": date.strftime('%Y-%m-%d %H:%M:%S'),
            "station_id": "2",
            "title": title,
            "body": msg,
            "image": image,
            "icon": "",
            "click_action": "https://capital.pe/"
        },
        topic=topic,
        fcm_options=messaging.FCMOptions(analytics_label="topic_label")
    )
    response = messaging.send(message)
    print('Successfully sent message to topic:', response)