# SmartGrade-Numpy 📊✨
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/Library-NumPy-blue.svg)](https://numpy.org/)

---

<iframe width="560" height="315" src="https://www.youtube.com/embed/NaibvhRw110?si=PKAuVs_bVPT4yBeW&amp;controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## ภาษาไทย 🇹🇭

ยินดีต้อนรับสู่ **SmartGrade-Numpy**! 👋 โปรเจกต์นี้คือระบบจัดการและวิเคราะห์คะแนนนักเรียนที่ใช้ไลบรารี **NumPy** อันทรงพลังของ Python 🐍 เพื่อจัดการข้อมูลคะแนนในรูปแบบ Array ทำให้การคำนวณและการวิเคราะห์มีประสิทธิภาพ โค้ดนี้สามารถ:

* **บันทึกและโหลดข้อมูล** นักเรียน, วิชา, และคะแนน.
* **คำนวณคะแนนเฉลี่ย** ทั้งรายวิชาและรายบุคคล.
* **ระบุผู้ที่ได้คะแนนสูงสุด** ในแต่ละวิชา.
* **ตรวจสอบและแสดงรายชื่อผู้สอบตก**.

### ทำไมต้อง SmartGrade-Numpy? 🤔

เราสร้าง SmartGrade-Numpy ขึ้นมาเพื่อเป็น **ตัวอย่างการประยุกต์ใช้ NumPy ในการจัดการข้อมูลทางการศึกษา** 💡 ช่วยให้คุณ:

* **เรียนรู้และทำความเข้าใจ** 🧠 การใช้งาน NumPy Array สำหรับการจัดเก็บและประมวลผลข้อมูลตัวเลขขนาดใหญ่.
* **ค้นหาและอ้างอิง** 🔍 เทคนิคการคำนวณค่าเฉลี่ย, ค่าสูงสุด, และการกรองข้อมูลโดยใช้ฟังก์ชันของ NumPy.
* **ฝึกฝนและสร้างแรงบันดาลใจ** ✨ ในการสร้างระบบจัดการข้อมูลที่ซับซ้อนขึ้นด้วย Python และไลบรารีที่จำเป็น.
* **สาธิตการจัดการไฟล์ JSON** 📁 เพื่อบันทึกและโหลดข้อมูลการตั้งค่าและชื่อต่างๆ.

### โครงสร้างของ Repository 📁

Repository นี้ประกอบด้วยไฟล์หลักและไฟล์ข้อมูลสำหรับระบบ:


```

SmartGrade-Numpy/

├── grade.py # โค้ดหลักสำหรับระบบ SmartGrade

├── data/ # โฟลเดอร์สำหรับบันทึกข้อมูลคะแนน

├── datetime/ # โฟลเดอร์สำหรับบันทึกข้อมูลคะแนน (จะถูกสร้างอัตโนมัติ)

     └── config.json # ไฟล์กำหนดค่าจำนวนนักเรียน/วิชา

     └── student_names.json # ไฟล์เก็บชื่อนักเรียน

     └── subject_names.json # ไฟล์เก็บชื่อวิชา

└── ...

```

### การตั้งค่าและการใช้งาน 🛠️

เพื่อให้สามารถรันโค้ดใน repository นี้ได้ คุณต้องติดตั้ง Python และไลบรารีที่จำเป็น:

1.  **ติดตั้ง Python**:
    * ดาวน์โหลด Python จาก [python.org](https://www.python.org/downloads/) (แนะนำเวอร์ชันล่าสุดสำหรับ Python 3).
2.  **ติดตั้ง NumPy**:
    * เปิด Terminal หรือ Command Prompt และใช้คำสั่ง pip:
        ```bash
        pip install numpy
        ```
3.  **โคลน Repository**:
    * เปิด Terminal หรือ Command Prompt และใช้คำสั่ง Git:
        ```bash
        git clone [https://github.com/YourUsername/SmartGrade-Numpy.git](https://github.com/YourUsername/SmartGrade-Numpy.git)
        cd SmartGrade-Numpy
        ```
4.  **ตั้งค่าเริ่มต้น (Optional)**:
    * คุณสามารถแก้ไข `config.json`, `student_names.json`, และ `subject_names.json` เพื่อกำหนดจำนวนนักเรียน, วิชา และชื่อเริ่มต้นได้. หากไม่มีไฟล์เหล่านี้ หรือโฟลเดอร์ `data` โปรแกรมจะสร้างให้ใหม่.

### วิธีการรันโค้ด 🚀

คุณสามารถรันไฟล์ `grade.py` ได้โดยตรง:

```bash
python grade.py

```

เมื่อรันโปรแกรม:

-   โปรแกรมจะตรวจสอบว่ามีข้อมูลเก่าหรือไม่ หากมี จะถามว่าต้องการโหลดข้อมูลเก่า หรือสร้างข้อมูลใหม่.
-   หากสร้างข้อมูลใหม่ คุณจะต้องป้อนชื่อนักเรียน, ชื่อวิชา, และคะแนนของนักเรียนแต่ละคนในแต่ละวิชา.
-   โปรแกรมจะแสดงผลการวิเคราะห์คะแนน รวมถึงคะแนนเฉลี่ยรายวิชา, คะแนนเฉลี่ยรายบุคคล, ผู้ที่ได้คะแนนสูงสุดในแต่ละวิชา และรายชื่อผู้สอบตก.
-   เมื่อสิ้นสุดการทำงาน โปรแกรมจะบันทึกข้อมูลคะแนนปัจจุบันลงในโฟลเดอร์ `data` พร้อม Timestamp เพื่อการจัดการข้อมูลในอนาคต.

### คำอธิบายโค้ดโดยย่อ 🧑‍💻

ไฟล์ `grade.py` ประกอบด้วยฟังก์ชันหลักๆ ดังนี้:

-   **`load_data()`**: โหลดข้อมูลจากไฟล์ JSON และโฟลเดอร์ `data` ที่มี Timestamp ล่าสุด.
-   **`save_data()`**: บันทึกข้อมูลปัจจุบัน (config, student_names, subject_names, scores) ลงในโฟลเดอร์ `data` ที่มี Timestamp ใหม่.
-   **`input_data()`**: รับชื่อนักเรียน, ชื่อวิชา, และคะแนนจากผู้ใช้ และสร้าง NumPy Array สำหรับคะแนน.
-   **การวิเคราะห์คะแนน**:
    -   คำนวณคะแนนเฉลี่ยรายวิชา (`score.mean(axis=0)`).
    -   คำนวณคะแนนเฉลี่ยรายบุคคล (`score.mean(axis=1)`).
    -   หาคะแนนสูงสุดในแต่ละวิชาและระบุนักเรียนที่ได้ (`score.max(axis=0)`, `score.argmax(axis=0)`).
    -   ระบุผู้สอบตก (`np.where(failed_mask)`).

### การมีส่วนร่วม 🤝

เรายินดีต้อนรับการมีส่วนร่วมจากทุกคน! 🎉 หากคุณมีแนวคิดในการปรับปรุงโค้ดนี้ (เช่น การเพิ่มฟังก์ชันการเรียงลำดับ, การสร้างรายงาน, หรือการปรับปรุง UI) หรือต้องการเพิ่มตัวอย่างที่เกี่ยวข้องอื่นๆ โปรดอ่าน [CONTRIBUTING.md](https://www.google.com/search?q=CONTRIBUTING.md) (ถ้ามี) สำหรับแนวทางในการมีส่วนร่วม.

### สิทธิ์การใช้งาน 📜

โปรเจกต์นี้อยู่ภายใต้ [MIT License](https://www.google.com/search?q=LICENSE)

----------

## English 🇬🇧

Welcome to **SmartGrade-Numpy**! 👋 This project is a student grade management and analysis system leveraging Python's powerful **NumPy** library 🐍 to handle grade data in Array format, ensuring efficient computation and analysis. This code can:

-   **Save and load data** for students, subjects, and scores.
-   **Calculate average scores** for both subjects and individual students.
-   **Identify top scorers** in each subject.
-   **Check for and display failing students**.

### Why SmartGrade-Numpy? 🤔

We created SmartGrade-Numpy to serve as a **clear example of applying NumPy in educational data management** 💡, helping you to:

-   **Learn and understand** 🧠 the use of NumPy Arrays for storing and processing large numerical datasets.
-   **Find and reference** 🔍 techniques for calculating averages, maximums, and filtering data using NumPy functions.
-   **Practice and get inspired** ✨ to build more complex data management systems with Python and essential libraries.
-   **Demonstrate JSON file handling** 📁 for saving and loading configuration and naming data.

### Repository Structure 📁

This repository consists of the main code file and data files for the system:

```
SmartGrade-Numpy/
├── grade.py                 # Main code for the SmartGrade system
├── data/                    # Folder for saving score data
├── datetime/                # Folder for saving score data (will be created automatically)
   └── config.json           # Configuration file for student/subject counts
   └── student_names.json    # File to store student names
   └── subject_names.json    # File to store subject names
└── ...

```

### Setup and Usage 🛠️

To run the code in this repository, you need to have Python and the necessary libraries installed:

1.  **Install Python**:
    -   Download Python from [python.org](https://www.python.org/downloads/) (latest Python 3 version recommended).
2.  **Install NumPy**:
    -   Open your Terminal or Command Prompt and use the pip command:
        
        Bash
        
        ```
        pip install numpy
        
        ```
        
3.  **Clone the Repository**:
    -   Open your Terminal or Command Prompt and use the Git command:
        
        Bash
        
        ```
        git clone [https://github.com/YourUsername/SmartGrade-Numpy.git](https://github.com/YourUsername/SmartGrade-Numpy.git)
        cd SmartGrade-Numpy
        
        ```
        
4.  **Initial Setup (Optional)**:
    -   You can modify `config.json`, `student_names.json`, and `subject_names.json` to define initial student counts, subject counts, and names. If these files or the `data` folder are missing, the program will create them.

### How to Run the Code 🚀

You can run the `grade.py` file directly:

Bash

```
python grade.py

```

Upon running the program:

-   The program will check for existing data. If found, it will ask if you want to load old data or create new data.
-   If creating new data, you will be prompted to enter student names, subject names, and scores for each student in each subject.
-   The program will then display the grade analysis, including subject-wise averages, individual student averages, top scorers in each subject, and a list of failing students.
-   Upon completion, the program will save the current score data into a `data` folder with a timestamp for future data management.

### Brief Code Explanation 🧑‍💻

The `grade.py` file contains the following main functions:

-   **`load_data()`**: Loads data from JSON files and the latest timestamped `data` folder.
-   **`save_data()`**: Saves current data (config, student_names, subject_names, scores) into a new timestamped `data` folder.
-   **`input_data()`**: Receives student names, subject names, and scores from the user, and creates a NumPy Array for scores.
-   **Grade Analysis**:
    -   Calculates subject-wise averages (`score.mean(axis=0)`).
    -   Calculates individual student averages (`score.mean(axis=1)`).
    -   Finds the highest score in each subject and identifies the student (`score.max(axis=0)`, `score.argmax(axis=0)`).
    -   Identifies failing students (`np.where(failed_mask)`).

### Contribution 🤝

We welcome contributions from everyone! 🎉 If you have ideas for improving this code (e.g., adding sorting functionalities, generating reports, or enhancing the UI) or wish to add other related examples, please refer to [CONTRIBUTING.md](https://www.google.com/search?q=CONTRIBUTING.md) (if available) for contribution guidelines.

### License 📜

This project is licensed under the [MIT License](https://www.google.com/search?q=LICENSE)