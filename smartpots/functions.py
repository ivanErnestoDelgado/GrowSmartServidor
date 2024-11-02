from smartpots.models import SmartPot

#Cuenta cuantos limites en parametros de la planta fueron sobrepasados segun los datos de los sensores
def count_breaked_limits(sensor_data, plant):
        out_of_limits_count=0
        #verifica la tamperatura
        if temperature_is_out_of_limits(sensor_data, plant):
            out_of_limits_count += 1
        
        # Verifica la humedad
        if humidity_is_out_of_limits(sensor_data, plant):
            out_of_limits_count += 1
        
        # Verifica el nivel de luz
        if light_level_is_out_of_limits(sensor_data, plant):
            out_of_limits_count += 1

        return out_of_limits_count

def light_level_is_out_of_limits(sensor_data, plant):
    return sensor_data.light_level < plant.minimun_ligth_level or sensor_data.light_level > plant.maximun_ligth_level

def humidity_is_out_of_limits(sensor_data, plant):
    return sensor_data.floor_humidity < plant.minumun_humidity or sensor_data.floor_humidity > plant.maximun_humidity

def temperature_is_out_of_limits(sensor_data, plant):
    return sensor_data.temperature < plant.minimun_temperature or sensor_data.temperature > plant.maximun_temperature

def evaluate_plant_status(breaked_limits_count):
        return status_cases.get(breaked_limits_count)

status_cases={
     0:SmartPot.GOOD,
     1:SmartPot.WARNING,
     2:SmartPot.DANGER,
     3:SmartPot.DANGER
}