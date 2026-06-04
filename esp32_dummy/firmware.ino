#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "YOUR_WIFI";
const char* password = "YOUR_PASSWORD";

void setup()
{
Serial.begin(115200);

```
WiFi.begin(ssid, password);

while(WiFi.status() != WL_CONNECTED)
{
    delay(500);
    Serial.print(".");
}

Serial.println("\nWiFi Connected");

sendResult();
```

}

void loop()
{
}

void sendResult()
{
HTTPClient http;

```
http.begin("http://YOUR_PC_IP:5000/update");

http.addHeader(
    "Content-Type",
    "application/json"
);

String payload =
"{\"component\":\"Arduino-Uno\",\"confidence\":87}";

int responseCode =
http.POST(payload);

Serial.print("Response Code: ");
Serial.println(responseCode);

http.end();
```

}
