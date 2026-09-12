from pathlib import Path
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else "joypad-os")
cmake = root / "src" / "CMakeLists.txt"
text = cmake.read_text(encoding="utf-8")

old = "target_compile_definitions(joypad_n642usb PRIVATE CONFIG_N642USB=1 CONFIG_USB=1 DISABLE_USB_HOST=1 N64_PIN_DATA=29)"
new = """target_compile_definitions(joypad_n642usb PRIVATE
    CONFIG_N642USB=1
    CONFIG_USB=1
    DISABLE_USB_HOST=1
    N64_PIN_DATA=4
    WS2812_PIN=16
    USE_BOOTSEL_BUTTON=1
    USBD_DEFAULT_MODE=USB_OUTPUT_MODE_XINPUT
)"""

if old not in text:
    raise SystemExit("ERROR: expected Joypad OS 2.4.0 n642usb target was not found; refusing to patch an unknown source tree")
text = text.replace(old, new, 1)
cmake.write_text(text, encoding="utf-8")
print("Patched joypad_n642usb: RP2040-Zero, DATA GPIO4, NeoPixel GPIO16, default XInput")
