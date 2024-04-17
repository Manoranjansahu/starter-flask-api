let mqttClient;

window.addEventListener("load", (event) => {
  connectToBroker();
});

function connectToBroker() {
  const clientId = "client" + Math.random().toString(36).substring(7);

  // Change this to point to your MQTT broker
  const host = "wss://broker.emqx.io:8084/mqtt";

  const options = {
    keepalive: 60,
    clientId: clientId,
    protocolId: "MQTT",
    protocolVersion: 4,
    clean: true,
    reconnectPeriod: 1000,
    connectTimeout: 30 * 1000,
  };

  mqttClient = mqtt.connect(host, options);

  mqttClient.on("error", (err) => {
    console.log("Error: ", err);
    mqttClient.end();
  });

  mqttClient.on("reconnect", () => {
    console.log("Reconnecting...");
  });

  mqttClient.on("connect", () => {
    console.log("Client connected:" + clientId);
  });

  // Received
  mqttClient.on("message", (topic, message, packet) => {
    console.log(
      "Received Message: " + message.toString() + "\nOn topic: " + topic
    );
  });
  publishMessage();
  
}

function publishMessage() {

  const topic = "topic/to/publish";

  console.log(`Sending Topic: ${topic}, Message: ${message}`);

  mqttClient.publish(topic, "this is test message", {
    qos: 0,
    retain: false,
  });
}
