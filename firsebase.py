from firebase_admin import messaging

message = messaging.Message(
    notification=messaging.Notification('推送测试', 'Test'),
    data={
        'score': '850',
        'time': '2:45',
    },
    topic='all'
)


# 推送方法
def cloud_push():
    response = messaging.send(message)
    print('Successfully sent message:', response)
    return ''
