import qrcode
import time
from databases import VisitorsCRUD
from databases import HomeownersCRUD


class QRGenerate:
    def __init__(self):
        self.today_date = time.strftime("%m-%d-%Y")

    def getQrVisit(self, user):  # Get the QR code of the registered Homeowner
        self.imgVist = qrcode.make(f"0, {user.name}, {user.vehicle}, {user.plate_number}, {user.contact}, {user.purpose},{self.today_date}, VISITOR")
        self.imgVist.save(f'qr_generate_scanner/qr_saves/VisitQR/QrVisit{user.name}-{self.today_date}.png')

    def getQrHome(self, user):
        self.imgHome = qrcode.make(
            f"1,{user.name}, {user.blkno}, {user.lotno}, {user.pltno}, {user.contc}, {user.email}, {user.vehicle},{self.today_date}, HOMEOWNER")
        self.imgHome.save(f'qr_generate_scanner/qr_saves/HomeQR/QrHome{user.name}-{self.today_date}.png')

    def genQrHome(self, list):
        self.imgHome = qrcode.make(
            f"1,{list[1]}, {list[2]}, {list[3]}, {list[4]}, {list[5]}, {list[6]}, {list[7]},{self.today_date}, HOMEOWNER")
        self.imgHome.save(f'qr_generate_scanner/qr_saves/HomeQR/QrHome{list[1]}-{self.today_date}.png')

    def genQrVisit(self, person):
        self.imgVist = qrcode.make(f"0, {person[0]}, {person[1]}, {person[2]}, {person[3]}, {person[4]},{self.today_date}, VISITOR")
        self.imgVist.save(f'qr_generate_scanner/qr_saves/VisitQR/QrVisit{person[0]}-{self.today_date}.png')




