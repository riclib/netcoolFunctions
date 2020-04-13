import logging
# from zeep import Client

import azure.functions as func
import json
import requests



def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
#    wsdl = ('file:///Users/riclib/solidmon/netcoolFunctions/sendToNetCool/ImpactWebServiceListenerDLService.wsdl')
#    client= Client(wsdl = wsdl)
    name = req.params.get('name')

# Intercept.rest connection to debug inputs :)
    response = requests.post(
        'https://101070a4d7.to.intercept.rest/', data=json.dumps(req.get_json()),
        headers={'Content-Type': 'application/json'}
    )

    webhook_url = 'https://hooks.slack.com/services/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'


    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
            alert_rule = req_body['data']['essentials']['alertRule']
            alert_metricValue = req_body['data']['alertContext']['condition']['allOf'][0]['metricValue']
            alert_resourceId = req_body['data']['alertContext']['condition']['allOf'][0]['dimensions'][0]['value']
            # req_body.body.data.alertContext.get('AffectedConfigurationItems')
    slack_string = "Alert " + alert_rule + " id " + alert_resourceId + " Value " + str(alert_metricValue)
    slack_data = {'text': slack_string}
    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        return func.HttpResponse("Couldn't call!")
    else: 
        return func.HttpResponse("Succesfully processed")
    
