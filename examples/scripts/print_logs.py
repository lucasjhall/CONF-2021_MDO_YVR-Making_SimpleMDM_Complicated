import SimpleMDMpy

simplemdm_api_key = '$YOUR_API_KEY'
filterID = '$LAST_LOG_UUID'

Logs = SimpleMDMpy.Logs(simplemdm_api_key)
logObj = Logs.get_logs(id_override=filterID)

for log in logObj['data']:
    print(log)