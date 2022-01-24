alert_failure_count = 0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    if (celcius <= 37): 
        return 200 # Return 200 for ok
    else: 
        return 500 # Return 500 for not-ok
    

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 0


alert_in_celcius(400.5)
assert(alert_failure_count == 0)
alert_in_celcius(303.6)
assert(alert_failure_count != 0)
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
