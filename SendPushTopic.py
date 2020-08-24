import FCMManager as fcm

topic = "topic_demo"
tokens = ["cC35WhWG-uY:APA91bEhMeJvuhGfCtVmG2falFYGA6G9ARxs3Rho9OdBaznv7d9B6JJ8eYF1-UYTO_r1QA9RvxXF4aa3wvu-X5gpc1epk5mqplLOZqK5sx8qboTSZRe_ucBDPymo8ksyo1tRmFtberne"]
# fcm.subscribe(tokens, topic)
# fcm.unsubscribe(tokens, topic)
fcm.sendPushTopic("TEST MOBILE", "PSG sufrió su primera baja", "https://e.rpp-noticias.io/medium/2020/08/24/portada_580258.jpg", topic)