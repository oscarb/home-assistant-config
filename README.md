# Home Assistant Config

My configuration for [Home Assistant](https://www.home-assistant.io/), running in Docker on a Synology DS718+ NAS.

## Instant updates from Tellstick sensors

### Mosquitto

1. Install Mosquitto in Synology Package.
2. Edit the configuration file
    
    sudo nano /volume1/@appstore/mosquitto/var/mosquitto.conf

    1. Disable anonymous usage

        allow_anonymous false

    2. Add a password file
    
        password_file /volume1/@appstore/mosquitto/var/password_file

3. Add users to Mosquitto

    cd /volume1/@appstore/mosquitto
    sudo nano /volume1/@appstore/mosquitto/var/password_file

    1. Add users to the file

        username:password

    2. Upgrade the password file

        sudo ./bin/mosquitto_passwd -U ./var/password_file 

4. Restart Mosquitto

### Tellsticknet

1. Clone the repo

    git clone https://github.com/molobrakos/tellsticknet.git

2. Build the Docker image

        sudo docker build -t tellsticknet .

3. Create a configuration file named `tellsticknet.conf`:

        ---
        # Bathroom motion sensor
        name: Bathroom Motion
        component: binary_sensor
        protocol: arctech
        model: selflearning
        unit: 10
        house: 12345678
        device_class: motion

    * ID:s for House can be retrieved by either Telldus Live or running the discover command inside the Docker container

4. Start a Docker container

    * Enable auto-restart
    * `/config/tellsticknet/tellsticknet.conf` -> `/app/tellsticknet.conf`
    * Use the same network as Docker host
    * Add an environment variable named `MQTT_URL`:

         mqtt://username:password@localhost:1883