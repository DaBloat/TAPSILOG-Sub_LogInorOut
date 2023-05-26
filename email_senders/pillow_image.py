from PIL import Image, ImageDraw, ImageFont
import os


class PicEdit:
    def __init__(self, name, code):
        self.img = Image.open('email_senders/T.A.P.S.I.Log.png')
        self.mod_img = ImageDraw.Draw(self.img)
        self.fnt = ImageFont.truetype("ariblk.ttf", 100)
        self.fnt2 = ImageFont.truetype("ariblk.ttf", 50)
        self.mod_img.text((350, 38), f"{name}", font=self.fnt2, fill=(3, 3, 3))
        self.mod_img.text((130, 180), f"{code}", font=self.fnt, fill=(3, 3, 3))
        self.img.save(f'email_senders/image_to_send/send{name}-{code}.png')
        print("SAVED")

    def delete_pic(self):
        os.remove('email_senders/image_to_send/send{name}-{code}.png')
