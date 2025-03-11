from firebase_admin.messaging import Message, Notification,MulticastMessage,send_multicast,send

def send_push_notification(title,body,devices):
    number_of_devices=len(devices)
    tokens = [device.registration_id for device in devices if device.registration_id]

    if number_of_devices==1:
        maked_message=make_unicast_message(title=title,body=body,token=tokens[0])
        return send(message=maked_message)
    else:
        maked_message=make_multicast_message(title=title,body=body,tokens=tokens)
        return send_multicast(maked_message)
    
    

def make_multicast_message(title,body,tokens):
    return MulticastMessage(
        notification=Notification(
            title=title,
            body=body
        ),
        tokens=tokens
    )

def make_unicast_message(title,body,token):
    return Message(
        notification=Notification(
            title=title,
            body=body
        ),
        token=token
    )