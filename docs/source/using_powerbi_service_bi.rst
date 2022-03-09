การใช้งาน Power BI Service
=========================

Visualization (การแสดงผลข้อมูล)
-----------------------------

การ Drill Down ใน Chart
~~~~~~~~~~~~~~~~~~~~~~~

* Chart ใน Power BI สามารถทำการ Drill Up หรือ Drill Down ได้
* Dimension ที่สามารถ Drill Down ลงไปนั้นไม่จำเป็นต้องสร้าง Hierarchy ขึ้นมาก่อนก็ได้
* Chart ใน Power BI ที่สามารถทำการ Drill ได้มีดังนี้
    - Clustered bar charts
    - Clustered column charts
    - Stacked bar charts
    - Stacked column charts
    - Dual axis charts
    - Pie charts
    - Line Charts
    - Waterfall charts
    - Scatter charts
    - Bubble charts

.. figure:: /images/visualization01.png
    :align: center

Drill Down Focus on ใน Chart

  * เมื่อกด drill down Focus on Icon เป็นการ Interactive drill down จาก Chart ในข้อมูลที่สนใจ เช่น เลือก Asia เมื่อคลิกเลือก Asia เข้าแสดงข้อมูลประเทศที่อยู่ใน Asia

    .. figure:: /images/visualization02.jpeg
        :align: center

    .. figure:: /images/visualization03.jpeg
        :align: center

Drill Up Icon

  * เมื่อกด Drill Up Icon เป็นการ Drill Up ข้อมูลขึ้นไปยัง level ถัดไป

    .. figure:: /images/visualization04.png
        :align: center

Expand all down one level

  * Expand all down one level in the hierarchy เป็นการ Drill Down ข้อมูลลงไปยัง Level ถัดไปโดยที่ยังคงมี Level ก่อนหน้าอยู่ด้วย เช่น การ Drill จาก Region Name ไปที่ Region Name และ Country ทั้ง 2 level

    .. figure:: /images/visualization05.png
        :align: center

    .. figure:: /images/visualization06.png
        :align: center 

Go to the next level

  * Go to the next level in the hierarchy เป็นการ Drill Down ข้อมูลลงไปยัง Level ถัดไปทั้งหมดโดยที่ไม่มีการคงอยู่ของ Level ก่อนหน้า เช่น การ Drill จาก Region Name ไปที่ Country เพียง level เดียวเท่านั้น

    .. figure:: /images/visualization07.png
        :align: center   

    .. figure:: /images/visualization08.png
        :align: center  

การ Filter Data
~~~~~~~~~~~~~~~

* Filter คือ การกรองข้อมูลที่เราต้องดู
* Power BI มี Filter อยู่ 3 level
    - Visualization-level Filter  มีผลกับ Visualization ที่เลือกเท่านั้น
    - Page-level Filter  มีผลกับทุก Visualization ในหน้าที่เลือกเท่านั้น
    - Report-level Filter  มีผลกับทุก Visualization ในรายงานเท่านั้น​
* เมื่อทำการสร้าง Visual และนำ Dimension หรือ measurement มาในวางใน Field Well ก็จะไปปรากฎที่ Visualization level filter

การ Filter Data และ Data Type

  * Filter level อื่นทำได้โดยการเลือกคอลัมน์ที่ต้องการจะทำการ Filter ลากไปวางยัง Page level filter หรือ Report level filter
  * สามารถทำการ Filter กับ Data Type เหล่านี้คือ Text, Dates, NUmeric values ซึ่งมีความแตกต่างกันตามแต่ละ Data Type

    .. figure:: /images/visualization09.png
        :width: 50%
        :align: center  

การ Filter Text Data

  * Basic Filtering สามารถติ๊กเลือกรายการที่ต้องการ Filter ได้

    .. figure:: /images/visualization10.png
        :width: 50%
        :align: center  

  * Advanced Filtering สามารถระบุเงื่อนไขที่ต้องการ Filter ข้อมูลด้วยเงื่อนไขอะไรบ้างได้

    .. figure:: /images/visualization11.png
        :width: 50%
        :align: center  

  * Top N Filtering เป็นการ Filter ข้อมูลในลักษณะของ Top/Bottom ตามข้อมูลที่ต้องการ (By Value) ได้และสามารถกำหนดจำนวนลำดับที่ต้องการได้ (N)

    .. figure:: /images/visualization12.png
        :align: center  

  * Filter Options ใน Advanced Filter สำหรับข้อมูลที่เป็น Text

    .. list-table:: ตาราง Filter Options
        :widths: 30 70
        :header-rows: 1

        * - Filter Options
          - Deciption
        * - Contains
          - The selected field contains the search text anywhere in the field data.
        * - Does Not Contain
          - The selected field does not contain the search text anywhere in the field data.
        * - Starts with
          - The selected field begins with the search text, followed by any data.
        * - Does Not Start With
          - The selected field does not begins with the search text, followed by any data.
        * - Is
          - The selected field matches the search text exactly.
        * - Is Not
          - The selected field does not matches the search text exactly.
        * - Is Blank
          - The selected field is blank.
        * - Is Not Blank
          - The selected field is not blank.

การ Filter Numeric Data

  * สามารถระบุข้อมูลช่วงที่ต้องการได้

    .. figure:: /images/visualization13.png
        :align: center 

  * Filter Option ใน Advanced Filter สำหรับข้อมูลที่เป็น Numeric Data

    .. list-table:: ตาราง Filter Options
        :widths: 30 70
        :header-rows: 1

        * - Filter Options
          - Deciption
        * - Is Less Than
          - The selected field is less than the number you are searching for.
        * - Is Less Than Or Equal To
          - The selected field is less than or equal to the number you are searching for.
        * - Is Greater Than
          - The selected field is greater than the number you are searching for.
        * - Is Greater Than Or Equal To
          - The selected field is greater than or equal to the number you are searching for.
        * - Is
          - The selected field matches exactly the number you are searching for.
        * - Is Not
          - The selected field does not matches exactly the number you are searching for.
        * - Is Blank
          - The selected field is blank.
        * - Is Not Blank
          - The selected field is not blank.

การ Filter Date & Time

  * Basic Filtering สามารถเลือกรายการที่ต้องการ Filter ได้

    .. figure:: /images/visualization14.png
        :width: 50%
        :align: center 

  * Advanced Filtering สามารถระบุเงื่อนไขที่ต้องการ Filter ข้อมูลด้วยเงื่อนไขอะไรบ้างได้

    .. figure:: /images/visualization15.png
        :align: center 

  * Top N Filtering เป็นการ Filter ข้อมูลในลักษณะของ Top/Bottom ตามข้อมูลที่ต้องการ (By Value) ได้และสามารถกำหนดจำนวนลำดับที่ต้องการได้ (N)

    .. figure:: /images/visualization16.png
        :width: 50%
        :align: center 

  * Filter Option ใน Advanced Filter สำหรับข้อมูลที่เป็น Date & Time

    .. list-table:: ตาราง Filter Options
        :widths: 30 70
        :header-rows: 1

        * - Filter Options
          - Deciption
        * - Is
          - The selected field contains the date that you are searching for.
        * - Is Not
          - The selected field does not contains the date that you are searching for.
        * - Is On Or After
          - The selected field contains dates beginning with the date that you entered or later.
        * - Is Before
          - The selected field contains the date before the date that you entered; that is, earlier dates that do not include the date you entered.
        * - Is On Or Before
          - DThe selected field contains the date on or before the date that you entered; that is, earlier dates up to and include the date you entered.
        * - Is Blank
          - The selected field is blank.
        * - Is Not Blank
          - The selected field is not blank.

  * Logical Filter Option สำหรับข้อมูลทุกประเภท

    .. list-table:: ตาราง Filter Options
        :widths: 30 70
        :header-rows: 1

        * - Filter Options
          - Deciption
        * - And
          - Applied both filter elements to reduce the amount of data allowed though the filter.
        * - Or
          - Applied both filter elements to reduce the amount of data allowed though the filter.

