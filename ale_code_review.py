import segno
from PIL import Image, ImageDraw, ImageFont
#from reportlab.pdfgen import canvas

#pdf_output_path = 'mdomqrcodes9.pdf'
#pdf_canvas = canvas.Canvas(pdf_output_path) #create pdf

## in main
for i in list(range(1,411)):

        if i%2==0:
                text = "'mDOM_top-{}'".format(i)                
        else:
                text = "'mDOM_bot-{}'".format(i)
## in a make qr code function        
        # make qr code                
        image_path = '{}.png'.format(text)
        qr = segno.make(text)
        qr.save(path, scale=10)
        
## in a edit text function        
        #open image
        image = Image.open(image_path)
        #add text
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        text_position=(100,2)
        text_color = 'black'
        draw.text(text_position, text, font=font, fill=text_color)
        #save the modified image
        image.save(image_path) 
        #add the image to the pdf
        #pdf_canvas.drawInlineImage(output_path,0,0)
        #add a new page for the next image
        #pdf_canvas.showPage()

        
#save pdf
#pdf_canvas.save()
