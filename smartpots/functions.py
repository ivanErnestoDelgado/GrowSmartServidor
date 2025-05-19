from smartpots.models import *

alertTypes_from_smartpots_status={
            SmartPot.GOOD: Alert.Type.OUT_OF_DANGER,
            SmartPot.WARNING: Alert.Type.MODERATE_DANGER,
            SmartPot.DANGER:Alert.Type.HIGH_DANGER
        }

status_cases={
     0:SmartPot.GOOD,
     1:SmartPot.WARNING,
     2:SmartPot.DANGER,
     3:SmartPot.DANGER
}

#Cuenta cuantos limites en parametros de la planta fueron sobrepasados segun los datos de los sensores
def find_breaked_limits(sensor_data, plant):
        out_of_limits_parameters=[]
        light_status=plant.evaluate_light_data(sensor_data.light_level)
        temperature_status=plant.evaluate_temperature_data(sensor_data.temperature)
        humidity_status=plant.evaluate_humidity_data(sensor_data.floor_humidity)

        if(light_status !=Plant.dataStatusFromSensor.NORMAL):
             string="Luz "+complete_string(light_status)
             out_of_limits_parameters.append(string)
        
        if(temperature_status !=Plant.dataStatusFromSensor.NORMAL):
             string="Temperatura "+complete_string(temperature_status)
             out_of_limits_parameters.append(string)
        
        if(humidity_status !=Plant.dataStatusFromSensor.NORMAL):
             string="Humedad "+complete_string(humidity_status)
             out_of_limits_parameters.append(string)
        
        return out_of_limits_parameters

def complete_string(sensor_status):
     match sensor_status:
        case Plant.dataStatusFromSensor.LOWER:
            return "baja"
        case Plant.dataStatusFromSensor.HIGHER:
            return "alta"
     
def evaluate_plant_status(breaked_limits_count):
        return status_cases.get(breaked_limits_count)

def choose_alert_type_from_status_choices(status):
        return alertTypes_from_smartpots_status.get(status)

def obtain_alert_message(alert_type,out_of_limits_sensors):
    match alert_type:
         case Alert.Type.OUT_OF_DANGER:
              return "Modulo fuera de peligro"
         case Alert.Type.WATHERING_EVENT:
              return "Modulo regado"
         case alert_type if is_on_danger(alert_type):
              return "Los siguientes parametros estan fuera de limite: "+", ".join(out_of_limits_sensors)

def is_on_danger(alert_type):
    return is_moderate_danger(alert_type) or is_high_danger(alert_type)

def is_high_danger(alert_type):
    return alert_type==Alert.Type.HIGH_DANGER

def is_moderate_danger(alert_type):
    return alert_type==Alert.Type.MODERATE_DANGER