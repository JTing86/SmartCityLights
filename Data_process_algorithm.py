total_lights = 60
current_data = [0 for i in range(total_lights)]
num_sensor = 12
overlap=3

def generate_led_on_pos(triggered_sensors):
    pos_to_turn_light_on = []
    ratio = int(total_lights / num_sensor) #5


    for k in triggered_sensors:
        lowest_index = (k * ratio - overlap) if (k * ratio - overlap) > 0 else 0
        higher_index = k * ratio + ratio + overlap + 1
        pos_to_turn_light_on.extend([i for i in range(lowest_index, higher_index)])
    pos_to_turn_light_on.sort()
    pos_to_turn_light_on = set(pos_to_turn_light_on)
    return pos_to_turn_light_on


def get_new_state(current_sensors_data, current_data):
    #sensor_num = len(current_sensors_data)

    #a list of position of lights need to be turned on
    sensors_triggered_pos = [i+1 for i in current_sensors_data if current_sensors_data[i] == '1']
    led_on_pos = generate_led_on_pos(sensors_triggered_pos)
    for i in led_on_pos:
        try:
            current_data[i] += 1
        except:
            return current_data
    return current_data


current_state = get_new_state(msg["payload"], current_state)
send_state = ""
for i in current_state:
    send_state += str(i)

msg["payload"] = send_state
return msg
