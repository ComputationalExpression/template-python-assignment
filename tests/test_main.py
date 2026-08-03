import machine
import network

from main import main


def test_main_runs_with_mockro() -> None:
    main()


def test_led_can_be_turned_on() -> None:
    led = machine.Pin(2, machine.Pin.OUT)
    led.on()
    assert led.value() == 0


def test_wlan_initially_inactive() -> None:
    wlan = network.WLAN(network.STA_IF)
    assert not wlan.active()
