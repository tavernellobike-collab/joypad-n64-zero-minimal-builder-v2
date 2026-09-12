# N64 -> USB builder for Waveshare RP2040-Zero

Builder minimale per GitHub Actions.

Compila **un solo firmware** da Joypad OS v2.4.0:

- Board: Waveshare RP2040-Zero
- Controller: Nintendo 64 originale
- N64 DATA: GPIO 4
- NeoPixel onboard: GPIO 16
- USB default: XInput
- Target compilato: `joypad_n642usb` soltanto

## Uso

1. Crea un repository GitHub vuoto.
2. Carica questi tre elementi nella root del repository:
   - `.github/`
   - `patch_n64_zero.py`
   - `README.md`
3. Vai in **Actions**.
4. Apri **Build N64 USB for RP2040-Zero**.
5. Premi **Run workflow**.
6. A build completata, scarica l'Artifact **N64-RP2040-Zero-GPIO4-XInput**.
7. Estrai lo ZIP dell'Artifact e troverai `N64_RP2040-Zero_GPIO4_XInput.uf2`.

Il workflow scarica Joypad OS e tutti i suoi submodule direttamente da GitHub. Non serve caricare il sorgente Joypad OS nel tuo repository.
