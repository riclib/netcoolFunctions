# Request format, captured with proxy
``` json
{
  "schemaId": "AzureMonitorMetricAlert",
  "data": {
    "version": "2.0",
    "properties": null,
    "status": "Activated",
    "context": {
      "timestamp": "2020-04-12T00:35:33.4494204Z",
      "id": "/subscriptions/a075e71f-4749-4d79-aa41-c62c7091b496/resourceGroups/libBlog/providers/microsoft.insights/metricAlerts/Too%20many%20succesful%20views",
      "name": "Too many succesful views",
      "description": "",
      "conditionType": "SingleResourceMultipleMetricCriteria",
      "severity": "3",
      "condition": {
        "windowSize": "PT5M",
        "allOf": [
          {
            "metricName": "Http2xx",
            "metricNamespace": "Microsoft.Web/sites",
            "operator": "GreaterThan",
            "threshold": "5",
            "timeAggregation": "Total",
            "dimensions": [
              {
                "name": "ResourceId",
                "value": "libblog.azurewebsites.net"
              }
            ],
            "metricValue": 10,
            "webTestName": null
          }
        ]
      },
      "subscriptionId": "a075e71f-4749-4d79-aa41-c62c7091b496",
      "resourceGroupName": "libBlog",
      "resourceName": "libBlog",
      "resourceType": "Microsoft.Web/sites",
      "resourceId": "/subscriptions/a075e71f-4749-4d79-aa41-c62c7091b496/resourceGroups/libBlog/providers/Microsoft.Web/sites/libBlog",
      "portalLink": "https://portal.azure.com/#resource/subscriptions/a075e71f-4749-4d79-aa41-c62c7091b496/resourceGroups/libBlog/providers/Microsoft.Web/sites/libBlog"
    }
  }
}
```

# Common format
``` json
{
  "schemaId": "azureMonitorCommonAlertSchema",
  "data": {
    "essentials": {
      "alertId": "/subscriptions/a075e71f-4749-4d79-aa41-c62c7091b496/providers/Microsoft.AlertsManagement/alerts/fa848f4f-8a27-4924-bd39-806aa9f10778",
      "alertRule": "Too many succesful views",
      "severity": "Sev3",
      "signalType": "Metric",
      "monitorCondition": "Resolved",
      "monitoringService": "Platform",
      "alertTargetIDs": [
        "/subscriptions/a075e71f-4749-4d79-aa41-c62c7091b496/resourcegroups/libblog/providers/microsoft.web/sites/libblog"
      ],
      "originAlertId": "a075e71f-4749-4d79-aa41-c62c7091b496_libBlog_microsoft.insights_metricAlerts_Too many succesful views_137837297",
      "firedDateTime": "2020-04-12T00:35:49.6989885Z",
      "resolvedDateTime": "2020-04-12T00:46:45.1095606Z",
      "description": "",
      "essentialsVersion": "1.0",
      "alertContextVersion": "1.0"
    },
    "alertContext": {
      "properties": null,
      "conditionType": "SingleResourceMultipleMetricCriteria",
      "condition": {
        "windowSize": "PT5M",
        "allOf": [
          {
            "metricName": "Http2xx",
            "metricNamespace": "Microsoft.Web/sites",
            "operator": "GreaterThan",
            "threshold": "5",
            "timeAggregation": "Total",
            "dimensions": [
              {
                "name": "ResourceId",
                "value": "libblog.azurewebsites.net"
              }
            ],
            "metricValue": 4,
            "webTestName": null
          }
        ],
        "windowStartTime": "2020-04-12T00:38:33.513Z",
        "windowEndTime": "2020-04-12T00:43:33.513Z"
      }
    }
  }
}
```
