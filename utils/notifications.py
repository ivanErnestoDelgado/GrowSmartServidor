from pyfcm import FCMNotification

push_service = FCMNotification(api_key="BOuxi-7CfAe91Ww9RMPHMOjkUXHdhUZp_tH8XMowdFbfJNrjhHuQ2D7f3eOwxsBgabFbiQKrkdxuglVltX0B8Kw")

def enviar_notificacion(fcm_token, titulo, mensaje):
    result = push_service.notify_single_device(
        registration_id=fcm_token,
        message_title=titulo,
        message_body=mensaje,
    )
    return result
