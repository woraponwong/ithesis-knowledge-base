คู่มือการเข้าใช้งาน Power BI Template
================================

#. เปิดไฟล์ Power BI Template : iThesis Analytics Template 2021

    โดยหากมีการเชื่อมต่อกับอินเตอร์เน็ตภายนอกมหาวิทยาลัย จะต้องทำการเชื่อมต่อ Tunnel ก่อน

    .. figure:: /images/template01.jpeg
        :width: 40% 
        :align: center

#. กรอก Database และ Server

    Database : default_univDB Server : dbs.ithesis.com

    .. figure:: /images/template02.png
        :align: center

#. กรอก User name และ Password

    .. figure:: /images/template03.png
        :align: center

#. พบหน้า Power BI View ไปที่แถบเมนู Home และ Transform Data

    .. figure:: /images/template04.png
        :align: center

#. พบหน้า Power Query ไปที่ Queries เลือกที่ Folder : Parameter > Database > Manage Parameter

    .. figure:: /images/template05.png
        :align: center

#. การใส่ Database และ Server ในช่อง Current Valves

    .. figure:: /images/template06.png
        :align: center

    * Database : ชื่อ Database ของระบบ iThesis มหาวิทยาลัย (univ… ,iThesis… )​
    * Server ขึ้นกับ การเชื่อมต่อกับอินเตอร์เน็ต
      
      * ภายนอกมหาวิทยาลัย

            Server : localhost

      * ภายในมหาวิทยาลัย

            Server : IP Server มหาวิทยาลัย

#. การใส่ User name และ Password บนหน้า Power Query

    ไปที่ แถบเมนู Home และ Data source settings

    .. figure:: /images/template07.png
        :align: center

    พบ Edit Permissions ให้ทำการกดที่ Edit..

    .. figure:: /images/template08.png
        :align: center

#. นำข้อมูลเข้าหน้า View

    กดที่ Close & Apply แล้วรอ Power BI โหลดข้อมูล

    .. figure:: /images/template09.png
        :align: center

#. ใส่ University Logo ในทุกหน้ารายงาน

    ลบรูป University Logo > Import Image (University Logo) > วางไว้ด้านข้าง iThesis Logo

    .. figure:: /images/template10.png
        :align: center

#. การ Save และ Publish File

    * การ Save
        
        ไปที่ File > Save As > ทำการเลือกที่จัดเก็บไฟล์และใส่ชื่อรายงาน

        .. figure:: /images/template11.png
            :width: 50% 
            :align: center

        .. figure:: /images/template12.png
            :align: center

    * การ Publish File

        .. figure:: /images/template13.png
            :align: center
