
farm_tasks = []

def add_task():
    name = input("ชื่องาน: ")
    category = input("ประเภทงาน (พืช/สัตว์): ")
    task = {"name": name, "category": category}
    farm_tasks.append(task)
    print("✅ เพิ่มงานเรียบร้อยแล้ว!\n")

def show_tasks():
    if not farm_tasks:
        print("📭 ยังไม่มีงานในระบบ\n")
        return
    print("📋 รายการงานทั้งหมด:")
    for i, task in enumerate(farm_tasks, start=1):
        print(f"{i}. {task['name']} ({task['category']})")
    print()

def delete_task():
    show_tasks()
    if not farm_tasks:
        return
    try:
        index = int(input("พิมพ์หมายเลขงานที่ต้องการลบ: ")) - 1
        if 0 <= index < len(farm_tasks):
            deleted = farm_tasks.pop(index)
            print(f"🗑 ลบงาน: {deleted['name']} เรียบร้อยแล้ว!\n")
        else:
            print("❌ หมายเลขไม่ถูกต้อง\n")
    except ValueError:
        print("⚠️ กรุณากรอกเลขนะ\n")

def summarize_tasks():
    summary = {}
    for task in farm_tasks:
        cat = task['category']
        summary[cat] = summary.get(cat, 0) + 1

    print("📊 สรุปจำนวนงานตามประเภท:")
    for cat, count in summary.items():
        print(f"- {cat}: {count} งาน")
    print()

def main():
    while True:
        print("📌 เมนูหลัก:")
        print("1. เพิ่มงานในฟาร์ม")
        print("2. แสดงรายการงานทั้งหมด")
        print("3. ลบงาน")
        print("4. สรุปจำนวนงานในแต่ละประเภท")
        print("5. ออกจากโปรแกรม")
        choice = input("เลือกเมนู (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            summarize_tasks()
        elif choice == "5":
            print("👋 ขอบคุณที่ใช้งาน!")
            break
        else:
            print("❗ กรุณาเลือกหมายเลข 1 ถึง 5 เท่านั้น\n")

if __name__ == "__main__":
    main()