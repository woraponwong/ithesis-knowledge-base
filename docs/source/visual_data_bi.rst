Visualization (การแสดงผลข้อมูล)
=============================

Visualization หรือ การเสนอข้อมูล เป็นการแสดงผลข้อมูลในรูปแบบของกราฟ ตาราง แผนที่ กราฟฟิกต่างๆ ที่จะช่วยการสรุปผลข้อมูลให้เข้าใจได้ง่าย และยังสามารถแสดงผลในรูปแบบของ Interactive ได้อีกด้วย

.. figure:: /images/visual_data01.png
    :align: center 

รู้จัก Visualization
-----------------

#. Filters  : ฟิลเตอร์ข้อมูลที่ใช้ใน Visual
#. Visualization Pane  : การแสดงผลข้อมูล
#. Field List  : แสดงตารางข้อมูลและคอลัมน์ต่างๆ
#. Selected Field  : สามารถเลือกคอลัมน์จาก Field เพื่อนำเสนอข้อมูล
#. Field Option and Field Well
    * Field Option: Option การใช้งาน ปรับแต่ง Visual
    * Field Well : กำหนดข้อมูลที่ต้องการแสดงใน Visual

.. figure:: /images/visual_data02.png
    :align: center 

Create Table
------------

#. เลือก Visualization ที่ต้องการนำเสนอ
#. เลือก Field ที่ต้องแสดงข้อมูล
#. กำหนด Aggregate Type
#. ทำการขยายขนาด (Resizing) หรือเปลี่ยนตำแหน่ง (Position)

.. figure:: /images/visual_data03.png
    :align: center 

Type of Data
------------

    .. list-table:: The initial two data types are Descriptive (non-numeric) attributes and Values (or numeric measures)
        :widths: 30 70
        :header-rows: 1

        * - Data Types
          - Comments
        * - Attribute
          - A descriptive element and is non-numeric. It can be counted but not summed or averaged
        * - Aggregates
          - A number field whose aggregation type can be changed.
        * - Calculated Column
          - The result of a formula applied to create a new, calculated column.
        * - Calculation
          - A number field whose aggregation type can be changed as it the result of a specific calculation.
        * - Geography
          - This field can potentially be used in a map to provide geographical.
        * - Binary Data
          - A field contains data, such as images.

Aggregate Type
--------------

.. figure:: /images/visual_data04.png
    :width: 30%
    :align: center
    :alt: Aggregate Type สำหรับข้อมูลประเภท Descriptive (non-numeric) attributes

    Aggregate Type สำหรับข้อมูลประเภท Descriptive (non-numeric) attributes

.. figure:: /images/visual_data05.png
    :width: 30%
    :align: center
    :alt: Aggregate Type สำหรับข้อมูลประเภท Values (or numeric measure)

    Aggregate Type สำหรับข้อมูลประเภท Values (or numeric measure)


Enhancing Table
---------------

* Row Totals จะถูกกำหนดให้แสดงโดยอัตโนมัติ แต่สามารถนำออกได้โดย
  * เลือก Visualization Table ที่ต้องการ
  * ไปที่ Visualization Pane และคลิก Format
  * เลือก Total ขยาย Total และคลิกเลือก off

.. figure:: /images/visual_data06.png
    :width: 30%
    :align: center 

กำหนด Formatting ของข้อมูล
------------------------

.. figure:: /images/visual_data07.png
    :align: center 

* Power BI สามารถกำหนดรูปแบบ (Format) ในการแสดงผลได้
* การเปลี่ยน Format โดย เลือก Modeling tab และเลือก Format จากนั้นเลือก กำหนด Format ของข้อมูลที่ต้องการให้แสดงใน Visualization

การสลับไปมาระหว่าง Visualization
------------------------------

* Visualization ประเภท Table, Matrix, Multi-Row Card สามารถทำการสลับเปลี่ยนได้โดยที่ไม่ต้องทำการสร้างขึ้นใหม่ 
* ทำการสลับได้โดยการคลิกเลือก Visualization ใน Report view ที่ต้องการสับเปลี่ยน และเลือก Visualization ใหม่ที่ต้องการ
* เนื่องจากการแสดงผลอยู่ในรูปของคอลัมน์และแถวจึงสามารถสลับเปลี่ยนได้

Text-Based Visualization
------------------------

Card
~~~~

เป็นการแสดงผลข้อมูลในกรณีต้องการแสดงค่าใดๆเพียงค่าเดียว เช่น เปอร์เซ็นต์ประชากรทั้งหมดจากทุกทวีป ซึ่งไม่เหมาะที่จะใช้ Table หรือ Matrix ในการแสดงผล

* คลิกที่ว่างใน Report view, คลิกเลือกปุ่ม Card icon ใน Visualization Pane
* คลิกเลือก Population (จากตาราง Fact Population) ไปวางที่ Fields
* ข้อมูลผลรวม Population จะไปแสดงที่ Card
* สามารถทำ Formatting ของ Card ได้โดยใช้ Format icon ใน Visualization Pane

.. figure:: /images/visual_data08.png
    :align: center

Multi-Row Card
~~~~~~~~~~~~~~

เป็นการแสดงผลข้อมูลเป็นตารางที่เป็น Multi Row Card รูปแบบคอลัมน์เดี่ยว หรือแถวเดี่ยว มีผลลัพธ์ที่เข้าใจง่าย

* คลิกที่ว่างใน Report view, คลิกเลือกปุ่ม Multi-Row icon ใน Visualization Pane
* คลิกเลือก Population, Yera (จากตาราง Fact Population) ไปวางที่ Fields
* คลิกเลือก Country (จากตาราง DIM-Region) ไปวางที่ Fields
* ข้อมูลจะไปแสดงที่ Multi-Row Card
* สามารถกำหนด Aggregate type ได้

.. figure:: /images/visual_data09.png
    :align: center

Chart
-----

  - Bar charts
  - Column charts
  - Stacked Bar Charts
  - Clustered Bar Charts
  - 100% Stacked Bar Charts
  - Stacked Column Charts
  - Clustered Column Charts
  - 100% Stacked Column Charts
  - Line charts
  - Area Charts
  - Ribbon charts
  - Line and Stacked Column
  - Line and Clustered Column
  - Pie charts
  - Donut charts
  - Funnel charts
  - Scatter charts
  - Bubble charts
  - Waterfall charts

Bar Charts
~~~~~~~~~~
* คลิกที่ว่างใน Report view, คลิกเลือกปุ่ม Bar chart icon ใน Visualization Pane
* Chart Visual จะปรากฎบน Report View
* คลิกเลือก Region Name (จากตาราง DIM-Region) ไปวางที่ Axis
* คลิกเลือก PoputionFemale, PoputionMale (จากตาราง Fact Population) ไปวางที่ Value
* ข้อมูลจะไปแสดงที่ Bar Chart

.. figure:: /images/visual_data10.png
    :width: 50%
    :align: center

.. figure:: /images/visual_data11.png
    :align: center

Column Chart
~~~~~~~~~~~~

* คลิกที่ว่างใน Report view, คลิกเลือกปุ่ม Column chart icon ใน Visualization Pane
* Chart Visual จะปรากฎบน Report View
* คลิกเลือก Region Name (จากตาราง DIM-Region) ไปวางที่ Axis 
* คลิกเลือก PopulationFemale, PopulationMale (จากตาราง Fact Population) ไปวางที่ Value
* ข้อมูลจะไปแสดงที่ Column Chart

.. figure:: /images/visual_data12.png
    :width: 50%
    :align: center

.. figure:: /images/visual_data13.png
    :align: center

Bar Chart & Column Chart
~~~~~~~~~~~~~~~~~~~~~~~~

* การสร้าง Chart จาก Data Value ด้วย Measure ค่าเดียว แต่บางครั้งอาจต้องดู Chart ของ Data Value มากกว่า 1 Measure โดยแบ่งออกเป็น Bar Chart & Column Chart ย่อยได้ดังนี้
  * Stacked Bar chart
  * Stacked Column chart
  * Clustered Bar chart
  * Clustered Column chart
  * 100% Stacked Bar chart
  * 100% Stacked Column chart

    Bar Chart  
        * ต้องการดู Data Value มากกว่า 1 ค่า
        * เลือก Category [จาก DIM AgeGroup]
        * เลือก PopulationFemale และ PopulationMale  [จาก Fact Population]

        .. figure:: /images/visual_data14.jpeg
            :align: center
            :alt: Stacked Bar

            Stacked Bar

        .. figure:: /images/visual_data15.jpeg
            :align: center
            :alt: Clustered Bar

            Clustered Bar

        .. figure:: /images/visual_data16.jpeg
            :align: center
            :alt: 100% Stacked Bar

            100% Stacked Bar

    Column Chart
        * ต้องการดู Data Value มากกว่า 1 ค่า
        * เลือก Category [จาก DIM AgeGroup]
        * เลือก PopulationFemale และ PopulationMale  [จาก Fact Population]

        .. figure:: /images/visual_data17.jpeg
            :align: center
            :alt: Stacked Column

            Stacked Column

        .. figure:: /images/visual_data18.jpeg
            :align: center
            :alt: Clustered Column

            Clustered Column

        .. figure:: /images/visual_data19.jpeg
            :align: center
            :alt: 100% Stacked Column

            100% Stacked Column

Line Chart
~~~~~~~~~~

เป็นการแสดงผลข้อมูลเป็นกราฟเส้น เพื่อเปรียบเทียบข้อมูล

* คลิกที่ว่างใน Report view, คลิกเลือกปุ่ม Line chart icon ใน Visualization Pane
* Chart Visual จะปรากฎบน Report View
* คลิกเลือก Region Name (จากตาราง DIM-Region) ไปวางที่ Legend
* คลิกเลือก PopulationFemale, PopulationMale (จากตาราง Fact Population) ไปวางที่ Values
* ข้อมูลจะไปแสดงที่ Line Chart

.. figure:: /images/visual_data21.jpeg
    :width: 50%
    :align: center

.. figure:: /images/visual_data20.jpeg
    :align: center

Line and Stacked Column Chart
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

เป็นการแสดงผลข้อมูลเป็นกราฟแท่งและเส้น เพื่อเปรียบเทียบข้อมูล

* กราฟแท่งและเส้นจะมีความสัมพันธ์กันของข้อมูลที่นำมา Shared Axis

.. figure:: /images/visual_data23.jpeg
    :width: 50%
    :align: center

.. figure:: /images/visual_data22.jpeg
    :align: center

Line and Clustered Column Chart
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

เป็นการแสดงผลข้อมูลเป็นกราฟแท่งและเส้น เพื่อเปรียบเทียบข้อมูล

* กราฟแท่งและเส้นจะมีความสัมพันธ์กันของข้อมูลที่นำมา Shared Axis

.. figure:: /images/visual_data25.jpeg
    :width: 50%
    :align: center

.. figure:: /images/visual_data24.jpeg
    :align: center

Pie Chart
~~~~~~~~~

เป็นการแสดงผลข้อมูลเป็นกราฟวงกลม เน้นการดูข้อมูลเป็นสัดส่วน

* คลิกที่ว่างใน Report view, คลิกเลือกปุ่ม Pie chart icon ใน Visualization Pane
* Chart Visual จะปรากฎบน Report View
* คลิกเลือก PopulationTotal (จากตาราง FACT-Population) ไปวางที่ Value
* คลิกเลือก Category (จากตาราง DIM-AgeGroup) ไปวางที่ Legend

.. figure:: /images/visual_data26.jpeg
    :align: center

Donut Chart
~~~~~~~~~~~

เป็นการแสดงผลข้อมูลเป็นกราฟวงกลม เน้นการดูข้อมูลเป็นสัดส่วน

* คลิกที่ว่างใน Report view, คลิกเลือกปุ่ม Donut chart icon ใน Visualization Pane
* Chart Visual จะปรากฎบน Report View
* คลิกเลือก PopulationTotal (จากตาราง FACT-Population) ไปวางที่ Value
* คลิกเลือก Category (จากตาราง DIM-AgeGroup) ไปวางที่ Legend
* ข้อมูลจะไปแสดงที่ Donut Chart

.. figure:: /images/visual_data27.jpeg
    :align: center
