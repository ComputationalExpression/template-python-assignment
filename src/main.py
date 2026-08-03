import machine
import network


def main() -> None:
    led = machine.Pin(2, machine.Pin.OUT)
    led.on()

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)


if __name__ == "__main__":
    main()
