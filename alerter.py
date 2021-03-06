alert_failure_count = 0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    if (celcius <= float(200)): 
        return 200 # Return 200 for ok
    else: 
        return 500 # Return 500 for not-ok
    
def GetFarenheitFromCelcius(farenheit:float)->float:
    return (farenheit - 32) * 5 / 9

def alert_in_celcius(celcius, network_alert_stub):
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 1
    else:
        alert_failure_count = alert_failure_count

def ValidateCode():
    try:
        assert(alert_failure_count == 1)
    except AssertionError:
        print("AssertionError occured. Please revisit")

alert_in_celcius(GetFarenheitFromCelcius(400.5), network_alert_stub)
alert_in_celcius(GetFarenheitFromCelcius(303.6), network_alert_stub)
assert(alert_failure_count == 1)
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
