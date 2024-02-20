import qr

if __name__ == "__main__":
    # number of half modules
    for count in range(500, 710):
        for side in ["top", "bot"]:
            #make qr code
            code, img_path = qr.makeQR(count, side, outdir="qrcodes")
            #edit qr code text
            qr.addText(code, img_path)

    print("QR codes generated and saved successfully.")