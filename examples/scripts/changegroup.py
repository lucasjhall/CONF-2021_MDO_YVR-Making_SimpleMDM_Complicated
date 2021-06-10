import SimpleMDMpy

simplemdm_api_key = '$YOUR_API_KEY'
device_id = '$YOUR_DEVICE_ID'
attribute_value = '10'

def change_device_attribute(attribute_value, device_id):
    Attributes = SimpleMDMpy.CustomAttributes(simplemdm_api_key)
    response = Attributes.update_custom_attribute(str(device_id), str(attribute_value))

    return response

resp = change_device_attribute(attribute_value, device_id)
print(resp)