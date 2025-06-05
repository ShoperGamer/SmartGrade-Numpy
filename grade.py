import numpy as np
import json
import os
from datetime import datetime

# เอาไว้โหลดข้อมูลเก่า
def load_data():
    data_root_folder = "data" # เปลี่ยนชื่อตัวแปรให้ชัดเจนว่าเป็น root folder
    
    # ตรวจสอบว่ามี root folder data หรือไม่
    if not os.path.exists(data_root_folder):
        print(f"\nไม่พบโฟลเดอร์ '{data_root_folder}' จะสร้างข้อมูลใหม่")
        return None, None, None, None, None

    # ค้นหาโฟลเดอร์ข้อมูลล่าสุดที่มี Timestamp
    all_timestamps = []
    # สแกนหาชื่อโฟลเดอร์ย่อยภายใน data_root_folder
    for folder_name in os.listdir(data_root_folder):
        folder_path = os.path.join(data_root_folder, folder_name)
        if os.path.isdir(folder_path): # ตรวจสอบว่าเป็นโฟลเดอร์
            try:
                # ลองแปลงชื่อโฟลเดอร์เป็น datetime object
                current_timestamp = datetime.strptime(folder_name, '%Y%m%d_%H%M%S')
                all_timestamps.append(current_timestamp)
            except ValueError:
                # ถ้าชื่อโฟลเดอร์ไม่ใช่รูปแบบ timestamp ที่คาดไว้ ให้ข้ามไป
                continue

    if not all_timestamps: # ถ้าไม่มีโฟลเดอร์ที่มี timestamp เลย
        print("\nไม่พบชุดข้อมูลที่บันทึกไว้ในโฟลเดอร์ 'data' จะสร้างข้อมูลใหม่")
        return None, None, None, None, None
    
    # หา timestamp ที่ใหม่ที่สุด
    latest_timestamp = max(all_timestamps)
    latest_timestamp_str = latest_timestamp.strftime('%Y%m%d_%H%M%S')
    
    # กำหนด path ของโฟลเดอร์ชุดข้อมูลล่าสุด
    latest_data_folder_path = os.path.join(data_root_folder, latest_timestamp_str)

    # สร้าง path ไฟล์ครบชุดสำหรับชุดข้อมูลล่าสุด
    scores_path = os.path.join(latest_data_folder_path, 'scores.npy')
    student_names_path = os.path.join(latest_data_folder_path, 'student_names.json')
    subject_names_path = os.path.join(latest_data_folder_path, 'subject_names.json')
    config_path = os.path.join(latest_data_folder_path, 'config.json')


    print(f"\nพบข้อมูลล่าสุดที่บันทึกเมื่อ: {latest_timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
    choice = input("ต้องการโหลดข้อมูลล่าสุดนี้หรือไม่? (y/n): ").lower()

    if choice == 'y':
        try:
            # ตรวจสอบว่าไฟล์ที่เกี่ยวข้องครบถ้วนสำหรับชุดข้อมูลล่าสุดหรือไม่
            if not (os.path.exists(scores_path) and
                    os.path.exists(student_names_path) and
                    os.path.exists(subject_names_path)):
                # หากไฟล์ไม่ครบ จะแจ้งและไม่โหลดชุดนี้
                raise FileNotFoundError(f"ไฟล์ข้อมูลสำหรับชุด {latest_timestamp_str} ไม่ครบถ้วนในโฟลเดอร์ '{latest_data_folder_path}'")

            score = np.load(scores_path)
            with open(student_names_path, 'r', encoding='utf-8') as f:
                student_name = json.load(f)
            with open(subject_names_path, 'r', encoding='utf-8') as f:
                subject_name = json.load(f)
            
            # โหลด config ด้วยถ้ามี (ใช้ .get เพื่อป้องกัน KeyError ถ้าไฟล์ไม่มีค่านั้น)
            student = len(student_name) # ค่าเริ่มต้น
            subject = len(subject_name) # ค่าเริ่มต้น
            if os.path.exists(config_path):
                with open(config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                student = config.get('student_count', student) # ใช้ค่าจาก config ถ้ามี
                subject = config.get('subject_count', subject) # ใช้ค่าจาก config ถ้ามี
            
            print("โหลดข้อมูลสำเร็จ!")
            return student, subject, student_name, subject_name, score
        except Exception as e:
            print(f"\nเกิดข้อผิดพลาดในการโหลดข้อมูลล่าสุด: {e}")
            print("จะสร้างข้อมูลใหม่แทน")
            return None, None, None, None, None
    else:
        print("ไม่โหลดข้อมูลเก่า จะสร้างข้อมูลใหม่แทน")
        return None, None, None, None, None

# เอาไว้เก็บข้อมูล (บันทึกไฟล์ใหม่เสมอในโฟลเดอร์ย่อยที่มี timestamp)
def save_data(student_name, subject_name, score):
    data_root_folder = "data" # เปลี่ยนชื่อตัวแปรให้ชัดเจนว่าเป็น root folder
    
    # สร้าง timestamp สำหรับชื่อโฟลเดอร์ย่อย
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    current_data_folder = os.path.join(data_root_folder, timestamp) # Path ของโฟลเดอร์ย่อยใหม่
    
    # สร้างโฟลเดอร์ย่อยใหม่
    if not os.path.exists(current_data_folder):
        os.makedirs(current_data_folder)
    
    try:
        # บันทึกไฟล์ลงในโฟลเดอร์ย่อยที่สร้างใหม่
        np.save(os.path.join(current_data_folder, 'scores.npy'), score)
        
        with open(os.path.join(current_data_folder, 'student_names.json'), 'w', encoding='utf-8') as f:
            json.dump(student_name, f, ensure_ascii=False, indent=4)
        
        with open(os.path.join(current_data_folder, 'subject_names.json'), 'w', encoding='utf-8') as f:
            json.dump(subject_name, f, ensure_ascii=False, indent=4)
        
        # บันทึก config
        config = {
            'student_count': len(student_name),
            'subject_count': len(subject_name)
        }
        with open(os.path.join(current_data_folder, 'config.json'), 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=4)
        
        print(f"\nบันทึกไฟล์ชุดใหม่ในโฟลเดอร์ '{current_data_folder}' เรียบร้อยแล้ว")
    except Exception as e:
        print(f"\nเกิดข้อผิดพลาดในการบันทึกข้อมูล: {e}")

# โหลดข้อมูลเก่า (ถ้ามี)
student, subject, student_name, subject_name, score = load_data()

data_modified = False 

# ตรรกะหลักของโปรแกรม (คงเดิม ไม่มีการเปลี่ยนแปลง)
if student_name is None:
    student = int(input("จำนวนนักเรียน = "))
    subject = int(input("จำนวนวิชา = "))

    #เก็บข้อมูล (เมื่อมีการป้อนใหม่)
    student_name = []
    subject_name = []
    data_modified = True

    #รับชื่อนักเรียนโดยอิงจำนวนจากที่ถามตอนแรก
    for i in range(student):
        name = input(f"ชื่อนักเรียนคนที่ {i+1}: ")
        student_name.append(name)

    #รับชื่อวิชาโดยอิงจำนวนจากที่ถามตอนแรก
    for j in range(subject):
        subject_input = input(f"ชื่อวิชาที่ {j+1}: ")
        subject_name.append(subject_input)

    #เก็บคะแนนโดยใช้ Array
    score = np.zeros((student,subject))

    #ลูปตามจำนวนนักเรียน
    for i in range(student):
        print(f"\nนักเรียน: {student_name[i]}")

        #ลูปตามจำนวนวิชา
        for j in range(subject):
            while True:
                try:
                    input_score = float(input(f"คะแนนวิชา {subject_name[j]}: "))
                    if 0 <= input_score <= 100:
                        score[i,j] = input_score
                        break
                    #ถ้าใส่ข้อมูลไม่ถูกต้อง เช่น -100 , 101
                    else:
                        print("คะแนนต้องอยู่ระหว่าง 0-100 กรุณาป้อนใหม่")
                except ValueError: # หรือว่า judy
                    print("กรุณาป้อนตัวเลขเท่านั้น")
                    
#ใช้ลูปสร้าตารางคะแนน
header = "นักเรียน\t\t" + "\t".join(subject_name)
print("\n" + "="*10 + " ตารางคะแนน " + "="*10) 
print(header)
for i in range(student):
    row_scores = "\t".join([f"{s:.2f}" for s in score[i]])
    row = f"{student_name[i]:<15}\t{row_scores}" 
    print(row)
print("="*40) 

#คะแนนรวมรายบุคคล
totalscore = score.sum(axis=1)
print("\nคะแนนรวม:")
for i in range(student):
    print(f"{student_name[i]}: {totalscore[i]:.2f}")
print("="*40) 

#คะแนนเฉลี่ยรายวิชา
avg_per_subject = score.mean(axis=0)
print("\nคะแนนเฉลี่ยแต่ละวิชา:")
for j in range(subject): # วนลูปตาม subject
    print(f"วิชา {subject_name[j]}: {avg_per_subject[j]:.2f}") 
print("="*40) 

# เพิ่มคะแนนเฉลี่ยรายบุคคลเข้ามาตามคำแนะนำก่อนหน้า
avg_per_student = score.mean(axis=1)
print("\nคะแนนเฉลี่ยรายบุคคล:")
for i in range(student):
    print(f"{student_name[i]}: {avg_per_student[i]:.2f}")
print("="*40)

#เก็บค่าของคะแนนสูงสุด และ index
max_score_per_subject = score.max(axis=0)
student_idx_highest_score = score.argmax(axis=0)
print("\nผลสอบ (นักเรียนที่ได้คะแนนสูงสุดในแต่ละวิชา):")
for j in range(subject):
    student_idx = student_idx_highest_score[j]
    maxstudent = student_name[student_idx]
    highest = max_score_per_subject[j]
    print(f"วิชา {subject_name[j]}: {maxstudent} ได้ {highest:.2f}")
print("="*40)

#ตัววัดว่าสอบผ่านหรือไม่
passing_score = 50 
failed_mask = score < passing_score 

#ประกาศรายชื่อคนสอบตกพร้อมบอกคะแนน
print(f"\nสอบตก (คะแนนต่ำกว่า {passing_score}):")
failed_rows, failed_cols = np.where(failed_mask) 

if len(failed_rows) == 0:
    print("ไม่มีนักเรียนคนใดสอบตกในวิชาใดเลย!")
else:
    for i in range(len(failed_rows)):
        r = failed_rows[i]
        c = failed_cols[i]
        print(f"{student_name[r]} สอบตกวิชา {subject_name[c]} ได้ {score[r,c]:.2f} คะแนน")
        
print("="*40)

if student_name is not None and subject_name is not None and score is not None:
    if data_modified:
        save_data(student_name, subject_name, score)
    else:
        print("\nไม่มีการแก้ไขข้อมูล จึงไม่บันทึกไฟล์ใหม่")
else:
    print("\nไม่มีข้อมูลสำหรับบันทึก")