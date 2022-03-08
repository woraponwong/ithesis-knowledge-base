คู่มือการเชื่อม Tunnel
=================

#. การดาวน์โหลดโปรแกรมที่ใช้สําหรับ Tunnel โปรแกรม PuTTY  ตามลิงค์ https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

    .. figure:: /images/tunnel01.jpeg
        :width: 50% 
        :align: center
        :alt: PuTTY

        PuTTY

#. การกรอกข้อมูล

    * กรอบสีแดงUserName@IPAddress ของเครื่องเซิร์ฟเวอร์ไอทีสิส
    
    * กรอบสีส้ม กรอกชื่อที่ต้องการใช้งาน

    .. figure:: /images/tunnel02.png
        :align: center

#. เแนบไฟล์ Private Key authentication

    * กดเลือกที่ SSH และเลือกที่ Auth จากนั้นกดที่ปุ่ม Browse
    * เลือกไปที่ ไฟล์ Private Key authentication
    * ที่ใช้ในการเข้าสู่เครื่องเซิร์ฟเวอร์ไอทีสิส

    .. figure:: /images/tunnel03.png
        :align: center    

    .. note::
    
        ไฟล์ Private Key authentication จะต้องทำผ่านโปรแกรม Putty gen

#. เลือกที่ Tunnels

    * ระบุ Port ที่จะถูกเปิดใช้บนเครื่อง
    * ระบุ หมายเลข IP address และ port เพื่อเชื่อมต่อ
    * ทำการบันทึกการตั้งค่า

    .. figure:: /images/tunnel04.png
        :align: center

#. การ Save ข้อมูลและเชื่อม Tunnel

    * ทำการบันทึกการตั้งค่ากดปุ่ม Save
    * เลือก Session และกดปุ่ม Loadเพื่อทำการเชื่อม Tunnel    

    .. figure:: /images/tunnel05.png
        :align: center

    .. figure:: /images/tunnel06.png
        :align: center


    