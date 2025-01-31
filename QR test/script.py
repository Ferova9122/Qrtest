import qrcode

# Paso 1: URL del archivo de audio
audio_url = "https://drive.google.com/file/d/1-AbG2Rpw_18EXXbppggYff2mzS9oyoRM/view?usp=drive_link"  # Cambia por tu enlace

# Paso 2: Configura el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Paso 3: Agrega el enlace al QR
qr.add_data(audio_url)
qr.make(fit=True)

# Paso 4: Genera la imagen del QR
img = qr.make_image(fill_color="black", back_color="white")

# Paso 5: Guarda la imagen en un archivo
img.save("codigo_qr_audio.png")

print("Código QR generado y guardado como 'codigo_qr_audio.png'")